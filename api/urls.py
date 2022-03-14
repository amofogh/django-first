from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet,NewsViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register('product',ProductViewSet,'product-view-set')
router.register('news',NewsViewSet,'news-view-set')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]