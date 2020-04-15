from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.contrib import messages
from .forms import RegisterForm, LoginForm

User = get_user_model()


def home(request):
    return render(request, 'myapp/index.html')


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.active = True
            person.save()
            messages.success(request, "User Created Successfully")
            return redirect('home')
        else:
            messages.info(request, "Something went wrong")
            return redirect('register')
    else:
        form = RegisterForm()
    front = {
        'form': form
    }
    return render(request, "myapp/register.html", front)


def login_request(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.info(request, "Login Failed")
            return redirect('login')
    front = {
        'form': form
    }
    return render(request, 'myapp/login.html', front)


def logout_request(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return render(request, 'myapp/logout.html')
