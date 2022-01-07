from django.urls import path

from Eshop_news.views import blog_detail, blog_list

app_name = 'blog'

urlpatterns = [
    path('blog-detail/<news_id>', blog_detail, name='blog_detail'),
    path('blog', blog_list.as_view(), name='blog_list')
]
