from django.urls import path, include

from rest_framework.routers import Route

from app.urls import router
from . import views

app_name = 'user'

router.routes += [
    # User View Route
    Route(
        url='^user{trailing_slash}$',
        mapping={
            'get': 'view_user',
            'post': 'create_user',
            'patch': 'update_user',
            'delete': 'delete_user'
        },
        name='user-view',
        detail=False,
        initkwargs={'suffix': 'View'}
    ),

    # User List Route
    Route(
        url=r'^users{trailing_slash}$',
        mapping={
            'get': 'list_user'
        },
        name='user-list',
        detail=False,
        initkwargs={'suffix': 'List'}
    )
]

router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.AuthTokenViewSet.as_view(), name='auth-token')
]
