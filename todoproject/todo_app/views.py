from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from django.views import View
from django.shortcuts import redirect,render,get_object_or_404
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

    #返り値の中身はフィルタリングされたデータが入ったリスト
    def get_queryset(self):
        TaskList.objects.prefetch_related('taskcreate_set').all()
        list_ids=self.request.GET.getlist('list_ids')
        print(f"list_ids: {list_ids}")  # list_idsの内容を出力
        if list_ids:
            queryset = TaskCreate.objects.filter(list__id__in=list_ids, user=self.request.user)
            print(f"Filtered tasks: {queryset}")  # フィルタリングされたタスクを出力
            return TaskCreate.objects.filter(list__id__in=list_ids,user=self.request.user)
        else:
            return TaskCreate.objects.filter(user=self.request.user)
        
    def get_context_data(self, **kwargs):
        # 基本のコンテキストを取得
        context = super().get_context_data(**kwargs)
        
        list_ids = self.request.GET.getlist('list_ids')
        # リストを取得して 'lists' という名前でコンテキストに追加
        if list_ids:
            context['lists'] = TaskList.objects.filter(id__in=list_ids)  # 選択されたリストのみ取得
        else:
            context['lists'] = TaskList.objects.all()  # チェックがない場合は全リスト取得
        
        context['filtered_tasks']=self.get_queryset()
        
        return context

class ToggleStarView(View):
    def get(self, task_id):
        task = get_object_or_404(TaskCreate, id=task_id)
        task.is_starred = not task.is_starred  # スターの状態を反転
        task.save()  # タスクを保存
        return redirect('task_list')  # タスク一覧ページにリダイレクト