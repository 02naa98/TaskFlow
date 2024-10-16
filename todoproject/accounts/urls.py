# urls.py
from django.urls import path
from .views import SignupView
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(next_page='task_list'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
