from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from .models import TaskCreate
from .forms import TaskForm

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
