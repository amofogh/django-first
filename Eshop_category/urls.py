from django.urls import path
from .views import CategoryView

app_name = 'category'

urlpatterns = [
    path('category/<slug>', CategoryView.as_view(), name='category_view'),
]
