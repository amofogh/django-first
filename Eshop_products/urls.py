from django.urls import path, include
from .views import Products_list, Search_item, product_detail

# from .views import  Product_detail

app_name = 'products'

urlpatterns = [
    path('products', Products_list.as_view(), name='product_list'),
    path('products/search', Search_item.as_view(), name='search_item'),
    # path('products/<productId>', Product_detail.as_view(), name='product_detail'),
    path('products/<productId>', product_detail, name='product_detail'),

]
