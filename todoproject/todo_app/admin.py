from django.contrib import admin
from .models import CustomUser,TaskCreate,TaskList

admin.site.register(CustomUser)
admin.site.register(TaskCreate)
admin.site.register(TaskList)


class TaskInline(admin.TabularInline):
    model = TaskCreate
    extra = 0  # 新しいタスクの追加を無効化したい場合は0に設定

class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [TaskInline]  # Taskを内包することでリストのタスクを表示

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'due_date', 'priority')
    list_filter = ('list',)  # リストでフィルタリングできるようにする
