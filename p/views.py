from django.shortcuts import render

from Eshop_category.models import Category
from Eshop_products.models import products
from Eshop_products.utils import grouper
from Eshop_slider.models import slider
from Eshop_setting.models import site_setting

def header(request):
    setting = site_setting.objects.first()
    context = {
        'setting': setting,
    }
    return render(request, 'shared/_header.html', context)


def header_references(request, title, *args, **kwargs):
    context = {
        'title': title,
    }
    return render(request, 'shared/_headerReferences.html', context)


def home_page(request):
    sliders = slider.objects.filter(active=True)
    most_visit: products = products.objects.order_by('-visit_count').filter(active=True).all()[:8]
    latest_products = products.objects.order_by('-id').filter(active=True).all()[:8]
    last_categories = Category.objects.order_by('-id').filter(active=True).all()[:5]

    context = {
        'sliders': sliders,
        'range': range(0, sliders.count()),
        'most_visit': grouper(4, most_visit),
        'latest_products': grouper(4, latest_products),
        'categories': last_categories,
    }
    return render(request, 'home_page.html', context)


def footer(request):
    setting = site_setting.objects.first()
    context = {
        'title': 't',
        'setting': setting
    }
    return render(request, 'shared/_footer.html', context)

