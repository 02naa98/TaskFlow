# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView 
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from .models import CustomUser

# サインアップビュー
class SignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

# ログインビュー
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    next_page = reverse_lazy('login')  # ログアウト後にリダイレクトするページ

