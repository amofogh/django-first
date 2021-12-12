from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import products
from django.http import Http404
from .utils import jalali_convertor


# Create your views here.

class Products_list(ListView):
    template_name = 'products/products.html'
    paginate_by = 6

    def get_queryset(self):
        return products.objects.get_active_products()


def product_detail(request, productId):
    product = products.objects.get_active_product(productId)
    if product is None:
        raise Http404

    # convert to persian calendar
    jalali = jalali_convertor(product)

    # slide show | show last 6 actives products
    last_products = products.objects.get_active_products()[:6]

    t = product.tag.all()
    print(t)

    context = {
        'products': product,
        'date': jalali,
        'first_products': last_products[0:3],
        'second_products': last_products[3:6],
    }
    return render(request, "products/product_detail.html", context)


# class Product_detail(DetailView):
#     template_name = 'products/product_detail.html'
#
#     def get_object(self, *args, **kwargs):
#         product_id = self.kwargs.get('productId')
#         product = products.objects.get_active_product(product_id)
#         if product is None:
#             raise Http404
#         return product
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(Product_detail, self).get_context_data(**kwargs)
#         # convert to persian calendar
#         jalali = jalali_convertor(context.get('object'))
#         context['date'] = jalali
#
#         # slide show
#         last_products = products.objects.get_active_products()[:6]
#         context['first_products'] = last_products[0:3]
#         context['second_products'] = last_products[3:6]
#
#         print(context)
#         print(products.tag_set.title)
#         return context


class Search_item(ListView):
    template_name = 'products/products.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query:
            return products.objects.search(query)
        return products.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super(Search_item, self).get_context_data(*args, **kwargs)
        return context
