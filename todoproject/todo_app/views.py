from django.db.models.query import QuerySet
from datetime import datetime
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.views import View, generic
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import TaskCreate, TaskList
from .forms import TaskForm, ListForm, ListSelectForm
from django.utils.safestring import mark_safe
from accounts.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

# 基本ビュー
# ==========================

# CSS適用テストview
def display_a(request):
    return render(request, 'todo_app/display_a.html')

# FullCalendar カレンダーテスト
def index(request):
    """
    カレンダー画面
    """
    template = loader.get_template("todo_app/calendar.html")
    return HttpResponse(template.render())

# ユーザー関連ビュー
# ==========================

# プロフィールページ
class ProfileView(DetailView, LoginRequiredMixin):
    model = CustomUser
    template_name = 'todo_app/profile.html'
    context_object_name = 'profile_user'
    slug_field = 'username'  # usernameフィールドをスラグとして使用
    slug_url_kwarg = 'username'  # URLから渡されるパラメータ名

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password'] = 'YourPassword'  # これは実際の実装では避けるべき
        return context

# リスト管理関連ビュー
# ==========================

# 簡易チェックリスト
class ListSelectView(FormView):
    template_name = 'todo_app/list_select_form.html'
    form_class = ListSelectForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        return super().form_valid(form)  # フォームが正常に送信された場合はリダイレクト

# リスト作成
class ListCreateView(CreateView):
    model = TaskList
    form_class = ListForm
    template_name = 'todo_app/list_create.html'
    success_url = reverse_lazy('task_list')

# リストのUpdate（名前変更）
class ListUpdateView(UpdateView):
    model = TaskList
    form_class = ListForm
    template_name = 'todo_app/list_update.html'
    success_url = reverse_lazy('task_list')

# リストのDelete（リスト内のタスクごと削除）
class ListDeleteView(DeleteView):
    model = TaskList
    success_url = reverse_lazy('task_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.taskcreate_set.all().delete()  # リスト内のタスク削除
        self.object.delete()  # リスト削除
        return redirect(self.success_url)

# タスク管理関連ビュー
# ==========================

# タスク一覧表示
class TaskListView(ListView):
    model = TaskCreate
    template_name = 'todo_app/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return TaskCreate.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_name = self.request.GET.get('filter_name', '')
        if filter_name:
             # 部分一致でフィルタリングされたリストを取得
            context['lists'] = TaskList.objects.filter(name__icontains=filter_name)
            # フィルタリングされたメッセージを作成
            context['filter_message'] = f"検索結果: 名前に 「{filter_name}」 を含むリスト"
        else:
            # POSTリクエストで選択されたリストがある場合
            selected_lists = getattr(self, 'selected_lists', None)
            if selected_lists:
                context['lists'] = TaskList.objects.filter(id__in=selected_lists)
                context['selected_lists'] = selected_lists
            else:
                context['lists'] = TaskList.objects.all()
        
        # チェックボックス選択状態の保持
        context['selected_list_ids'] = [int(id) for id in getattr(self, 'selected_lists', [])]
        
        return context
    
    # データの受け取りとレスポンス (未実装)
    def post(self, request, *args, **kwargs):
        # チェックボックスで選ばれたリストIDをPOSTデータから取得
        selected_lists = request.POST.getlist('list-checkbox')
        
        # デバッグ用: selected_listsの内容を確認
        print("選ばれたリストID:", selected_lists)
        
        # 選ばれたリストIDがある場合
        if selected_lists:
            # 選択されたリストIDを保存
            self.selected_lists = selected_lists
            return self.get(request, *args, **kwargs)
        else:
            # リストが選ばれていない場合は、全タスクを表示
            return HttpResponseRedirect(reverse('task_list'))

# タスク作成＋質問
class TaskCreateView(CreateView):
    model = TaskCreate
    form_class = TaskForm
    template_name = 'todo_app/task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        list_id = self.request.GET.get('list_id', None)
        if list_id:
            form.instance.list = get_object_or_404(TaskList, id=list_id)
        else:
            form.instance.list = get_object_or_404(TaskList, id=1)
        return super().form_valid(form)

    def get_queryset(self):
        return TaskCreate.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# スターの付け外しとスタータスクの表示
class ToggleStarView(View):
    def post(self, request, task_id):
        task = get_object_or_404(TaskCreate, id=task_id)
        task.is_starred = not task.is_starred  # スターの状態を反転
        task.save()  # タスクを保存
        return redirect('task_list')

# タスクのUpdate
class TaskUpdateView(UpdateView):
    model = TaskCreate
    form_class = TaskForm
    template_name = 'todo_app/task_update.html'
    success_url = reverse_lazy('task_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise ValueError("pkが定義されていません")
        obj = super().get_object(queryset)
        return obj

# タスクのDelete
class TaskDeleteView(DeleteView):
    model = TaskCreate
    success_url = reverse_lazy('task_list')
