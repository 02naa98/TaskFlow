from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from django.shortcuts import redirect,render
from .models import TaskCreate,TaskList
from .forms import TaskForm,ListForm


#リスト作成
class ListCreateView(CreateView):
    model=TaskList
    form_class=ListForm
    template_name='todo_app/list_create.html'
    success_url=reverse_lazy('task_list')

class TaskCreateView(CreateView):
    model = TaskCreate #表示するモデル
    form_class = TaskForm #表示するフォーム
    template_name = 'todo_app/task_create.html'  # フォームを表示するテンプレートの指定
    success_url = reverse_lazy('task_list')  # 作成成功後のリダイレクト先

    def form_valid(self, form):
        form.instance.user=self.request.user #現在のユーザーを設定
        # フォームが有効な場合の処理
        return super().form_valid(form)
    def get_queryset(self): #現在ログインしているユーザーが作成したタスクを取得
        return TaskCreate.objects.filter(user=self.request.user)

class TaskListView(ListView):
    model = TaskCreate  # 表示するモデル
    template_name = 'todo_app/task_list.html'  # 使用するテンプレート
    context_object_name = 'tasks'  # テンプレートで使用するオブジェクト名


    def get_queryset(self):
        return TaskList.objects.prefetch_related('taskcreate_set').all()
    
    def get_context_data(self, **kwargs):
        # 基本のコンテキストを取得
        context = super().get_context_data(**kwargs)
        # リストを取得して 'lists' という名前でコンテキストに追加
        context['lists'] = self.get_queryset()  # リストごとのタスク
        print(context)
        return context

