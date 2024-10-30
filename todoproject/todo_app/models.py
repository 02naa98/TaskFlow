from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.conf import settings

class TaskList(models.Model):
    name=models.CharField(max_length=20) #リスト名

    def __str__(self):
        return self.name

class TaskCreate(models.Model):
    title=models.CharField(max_length=20) #タスクのタイトル
    description=models.TextField(null=True,blank=True) #説明
    due_date=models.DateTimeField(default=timezone.now) #期日
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #作成したユーザー

    is_starred=models.BooleanField(default=False) #スターの状態

    list=models.ForeignKey(TaskList,on_delete=models.CASCADE,default=1) #リストモデルとの関係

    def __str__(self):
        return self.title





