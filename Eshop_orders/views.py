from django.contrib import messages
from django.shortcuts import render, redirect

from Eshop_products.models import products
from .forms import order_form
from .models import order, order_detail
from django.contrib.auth.decorators import login_required


# Create your views here.
def add_user_order(request):
    if request.user.is_anonymous:
        messages.warning(request, 'برای اضافه کردن به سبد خرید باید اول وارد حساب کاربری خود شوید. ')
    return add_user_order_main(request)


@login_required(login_url='/login')
def add_user_order_main(request):
    orderForm = order_form(request.POST or None)

    if orderForm.is_valid():
        order_cart = order.objects.filter(owner=request.user, is_paid=False).first()
        if order_cart is None:
            order_cart = order.objects.create(owner=request.user, is_paid=False)

        productId = orderForm.cleaned_data.get('product_id')
        count = orderForm.cleaned_data.get('count')
        product = products.objects.filter(id=productId).first()
        order_cart.order_detail_set.create(product_id=productId, price=product.price, count=count)
        messages.success(request, f'{product.title} با موفقیت به سبد خرید اضافه شد.')
    return redirect('/')
    # return redirect('/')
