from rest_framework import serializers

from core.models import Board, Task, Group
from core.serializers import DynamicModelSerializer
from user.serializers import UserSerializer


class BoardSerializer(DynamicModelSerializer):
    """Serializer for Board model"""

    group = serializers.SerializerMethodField('get_group')

    def get_group(self, obj):
        """Return associated group"""
        return GroupSerializer(obj.group).data

    class Meta:
        model = Board
        fields = ('id', 'name', 'is_personal', 'group')
        read_only_fields = ('id', )


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model"""

    board = BoardSerializer()

    class Meta:
        model = Task
        fields = ('id', 'name', 'isDone', 'board')
        read_only_fields = ('id', )


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model"""

    admin = UserSerializer()
    users = UserSerializer()
    boards = BoardSerializer(many=True, exclude=['group', ])

    class Meta:
        model = Group
        fields = ('id', 'name', 'admin', 'users', 'boards')
        read_only_fields = ('id', )
