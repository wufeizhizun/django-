from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="用户名", max_length=254)
    password1 = forms.CharField(label="密码", widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="用户名", max_length=254)
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
