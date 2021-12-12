from django.urls import path, include
from .views import tag_list

app_name = 'tag'

urlpatterns = [
    path('tag/<slug>', tag_list.as_view(), name='tag_list'),
]
