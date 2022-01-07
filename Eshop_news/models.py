from django.db import models
from django.contrib.auth.models import User

from Eshop_products.models import get_filename


# Create your models here.
from Eshop_products.utils import jalali_convertor


def upload_image_path(instance, filename):
    name, ext = get_filename(filename)

    new_name = f'{instance.title}{ext}'
    return f'products/news/{new_name}'


class news(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=200, verbose_name='موضوع خبر')
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True, verbose_name='عکس خبر')
    date = models.DateTimeField(auto_now=True, verbose_name='زمان انتشار/ویرایش')
    description = models.TextField(verbose_name='خبر')

    def get_absolute_url(self):
        return f'blog-detail/{self.id}'

    def convert_jalali_date(self):
        return jalali_convertor(self)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = 'بخش اخبار'
