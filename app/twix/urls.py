from django.urls import path, include

from rest_framework.routers import Route

from app.urls import router
from . import views

app_name = 'twix'

router.routes += [
    # Board View Route
    Route(
        url=r'^twix{trailing_slash}board{trailing_slash}$',
        mapping={
            'get': 'view_board',
            'post': 'create_board'
        },
        name='board-view',
        detail=False,
        initkwargs={'suffix': 'View'}
    ),

    # Board Detail Route
    Route(
        url=r'^twix{trailing_slash}board{trailing_slash}{lookup}'
            r'{trailing_slash}$',
        mapping={
            'get': 'view_board_by_id',
            'patch': 'update_board_by_id',
            'delete': 'destroy_board_by_id'
        },
        name='board-detail',
        detail=True,
        initkwargs={'suffix': 'Detail'}
    ),

    # Task View Route
    Route(
        url=r'^twix{trailing_slash}task{trailing_slash}$',
        mapping={
            'get': 'view_task',
            'post': 'create_task'
        },
        name='task-view',
        detail=False,
        initkwargs={'suffix': 'View'}
    ),

    # Task Detail Route
    Route(
        url=r'^twix{trailing_slash}task{trailing_slash}{lookup}'
            r'{trailing_slash}$',
        mapping={
            'get': 'view_task_by_id',
            'patch': 'update_task_by_id',
            'delete': 'destroy_task_by_id'
        },
        name='task-detail',
        detail=True,
        initkwargs={'suffix': 'Detail'}
    ),

    # Task Assigned View Route
    Route(
        url=r'^twix{trailing_slash}tasks{trailing_slash}assigned'
            r'{trailing_slash}$',
        mapping={
            'get': 'view_assigned_task',
        },
        name='task-assign-view',
        detail=False,
        initkwargs={'suffix': 'View'}
    ),

    # Task Assigned Detail Route
    Route(
        url=r'^twix{trailing_slash}tasks{trailing_slash}assigned'
            r'{trailing_slash}{lookup}{trailing_slash}$',
        mapping={
            'get': 'view_assigned_task_by_id',
            'patch': 'update_assigned_task_by_id'
        },
        name='task-assign-detail',
        detail=True,
        initkwargs={'suffix': 'Detail'}
    ),

    # Group View Route
    Route(
        url=r'^twix{trailing_slash}group{trailing_slash}$',
        mapping={
            'get': 'view_group',
            'post': 'create_group'
        },
        name='group-view',
        detail=False,
        initkwargs={'suffix': 'View'}
    ),

    # Group Detail Route
    Route(
        url=r'^twix{trailing_slash}group{trailing_slash}{lookup}'
            r'{trailing_slash}$',
        mapping={
            'get': 'view_group_by_id',
            'patch': 'update_group_by_id',
            'delete': 'destroy_group_by_id'
        },
        name='group-detail',
        detail=True,
        initkwargs={'suffix': 'Detail'}
    ),

    # Group Add Route
    Route(
        url=r'^twix{trailing_slash}group{trailing_slash}{lookup}'
            r'{trailing_slash}add{trailing_slash}$',
        mapping={
            'post': 'add_group_member_by_id'
        },
        name='group-add',
        detail=True,
        initkwargs={'suffix': 'Add'}
    ),

    # Group Remove Route
    Route(
        url=r'^twix{trailing_slash}group{trailing_slash}{lookup}'
            r'{trailing_slash}remove{trailing_slash}$',
        mapping={
            'post': 'remove_group_member_by_id',
        },
        name='group-remove',
        detail=True,
        initkwargs={'suffix': 'Remove'}
    ),
]

router.register('twix', views.BoardViewSet)
router.register('twix', views.BoardDetailViewSet)
router.register('twix', views.TaskViewSet)
router.register('twix', views.TaskDetailViewSet)
router.register('twix', views.GroupViewSet)
router.register('twix', views.GroupDetailViewSet)
router.register('twix', views.AssignedTaskViewSet)
router.register('twix', views.AssignedTaskDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'devices/', views.FCMDeviceCustomAuthViewSet.as_view(
        {'post': 'create'}),
         name='create_fcm_device')
]
