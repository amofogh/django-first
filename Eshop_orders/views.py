import datetime
import time

from django.contrib import messages
from django.shortcuts import render, redirect

from Eshop_products.models import products
from .forms import order_form, discount_form
from .models import order, order_detail, discount
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json


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

        # check product if exists update it instead of create duplicate of it
        check_product = order_cart.order_detail_set.filter(product_id=productId).first()
        if check_product:
            last_count = check_product.count
            count = int(last_count) + int(count)
            check_product.count = count
            check_product.save()
            # order_cart.order_detail_set.update(product_id=productId, count=count)
            messages.success(request, f'تعداد {product.title} با موفقیت به روزرسانی شد .', extra_tags='order')
        else:
            order_cart.order_detail_set.create(product_id=productId, price=product.price, count=count)
            messages.success(request, f'{product.title} با موفقیت به سبد خرید اضافه شد.', extra_tags='order')

    return redirect('/')
    # return redirect('/')


def count_product_editor(request, productId, count):
    order_cart = order.objects.filter(owner=request.user, is_paid=False).first()
    if order_cart is None:
        order_cart = order.objects.create(owner=request.user, is_paid=False)

    check_product = order_cart.order_detail_set.filter(product_id=productId).first()
    if check_product:
        check_product.count += int(count)
        check_product.save()
    return redirect('/cart')


def check_in_cart(request, cart: order, productId):
    o = cart.order_detail_set.filter(product_id=productId).exists()


@login_required(login_url='/login')
def cart(request):
    user_cart = order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    discount_apply = 0
    discountForm = discount_form(request.POST or None)
    if discountForm.is_valid():
        code = discountForm.cleaned_data.get('code')
        check = discount.objects.filter(code=code).first()
        if check:
            time_fmt = '%Y-%m-%d %H:%M:%S'
            now = datetime.datetime.now().strftime(time_fmt)
            expire_date = check.expire_date.strftime(time_fmt)
            # ! the add_error is not working idk why i've been trying for 2 days
            # if expire_date < now:
            #     # raise forms.ValidationError('ایمیل وجود دارد.')
            #     discountForm.add_error(field='code', error='تاریخ انقضای کد تخفیف گذشته است.')
            # else:
            #     user_cart.discount = check

            user_cart.discount = check

    context = {
        'user_cart': user_cart,
        'details': None,
        'discount_form': discount_form,
        'discount': discount_apply,
    }
    if user_cart:
        context['details'] = user_cart.order_detail_set.all()
    return render(request, 'orders/cart.html', context)


@login_required(login_url='/login')
def remove_product_cart(request, order_detail_id):
    if order_detail_id:
        product = order_detail.objects.get_queryset().get(id=order_detail_id, order__owner_id=request.user.id)
        if product:
            product.delete()
    return redirect('/cart')


# zarinpal.com
MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
# amount = 11000  # Rial / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# email = 'email@example.com'  # Optional
# mobile = '09123456789'  # Optional
# Important: need to edit for really server.
CallbackURL = 'http://localhost:8000/verify/'


def send_request(request, discount_id=None):
    # important : i dont know these 2 function's works or not because i dont have merchant id
    total_price = 0
    user_cart = order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if user_cart:
        if discount_id:
            coupon = discount.objects.get_queryset().get(id=discount_id)
            user_cart.discount = coupon
        total_price = order.get_total_price(user_cart)
        print(total_price)
        description = f'order:{user_cart.id} - name:{user_cart.owner.get_username()}'
        req_data = {
            "merchant_id": MERCHANT,
            "amount": total_price,
            "callback_url": f'{CallbackURL}/{user_cart.id}',
            "description": description,
            # "metadata": {"mobile": mobile, "email": email}
        }
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
            req_data), headers=req_header)
        authority = req.json()['data']['authority']
        if len(req.json()['errors']) == 0:
            # save percentage discount used after payment
            user_cart.save()
            return redirect(ZP_API_STARTPAY.format(authority=authority))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request, order_id):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            # "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                user_cart = order.objects.filter(id=order_id, is_paid=False).first()
                user_cart.is_paid = True
                user_cart.payment_date = datetime.datetime.now()
                user_cart.ref_id = req.json()['data']['ref_id']
                user_cart.save()
                return redirect('/')
                # return HttpResponse('Transaction success.\nRefID: ' + str(
                #     req.json()['data']['ref_id']
                # ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
