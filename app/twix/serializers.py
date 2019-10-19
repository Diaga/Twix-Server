from rest_framework import serializers

from core.models import Board, Task, Group, User
from core.serializers import DynamicModelSerializer
from user.serializers import UserSerializer


class BoardSerializer(DynamicModelSerializer):
    """Serializer for Board model"""

    class Meta:
        model = Board
        fields = ('id', 'name', 'is_personal', 'group')
        read_only_fields = ()


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model"""

    board = BoardSerializer()
    group = serializers.SerializerMethodField('get_group')

    def get_group(self, obj):
        """Return associated group"""
        return GroupSerializer(obj.group).data

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'is_done', 'is_assigned', 'board', 'group',
            'due_date',
            'remind_me',)
        read_only_fields = ()


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model"""

    admin = UserSerializer(read_only=True)
    admin_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=User.objects.all())
    users = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'admin', 'users', 'admin_id')
        read_only_fields = ()

    def create(self, validated_data):
        """Override to link admin"""
        admin_id = validated_data.pop('admin_id')
        users = validated_data.pop('users')
        group = Group.objects.create(
            admin=admin_id, **validated_data
        )
        group.users.set(users)
        group.save()
        return group
