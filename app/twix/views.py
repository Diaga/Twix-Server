from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Board, Task, Group, User, AssignedTask
from core.permissions import IsGroupAdmin, check_permission, \
    check_object_permission

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
            user=user
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
            board__user=user
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
            board__user=user
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


class AssignedTaskViewSet(viewsets.GenericViewSet):
    """View set for Assigned Task model"""

    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.AssignedTaskSerializer

    queryset = AssignedTask.objects.all()

    def get_queryset(self):
        """Enforce scope"""
        user = self.request.user
        queryset = super(AssignedTaskViewSet, self).get_queryset()
        queryset = queryset.filter(
            group__admin=user
        ) | queryset.filter(
            user=user
        )
        return queryset.all()

    def view_assigned_task(self, request, *args, **kwargs):
        """View all assigned tasks"""
        serializer = self.get_serializer(
            self.get_queryset(), many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class AssignedTaskDetailViewSet(viewsets.GenericViewSet,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin):
    """Detail view set for Assigned Task model"""

    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.AssignedTaskSerializer

    queryset = AssignedTask.objects.all()

    def get_queryset(self):
        """Enforce scope"""
        user = self.request.user
        queryset = super(AssignedTaskDetailViewSet, self).get_queryset()
        queryset = queryset.filter(
            user=user
        )
        return queryset.all()

    def view_assigned_task_by_id(self, request, *args, **kwargs):
        """Wrapper around retrieve method for view set distinction"""
        return self.retrieve(request, *args, **kwargs)

    def update_assigned_task_by_id(self, request, *args, **kwargs):
        """Wrapper around update method for view set distinction"""
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update partially"""
        kwargs.update({'partial': True})
        return super(AssignedTaskDetailViewSet, self).update(request, *args,
                                                             **kwargs)


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
            users__in=[user, ]
        ) | super(GroupViewSet, self).get_queryset().filter(
            admin=user
        )
        queryset = queryset.all()
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
            users__in=[user, ]
        ) | super(GroupDetailViewSet, self).get_queryset().filter(
            admin=user
        )
        queryset = queryset.all()
        return queryset

    def view_group_by_id(self, request, *args, **kwargs):
        """Wrapper around retrieve method for view set distinction"""
        return self.retrieve(request, *args, **kwargs)

    def update_group_by_id(self, request, *args, **kwargs):
        """Wrapper around update method for view set distinction"""
        check_object_permission(request, self, self.get_object())
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update partially"""
        kwargs.update({'partial': True})
        return super(GroupDetailViewSet, self).update(request, *args, **kwargs)

    def destroy_group_by_id(self, request, *args, **kwargs):
        """Wrapper around destroy method for view set distinction"""
        check_object_permission(request, self, self.get_object())
        return self.destroy(request, *args, **kwargs)

    def add_group_member_by_id(self, request, *args, **kwargs):
        """Add action for group member"""
        check_object_permission(IsGroupAdmin, request, self, self.get_object())
        err_msg = 'User id required!'
        user_id = request.data.get('user')
        if user_id is not None:
            err_msg = 'No user with given id found!'
            user_exists = User.objects.filter(
                id=user_id
            ).exists()
            if user_exists:
                user = User.objects.filter(
                    id=user_id
                ).first()
                group = self.get_object()
                group.users.add(user)
                group.save()
                return Response(
                    self.get_serializer(group).data,
                    status=status.HTTP_200_OK
                )
        return Response(err_msg, status=status.HTTP_400_BAD_REQUEST)

    def remove_group_member_by_id(self, request, *args, **kwargs):
        """Delete action for group member"""
        check_object_permission(IsGroupAdmin, request, self, self.get_object())
        err_msg = 'User id required!'
        user_id = request.data.get('user')
        if user_id is not None:
            err_msg = 'No user with given id found!'
            user_exists = User.objects.filter(
                id=user_id
            ).exists()
            if user_exists:
                user = User.objects.filter(
                    id=user_id
                ).first()
                group = self.get_object()
                group.users.remove(user)
                group.save()
                return Response(
                    self.get_serializer(group).data,
                    status=status.HTTP_200_OK
                )
        return Response(err_msg, status=status.HTTP_400_BAD_REQUEST)
