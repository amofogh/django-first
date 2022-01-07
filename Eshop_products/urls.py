from django.urls import path, include
from .views import Products_list, Search_item, product_detail, last_Products_list, most_visited_Products_list

# from .views import  Product_detail

app_name = 'products'

urlpatterns = [
    path('products', Products_list.as_view(), name='product_list'),
    path('last-products', last_Products_list.as_view(), name='last_product_list'),
    path(' most_visited-products', most_visited_Products_list.as_view(), name='most_visited_products'),
    path('products/search', Search_item.as_view(), name='search_item'),
    # path('products/<productId>', Product_detail.as_view(), name='product_detail'),
    path('products/<productId>', product_detail, name='product_detail'),

]
