from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import Login_Form


# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    loginform = Login_Form(request.POST or None)
    if loginform.is_valid():
        username = loginform.cleaned_data['username']
        password = loginform.cleaned_data['password']
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {
        'login_form': loginform
    }
    return render(request, 'accounts/login.html', context)


def register_user(request):
    context = {}
    return render(request, 'accounts/register.html', context)
