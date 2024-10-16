from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.conf import settings

class TaskCreate(models.Model):
    title=models.CharField(max_length=20) #タスクのタイトル
    description=models.TextField(null=True,blank=True) #説明
    due_date=models.DateTimeField(default=timezone.now) #期日
    priority=models.IntegerField(choices=[(1, '高'), (2, '中'), (3, '低')]) #優先度(仮)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #作成したユーザー

    def __str__(self):
        return self.title



