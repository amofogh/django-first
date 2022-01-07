from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from Eshop_comments.forms import comment_form
from .models import comments


@login_required(login_url='/login')
def comment(request):
    commentForm = comment_form(request.POST or None)

    if commentForm.is_valid():
        product_id = commentForm.cleaned_data.get('product_id')
        email = commentForm.cleaned_data.get('email')
        name = commentForm.cleaned_data.get('name')
        text = commentForm.cleaned_data.get('text')

        comments.objects.create(name=name, email=email, text=text, product_id=product_id)
        messages.success(request, 'نظر شما با موفقیت ثبت شد.')

        return redirect(f'/products/{product_id}')

    messages.info(request, 'مشکلی در ثبت نظر شما پیش امده است لطفا مجددا تلاش کنید.')
    return redirect('/')
