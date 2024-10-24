from django.urls import path
from .views import TaskCreateView,TaskListView,TaskUpdateView,TaskDeleteView,ListCreateView,ListUpdateView,ListDeleteView,ToggleStarView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),  # タスク一覧
    path('task/create/', TaskCreateView.as_view(), name='task_create'),  #タスク作成
    path('list/create/', ListCreateView.as_view(), name='list_create'),  #リスト作成
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'), #タスク更新
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'), #タスク削除
    path('list/update/<int:pk>/', ListUpdateView.as_view(), name='list_update'), #リスト更新
    path('list/delete/<int:pk>/', ListDeleteView.as_view(), name='list_delete'), #リスト削除
    #動的url(ページ遷移が小さい)
    path('tasks/<int:list_id>/', TaskListView.as_view(), name='task_list_by_list'),
    path('tasks/toggle_star/<int:task_id>/', ToggleStarView.as_view(), name='toggle_star'), #スタートグル
]
