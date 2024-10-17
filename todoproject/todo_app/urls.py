from django.urls import path
from .views import TaskCreateView,TaskListView,ListCreateView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),  # タスク一覧
    path('tasks/list/<int:list_id>/', TaskListView.as_view(), name='task-list-by-list'),  # リストIDを受け取るURL
    path('list/create/', ListCreateView.as_view(), name='list_create'),  #リスト作成
    path('task/create/', TaskCreateView.as_view(), name='task_create'),  #タスク作成
]
