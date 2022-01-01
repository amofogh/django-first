from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category
from Eshop_products.models import products
from django.shortcuts import Http404


# Create your views here.

class CategoryView(ListView):
    template_name = 'products/products.html'
    paginate_by = 6

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        # qs = Category.objects.filter(slug=slug, active=True)
        qs = get_object_or_404(Category, slug=slug, active=True)
        # product = products.objects.filter(category=qs.id)
        product = products.objects.filter(category__slug=qs.slug)
        if product is None:
            raise Http404
        return product

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        return context


def categories_partial(request, *args, **kwargs):
    qs = Category.objects.filter(active=True)
    context = {
        'categories': qs
    }
    return render(request, 'categories/categories_render_partial.html', context)
