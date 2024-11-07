from django.urls import path
from .views import TaskCreateView,TaskListView,TaskUpdateView,TaskDeleteView,ListCreateView,ListUpdateView,ListDeleteView,ListSelectView,ToggleStarView,ProfileView
from . import views

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),  # タスク一覧
    path('task/create/', TaskCreateView.as_view(), name='task_create'),  #タスク作成
    path('list/create/', ListCreateView.as_view(), name='list_create'),  #リスト作成
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'), #タスク更新
    path('list/update/<int:pk>/', ListUpdateView.as_view(), name='list_update'), #リスト更新
    path('select-list/', ListSelectView.as_view(), name='select_list'),#リスト選択
    path('calendar/', views.index, name='only_calendar'),#カレンダー
    path('profile/<str:username>/', ProfileView.as_view(), name='temporary_profile'),#プロフィール
    #動的url(ページ遷移が小さい)
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'), #タスク削除
    path('list/delete/<int:pk>/', ListDeleteView.as_view(), name='list_delete'), #リスト削除
    path('tasks/toggle_star/<int:task_id>/', ToggleStarView.as_view(), name='toggle_star'), #スタートグル

    #テスト
    path('display_a/', views.display_a, name='display_a'),

]
