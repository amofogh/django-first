from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from Eshop_comments.forms import comment_form
from Eshop_comments.models import comments
from Eshop_orders.forms import order_form
from .models import products, products_gallery
from django.http import Http404
from .utils import jalali_convertor, grouper


# Create your views here.


class Products_list(ListView):
    template_name = 'products/products.html'
    paginate_by = 6

    def get_queryset(self):
        return products.objects.get_active_products()

    def get_context_data(self, *args, **kwargs):
        context = super(Products_list, self).get_context_data(*args, **kwargs)
        return context


class last_Products_list(ListView):
    template_name = 'products/products.html'
    paginate_by = 6

    def get_queryset(self):
        return products.objects.get_active_products().order_by('-id')

    def get_context_data(self, *args, **kwargs):
        context = super(last_Products_list, self).get_context_data(*args, **kwargs)
        return context


class most_visited_Products_list(ListView):
    template_name = 'products/products.html'
    paginate_by = 6

    def get_queryset(self):
        return products.objects.get_active_products().order_by('-visit_count')

    def get_context_data(self, *args, **kwargs):
        context = super(most_visited_Products_list, self).get_context_data(*args, **kwargs)
        return context


def product_detail(request, productId):
    product = products.objects.get_active_product(productId)
    orderForm = order_form(request.POST or None, initial={'product_id': productId})
    user_id = request.user.id
    user = User.objects.filter(id=user_id).first()
    commentForm = comment_form(request.POST or None,
                               initial={'product_id': productId, 'name': user.get_full_name(), 'email': user.email})

    if product is None:
        raise Http404
    product.visit_count += 1
    product.save()

    # galleries
    galleries = products_gallery.objects.filter(product_id=productId)
    galleries = list(grouper(3, galleries))

    # convert to persian calendar
    jalali = jalali_convertor(product)

    related_products = products.objects.get_related_products(product)

    all_comments = comments.objects.get_all_comments(productId)

    context = {
        'products': product,
        'date': jalali,
        'suggest_products': list(grouper(3, related_products)),
        'galleries': galleries,
        'order_form': orderForm,
        'comment_form': commentForm,
        'comments': all_comments,
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
