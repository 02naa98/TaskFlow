from django.urls import path
from .views import TaskCreateView,TaskListView,ListCreateView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),  # タスク一覧
    path('tasks/test/', TaskListView.as_view(), name='task_test'), #tasks by listで使ってた
    path('tasks/<int:list_id>/', TaskListView.as_view(), name='task_list_by_list'),
    path('list/create/', ListCreateView.as_view(), name='list_create'),  #リスト作成
    path('task/create/', TaskCreateView.as_view(), name='task_create'),  #タスク作成
]
