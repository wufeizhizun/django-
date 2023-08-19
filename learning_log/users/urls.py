"""为应用程序users定义URL模式"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # 自定义登录页面
    path('login/', views.login_view, name='login'),
    # 注册页面
    path('register/', views.register, name='register'),
    # 包含默认的身份验证URL。
    path('', include('django.contrib.auth.urls')),
]
