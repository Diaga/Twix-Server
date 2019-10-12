from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Board, Task, Group

from . import serializers


class BoardViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin):
    """View set for Board model"""

    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.BoardSerializer

    queryset = Board.objects.all()

    def get_queryset(self):
        """Enforce scope"""
        user = self.request.user
        queryset = super(BoardViewSet, self).get_queryset().filter(
            twix_groups__users__in=[user, ]
        ).all()
        return queryset

    def view_board(self, request, *args, **kwargs):
        """Return associated boards"""
        serializer = self.get_serializer(
            self.get_queryset(), many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_board(self, request, *args, **kwargs):
        """Wrapper around create method for view set distinction"""
        return self.create(request, *args, **kwargs)


class BoardDetailViewSet(viewsets.GenericViewSet,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    """Detail view set for Board model"""

    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.BoardSerializer

    queryset = Board.objects.all()

    def get_queryset(self):
        """Enforce scope"""
        user = self.request.user
        queryset = super(BoardDetailViewSet, self).get_queryset().filter(
            twix_groups__users__in=[user, ]
        ).all()
        return queryset

    def view_board_by_id(self, request, *args, **kwargs):
        """Wrapper around retrieve method for view set distinction"""
        return self.retrieve(request, *args, **kwargs)

    def update_board_by_id(self, request, *args, **kwargs):
        """Wrapper around update method for view set distinction"""
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update partially"""
        kwargs.update({'partial': True})
        return super(BoardDetailViewSet, self).update(request, *args, **kwargs)

    def destroy_board_by_id(self, request, *args, **kwargs):
        """Wrapper around destroy method for view set distinction"""
        return self.destroy(request, *args, **kwargs)


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):
    """View set for Task model"""

    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.TaskSerializer

    queryset = Task.objects.all()

    def get_queryset(self):
        """Enforce scope"""
        user = self.request.user
        queryset = super(TaskViewSet, self).get_queryset().filter(
            board__twix_groups__users__in=[user, ]
        ).all()
        return queryset

    def view_task(self, request, *args, **kwargs):
        """Return associated tasks"""
        serializer = self.get_serializer(
            self.get_queryset(), many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_task(self, request, *args, **kwargs):
        """Wrapper around create method for view set distinction"""
        return self.create(request, *args, **kwargs)


class TaskDetailViewSet(viewsets.GenericViewSet,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    """Detail view set for Task model"""

    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.TaskSerializer

    queryset = Task.objects.all()

    def get_queryset(self):
        """Enforce scope"""
        user = self.request.user
        queryset = super(TaskDetailViewSet, self).get_queryset().filter(
            board__twix_groups__users__in=[user, ]
        ).all()
        return queryset

    def view_task_by_id(self, request, *args, **kwargs):
        """Wrapper around retrieve method for view set distinction"""
        return self.retrieve(request, *args, **kwargs)

    def update_task_by_id(self, request, *args, **kwargs):
        """Wrapper around update method for view set distinction"""
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update partially"""
        kwargs.update({'partial': True})
        return super(TaskDetailViewSet, self).update(request, *args, **kwargs)

    def destroy_task_by_id(self, request, *args, **kwargs):
        """Wrapper around destroy method for view set distinction"""
        return self.destroy(request, *args, **kwargs)


class GroupViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin):
    """View set for Group model"""

    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.GroupSerializer

    queryset = Group.objects.all()

    def get_queryset(self):
        """Enforce scope"""
        user = self.request.user
        queryset = super(GroupViewSet, self).get_queryset().filter(
            users_in=[user, ]
        ).all()
        return queryset

    def view_group(self, request, *args, **kwargs):
        """Return associated groups"""
        serializer = self.get_serializer(
            self.get_queryset(), many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_group(self, request, *args, **kwargs):
        """Wrapper around create method for view set distinction"""
        return self.create(request, *args, **kwargs)


class GroupDetailViewSet(viewsets.GenericViewSet,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    """Detail view set for Group model"""

    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.GroupSerializer

    queryset = Group.objects.all()

    def get_queryset(self):
        """Enforce scope"""
        user = self.request.user
        queryset = super(GroupDetailViewSet, self).get_queryset().filter(
            users_in=[user, ]
        ).all()
        return queryset

    def view_grade_by_id(self, request, *args, **kwargs):
        """Wrapper around retrieve method for view set distinction"""
        return self.retrieve(request, *args, **kwargs)

    def update_grade_by_id(self, request, *args, **kwargs):
        """Wrapper around update method for view set distinction"""
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update partially"""
        kwargs.update({'partial': True})
        return super(GroupDetailViewSet, self).update(request, *args, **kwargs)

    def destroy_grade_by_id(self, request, *args, **kwargs):
        """Wrapper around destroy method for view set distinction"""
        return self.destroy(request, *args, **kwargs)
