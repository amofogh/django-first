from django_filters.rest_framework import DjangoFilterBackend,FilterSet
import django_filters
from rest_framework import viewsets

from Eshop_products.models import products
from Eshop_news.models import news
from .serializers import ProductSerilizer,NewsSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.

class ProductFilter(FilterSet):
    title = django_filters.CharFilter('title','icontains')
    description = django_filters.CharFilter('description','icontains')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    tag = django_filters.CharFilter('tag__title','icontains')
    category = django_filters.CharFilter('category__title','icontains')
    
    class Meta:
        model = products
        fields = ['id','active','available']

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerilizer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAdminOrReadOnly]
    filter_class = ProductFilter
    queryset = products.objects.all()
    

class NewsFilter(FilterSet):
    title = django_filters.CharFilter('title','icontains')
    description = django_filters.CharFilter('description','icontains')
    user = django_filters.CharFilter('user__username','iexact')
    
    class Meta:
        model = news
        fields = ['title','description','user']

class NewsViewSet(viewsets.ModelViewSet):
    queryset = news.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAdminOrReadOnly]
    filter_class = NewsFilter