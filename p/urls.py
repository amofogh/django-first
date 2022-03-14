"""p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from p.views import home_page, header, footer, header_references
from Eshop_category.views import categories_partial

urlpatterns = [
    path('', include('Eshop_accounts.urls', namespace='accounts')),
    path('', include('Eshop_products.urls', namespace='products')),
    path('', include('Eshop_tag.urls', namespace='tag')),
    path('', include('Eshop_category.urls', namespace='category')),
    path('', include('Eshop_contact.urls', namespace='contact')),
    path('', include('Eshop_orders.urls', namespace='orders')),
    path('', include('Eshop_comments.urls', namespace='comments')),
    path('', include('Eshop_news.urls', namespace='blog')),
    path('api/', include('api.urls', namespace='api')),
    path('categories_partial', categories_partial, name='categories_partial'),
    path('header/<title>', header_references, name='headerReferences'),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('', home_page),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
