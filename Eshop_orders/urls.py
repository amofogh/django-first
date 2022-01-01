from django.urls import path
from .views import add_user_order

app_name = 'orders'

urlpatterns = [
    path('add-user-order', add_user_order, name='add_user_order')
]