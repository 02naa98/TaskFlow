from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from .models import TaskCreate
from .forms import TaskForm

class TaskCreateView(CreateView):
    model = TaskCreate #表示するモデル
    form_class = TaskForm #表示するフォーム
    template_name = 'task_form.html'  # フォームを表示するテンプレートの指定
    success_url = reverse_lazy('task_list')  # 作成成功後のリダイレクト先

    def form_valid(self, form):
        # フォームが有効な場合の処理
        return super().form_valid(form)

class TaskListView(ListView):
    model = TaskCreate  # 表示するモデル
    template_name = 'task_list.html'  # 使用するテンプレート
    context_object_name = 'tasks'  # テンプレートで使用するオブジェクト名
