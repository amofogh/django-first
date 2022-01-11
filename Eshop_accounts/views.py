from django.shortcuts import render, redirect, Http404
from django.contrib.auth import login, authenticate, logout

from utilities.EmailServices import send_email
from .forms import Login_Form, Register_Form, edit_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Eshop_setting.models import site_setting


# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    loginform = Login_Form(request.POST or None)
    if loginform.is_valid():
        username = loginform.cleaned_data['username']
        password = loginform.cleaned_data['password']
        remember = loginform.cleaned_data['remember_me']
        user = authenticate(request, password=password, username=username)
        if user:
            login(request, user)
            if not remember:
                request.session.set_expiry(0)  # after session closed user logout of the account
            return redirect('/')
        else:
            loginform.add_error('username', 'نام کاربری یا کلمه عبور نادرست است')
    context = {
        'login_form': loginform
    }
    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = Register_Form(request.POST or None)
    siteSetting = site_setting.objects.first()

    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        User.objects.create_user(username=username,
                                 email=email,
                                 password=password,
                                 first_name=first_name,
                                 last_name=last_name)
        send_email(siteSetting.site_title,
                   f"Hi, {username} you have been signed up successfully in {siteSetting.site_title}",
                   [email]
                   )
        user = authenticate(request, password=password, username=username)
        login(request, user)

        request.session.set_expiry(0)  # after session closed user logout of the account

        return redirect('/')

    context = {
        'register_form': register_form
    }
    return render(request, 'accounts/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def user_panel(request):
    return render(request, 'accounts/user_account_main.html')


@login_required(login_url='/login')
def edit_profile(request):
    user_id = request.user.id
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404('کاربر یافت نشد!')

    editForm = edit_form(request.POST or None, initial={'first_name': user.first_name, 'last_name': user.last_name, })
    if editForm.is_valid():
        firstname = editForm.cleaned_data.get('first_name')
        lastname = editForm.cleaned_data.get('last_name')
        user.first_name = firstname
        user.last_name = lastname
        user.save()

    context = {
        'edit_form': editForm
    }

    return render(request, 'accounts/edit_account.html', context)
