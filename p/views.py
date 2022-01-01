from django.shortcuts import render
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
    context = {
        'sliders': sliders,
        'range': range(0, sliders.count()),
    }
    return render(request, 'home_page.html', context)


def footer(request):
    setting = site_setting.objects.first()
    context = {
        'title': 't',
        'setting': setting
    }
    return render(request, 'shared/_footer.html', context)
