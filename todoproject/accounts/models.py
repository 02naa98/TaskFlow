from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username=models.CharField(null=False,unique=True) #ユーザーネーム
    age=models.IntegerField(null=True, blank=True) #年齢
    mail=models.EmailField(max_length=30,null=True, blank=True,unique=True) #メールアドレス
