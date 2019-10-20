from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from core.models import User
from core.permissions import check_permission, IsAppToken

from . import serializers


class UserViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    """View set for User model"""
    authentication_classes = [TokenAuthentication, ]

    permission_classes = [IsAuthenticated, ]

    serializer_class = serializers.UserSerializer

    queryset = User.objects.all()

    def get_queryset(self):
        """Remove admin & registration"""
        queryset = super(UserViewSet, self).get_queryset().exclude(
            email='admin@asperal.com'
        ).all()
        queryset = queryset.exclude(
            email='register@twix.com'
        ).all()
        return queryset

    def get_object(self):
        """Return logged in user"""
        return self.request.user

    def view_user(self, request, *args, **kwargs):
        """Return logged in user"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_user(self, request, *args, **kwargs):
        """Allow only if public app token included"""
        check_permission(IsAppToken, request, self)
        return self.create(request, *args, **kwargs)

    def update_user(self, request, *args, **kwargs):
        """Update logged in user partially"""
        kwargs.update({'partial': True})
        return self.update(request, *args, **kwargs)

    def destroy_user(self, request, *args, **kwargs):
        """Delete logged in user"""
        return self.destroy(request, *args, **kwargs)

    def list_user(self, request, *args, **kwargs):
        """List all users"""
        queryset = self.get_queryset()
        email = request.GET.get('email', None)
        if email is not None:
            queryset = queryset.filter(
                email__regex=rf'{email}'
            ).all()
        serializer = self.get_serializer(
            queryset, many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthTokenViewSet(ObtainAuthToken):
    """Custom token authentication view set"""
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
