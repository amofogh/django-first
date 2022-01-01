from django.db import models
from Eshop_products.models import get_filename


# Create your models here.
def upload_image_path(instance, filename):
    name, ext = get_filename(filename)

    new_name = f'logo-{instance.site_title}{ext}'
    return f'site_setting/{new_name}'


class site_setting(models.Model):
    site_title = models.CharField(max_length=150, verbose_name='نام سایت')
    logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='لوگو سایت')
    logo2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='لوگو سایت 2')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='آدرس')
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='شماره تلفن')
    fax = models.CharField(max_length=50, null=True, blank=True, verbose_name='فکس')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ما')
    copyright = models.CharField(max_length=500, verbose_name='متن کپی رایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__(self):
        return self.site_title
