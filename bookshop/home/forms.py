from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text="Обязательное поле")

    class Meta:
        model = MyUser
        fields = ('login', 'email', 'birth_date')


class LoginForm(AuthenticationForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
