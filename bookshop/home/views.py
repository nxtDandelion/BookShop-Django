from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import MyUser

from rest_framework.decorators import api_view

from .forms import SignUpForm, LoginForm, ProfileEditForm


def home(request):
    return render(request, 'home/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(login=user_login, password=password)
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'home/signin.html', {'form': form})


@login_required
def profile_view(request, user_id):
    user_profile = get_object_or_404(MyUser, id=user_id)
    if request.user != user_profile:
        return redirect('/')
    if request.method == 'POST':
        if 'action' in request.POST:
            if request.POST['action'] == 'logout':
                logout(request)
                return redirect('/')
        form = ProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id)
    else:
        form = ProfileEditForm(instance=user_profile)
    return render(request, 'home/profile.html',
                  {'user_profile': user_profile, 'form': form})
