from django.db import models
from django.contrib.auth.models import User

from Eshop_products.models import products


# Create your models here.
class comments_manager(models.Manager):
    def get_all_comments(self, product_id):
        return self.get_queryset().filter(product_id=product_id).all()


class comments(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام و نام خوانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    text = models.TextField(verbose_name='نظر')
    product = models.ForeignKey(products, on_delete=models.CASCADE, verbose_name='محصول')
    time = models.DateTimeField(auto_now=True)

    objects = comments_manager()

    class Meta:
        verbose_name = "نظر کاربر"
        verbose_name_plural = 'نظرات کاربران'

    def __str__(self):
        return self.name
