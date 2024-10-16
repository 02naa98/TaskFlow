from django.contrib import admin
from .models import CustomUser,TaskCreate

admin.site.register(CustomUser)
admin.site.register(TaskCreate)