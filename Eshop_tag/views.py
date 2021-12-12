from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Tag
from Eshop_products.models import products
from django.http import Http404


# Create your views here.


class tag_list(ListView):
    template_name = 'products/products.html'
    paginate_by = 6

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        qs = get_object_or_404(Tag, slug=slug, active=True)
        product = products.objects.filter(tag=qs.id, active=True)
        if product is None:
            raise Http404
        return product
