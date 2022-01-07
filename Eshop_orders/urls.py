from django.urls import path
from .views import add_user_order, cart, send_request, verify, remove_product_cart, count_product_editor

app_name = 'orders'

urlpatterns = [
    path('add-user-order', add_user_order, name='add_user_order'),
    path('cart', cart, name='cart'),
    path('remove_product/<order_detail_id>', remove_product_cart),
    path('edit_count/<productId>/<count>', count_product_editor),
    path('request/', send_request, name='request'),
    path('request/<discount_id>', send_request),
    path('verify/<order_id>', verify, name='verify'),
]