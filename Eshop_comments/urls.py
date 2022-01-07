from django.urls import path, include

from Eshop_comments.views import comment

app_name = 'comments'

urlpatterns = [
    path('comments', comment)
]