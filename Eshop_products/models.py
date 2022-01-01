from django.db import models
from os import path
from django.db.models import Q
from Eshop_tag.models import Tag
from Eshop_category.models import Category


# Create your models here.

def get_filename(filepath):
    basename = path.basename(filepath)
    name, ext = path.splitext(basename)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename(filename)

    new_name = f'{instance.title}{ext}'
    return f'products/{new_name}'


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename(filename)

    new_name = f'{instance.title}{ext}'
    return f'products/gallery/{instance.title}/{new_name}'


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

    def get_related_products(self, product):
        lookup = (
                Q(tag__products=product) |
                Q(category__products=product)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    available = models.BooleanField(default=False, verbose_name='موجودیت')
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


class products_gallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر محصول')
    product = models.ForeignKey(products, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'گالری تصاویر'

    def __str__(self):
        return self.title
