from django.shortcuts import render, Http404
from django.views.generic import ListView

from .models import news
from Eshop_products.utils import jalali_convertor


# Create your views here.

def blog_detail(request, news_id):
    try:
        news_info = news.objects.get(id=news_id)
    except news.DoesNotExist:
        raise Http404('خبری که دنباش میگردی رو پیدا نکردم')

    date = news_info.convert_jalali_date()
    context = {
        'news': news_info,
    }
    return render(request, 'news/blog_detail.html', context)


class blog_list(ListView):
    template_name = 'news/blog_list.html'
    paginate_by = 6

    def get_queryset(self):
        return news.objects.order_by('-id').all()
