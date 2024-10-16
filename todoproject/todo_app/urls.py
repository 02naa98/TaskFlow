from django.urls import path
from .views import TaskCreateView,TaskListView

urlpatterns = [
    path('task/create/', TaskCreateView.as_view(), name='task_create'),  #タスク作成
    path('tasks/', TaskListView.as_view(), name='task_list'),  # タスク一覧
]
