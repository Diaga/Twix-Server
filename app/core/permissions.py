from rest_framework import permissions
from django.contrib.auth.models import Group

def check_permission(permission, request, view):
    """Check permission explicitly"""
    if not permission().has_permission(request, view):
        view.permission_denied(
            request, message=getattr(permission, 'message', None)
        )


def check_object_permission(permission, request, view, obj):
    """Check object permission explicitly"""
    if not permission().has_object_permission(request, view, obj):
        view.permission_denied(
            request, message=getattr(permission, 'message', None)
        )


class IsAppToken(permissions.BasePermission):
    """Global permission to check if AppToken included"""
    message = 'App Token required!'

    def has_permission(self, request, view):
        """Logic for checking IsAppToken"""
        app_token_group = request.user.groups.filter(
            name='App Token'
        ).exists()
        return app_token_group
