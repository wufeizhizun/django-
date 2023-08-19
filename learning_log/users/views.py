from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, login
from .forms import CustomUserCreationForm, CustomAuthenticationForm  # 导入自定义的表单

def register(request):
    """注册新用户。"""
    if request.method != 'POST':
        # 显示空的注册表单。
        form = CustomUserCreationForm()  # 使用自定义表单
    else:
        # 处理填写好的表单
        form = CustomUserCreationForm(data=request.POST)  # 使用自定义表单
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            login(request, new_user)
            return redirect('learning_logs:index')

    # 显示空表单或指出表单无效。
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def login_view(request):
    """登录用户。"""
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)  # 使用自定义表单
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # 使用Django的auth_login方法
            return redirect('learning_logs:index')
    else:
        form = CustomAuthenticationForm()  # 使用自定义表单

    context = {'form': form}
    return render(request, 'registration/login.html', context)
