from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.views import View
from django.shortcuts import redirect,render,get_object_or_404
from django.http import JsonResponse
from .models import TaskCreate,TaskList
from .forms import TaskForm,ListForm


#リスト作成 
class ListCreateView(CreateView):
    model=TaskList
    form_class=ListForm
    template_name='todo_app/list_create.html'
    success_url=reverse_lazy('task_list')

#タスク作成+質問
class TaskCreateView(CreateView):
    model = TaskCreate #表示するモデル
    form_class = TaskForm #表示するフォーム
    template_name = 'todo_app/task_create.html'  # フォームを表示するテンプレートの指定
    success_url = reverse_lazy('task_list')  # 作成成功後のリダイレクト先

    def form_valid(self, form):
        form.instance.user=self.request.user #現在のユーザーを設定

        #クエリパラメータからList_idを取得
        list_id=self.request.GET.get('list_id',None)
        if list_id:
            #クエリパラメータのList_idに対応するリストを取得
            form.instance.list=get_object_or_404(TaskList,id=list_id)
        else:
            #List_idが指定されていない場合、デフォルトリストを指定
            form.instance.list=get_object_or_404(TaskList,id=1)
        return super().form_valid(form)
    
    def get_queryset(self): #現在ログインしているユーザーが作成したタスクを取得
        return TaskCreate.objects.filter(user=self.request.user)
    
    def post(self,request,*args,**kwargs):
        #質問フォームへの回答が送信された場合
        return super().post(request,*args,**kwargs)

#タスク一覧表示
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

#スターの付け外しとスタータスクの表示
class ToggleStarView(View):
    def post(self,request,task_id):
        print(f"Request POST data: {request.POST}")  # POSTリクエストのデータを表示
        print(f"Received task_id: {task_id}")  # デバッグ用
        task = get_object_or_404(TaskCreate, id=task_id)
        task.is_starred = not task.is_starred  # スターの状態を反転
        task.save()  # タスクを保存
        print(f"After toggle, is_starred: {task.is_starred}")

        return redirect('task_list')  # タスク一覧ページにリダイレクト

#タスクのUpdate
class TaskUpdateView(UpdateView):
    model=TaskCreate
    form_class=TaskForm
    template_name='todo_app/task_update.html'
    success_url=reverse_lazy('task_list')

    def get_object(self, queryset=None):
        #デバッグ
        print(f"kwargs: {self.kwargs}")
        pk = self.kwargs.get('pk')
        if pk is None:
            raise ValueError("pkが定義されていません")
        print(f"Requested task ID: {self.kwargs.get('pk')}")

        obj = super().get_object(queryset)
        print(obj)  # デバッグ用にタスクオブジェクトを表示
        return obj

#タスクのDelete
class TaskDeleteView(DeleteView):
    model=TaskCreate
    success_url=reverse_lazy('task_list')

#リストのUpdate(rename)
class ListUpdateView(UpdateView):
    model=TaskList
    form_class=ListForm
    template_name='todo_app/list_update.html'
    success_url=reverse_lazy('task_list')

#リストのDelete(リスト内のタスクごと削除)
class ListDeleteView(DeleteView):
    model=TaskList
    success_url=reverse_lazy('task_list')

    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        #リスト内のタスク削除
        self.object.taskcreate_set.all().delete()
        self.object.delete() #リスト削除
        return redirect(self.success_url)