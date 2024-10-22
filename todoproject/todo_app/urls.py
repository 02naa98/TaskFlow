from django.urls import path
from .views import TaskCreateView,TaskListView,TaskUpdateView,TaskDeleteView,ListCreateView,ToggleStarView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),  # タスク一覧
    path('list/create/', ListCreateView.as_view(), name='list_create'),  #リスト作成
    path('task/create/', TaskCreateView.as_view(), name='task_create'),  #タスク作成
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'), #subbranch2
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'), #subbranch3
    #動的url(ページ遷移が小さい)
    path('tasks/<int:list_id>/', TaskListView.as_view(), name='task_list_by_list'),
    path('tasks/toggle_star/<int:task_id>/', ToggleStarView.as_view(), name='toggle_star'),
]
