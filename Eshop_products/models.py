from django.db import models
from os import path
from django.db.models import Q
from Eshop_tag.models import Tag
from Eshop_category.models import Category


def get_filename(filepath):
    basename = path.basename(filepath)
    name, ext = path.splitext(basename)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename(filename)

    new_name = f'{instance.title}{ext}'
    return f'products/{new_name}'


# Create your models here.
class Products_manager(models.Manager):

    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_active_product(self, product_id):
        qs = self.get_queryset().filter(id=product_id, active=True)
        if qs:
            return qs.first()
        return None

    def search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(tag__title__icontains=query))

        return self.get_queryset().filter(lookup, active=True).distinct()


class products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    available = models.BooleanField(default=False, verbose_name='موجودیت')
    brand = models.CharField(max_length=40, blank=True, null=True, verbose_name='برند')
    date = models.DateTimeField(verbose_name='تاریخ', auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category, blank=True)

    objects = Products_manager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products/{self.id}'
