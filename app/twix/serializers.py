from rest_framework import serializers

from core.models import Board, Task, Group, User, AssignedTask
from core.serializers import DynamicModelSerializer
from user.serializers import UserSerializer


class BoardSerializer(DynamicModelSerializer):
    """Serializer for Board model"""

    class Meta:
        model = Board
        fields = ('id', 'name', 'is_personal', 'user')
        read_only_fields = ()


class TaskSerializer(DynamicModelSerializer):
    """Serializer for Task model"""

    board = BoardSerializer(read_only=True)
    board_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=Board.objects.all())
    group = serializers.SerializerMethodField('get_group')
    group_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=Group.objects.all())

    def get_group(self, obj):
        """Return associated group"""
        return GroupSerializer(obj.group, read_only=True).data

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'is_done', 'is_assigned', 'board', 'group',
            'due_date', 'remind_me', 'board_id', 'group_id', 'notes')
        read_only_fields = ()

    def create(self, validated_data):
        """Override to link board & group"""
        board = validated_data.pop('board_id', None)

        group = validated_data.pop('group_id', None)

        task = Task.objects.create(
            board=board, **validated_data, group=group
        )
        return task

    def update(self, instance, validated_data):
        """Override to link board & group"""
        board = validated_data.pop('board_id', None)
        if board is not None:
            instance.board = board

        group = validated_data.pop('group_id', None)
        if group is not None:
            instance.group = group

        instance.save()

        super(TaskSerializer, self).update(instance, validated_data)

        return instance


class AssignedTaskSerializer(serializers.ModelSerializer):
    """Serializer for AssignedTask model"""

    task = TaskSerializer(read_only=True, exclude=['group', ])
    user = UserSerializer(read_only=True)
    group = serializers.SerializerMethodField('get_group')

    def get_group(self, obj):
        """Return associated group"""
        return GroupSerializer(obj.group, read_only=True).data

    class Meta:
        model = AssignedTask
        fields = ('id', 'is_done', 'task', 'group', 'user')
        read_only_fields = ('id',)


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model"""

    admin = UserSerializer(read_only=True)
    admin_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=User.objects.all())
    users = UserSerializer(many=True, required=False)

    class Meta:
        model = Group
        fields = ('id', 'name', 'admin', 'users', 'admin_id')
        read_only_fields = ()

    def create(self, validated_data):
        """Override to link admin"""
        admin_id = validated_data.pop('admin_id', None)
        users = validated_data.pop('users', None)
        group = Group.objects.create(
            admin=admin_id, **validated_data
        )
        if users is not None:
            group.users.set(users)
        group.save()
        return group
