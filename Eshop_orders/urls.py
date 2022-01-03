from django.urls import path
from .views import add_user_order, cart, send_request, verify

app_name = 'orders'

urlpatterns = [
    path('add-user-order', add_user_order, name='add_user_order'),
    path('cart', cart, name='cart'),
    path('request', send_request, name='request'),
    path('verify/<order_id>', verify, name='verify'),
]