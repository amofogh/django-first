from django.shortcuts import render, redirect
from .models import contact_us
from .forms import contact_us_form
from django.contrib import messages
from Eshop_setting.models import site_setting


# Create your views here.

def contact_us_view(request):
    contact_form = contact_us_form(request.POST or None)
    setting = site_setting.objects.first()
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        contact_us.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        messages.success(request, 'پیام شما با موفقیت ارسال شد. ')
        return redirect('/')

    context = {
        'form': contact_form,
        'setting': setting
    }
    return render(request, 'contact_us/contact_us.html', context)


def about_us(request):
    setting = site_setting.objects.first()
    context = {
        'setting':setting
    }
    return render(request, 'contact_us/about_us.html', context)
