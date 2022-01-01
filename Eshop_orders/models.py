from django.db import models
from django.contrib.auth.models import User
from Eshop_products.models import products


# Create your models here.


class order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده/نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='زمان پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید ها'

    def __str__(self):
        return self.owner.get_username()


class order_detail(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(products, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت')
    count = models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'جزِئیات محصول'
        verbose_name_plural = 'جزئیات محصولات'

    def __str__(self):
        return self.product.title
