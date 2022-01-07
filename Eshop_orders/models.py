from django.db import models
from django.contrib.auth.models import User
from Eshop_products.models import products
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class discount(models.Model):
    code = models.CharField(max_length=200, unique=True, verbose_name='کد تخفیف')
    worth = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
        verbose_name='درصد تخفیف')
    expire_date = models.DateTimeField(verbose_name='تاریخ انقضا')

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'

    def __str__(self):
        return self.code


class order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده/نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='زمان پرداخت')
    ref_id = models.CharField(max_length=100, verbose_name='کد پیگیری درگاه')
    discount = models.ForeignKey(discount, on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='کد تخفیف اعمال شده')

    def get_total_price(self):
        amount = 0
        ordered = self.order_detail_set.all()
        for product in ordered:
            amount += product.price * product.count
        if self.discount == None:
            return amount
        elif self.discount:
            user_discount = self.discount.worth
            return amount * (int(user_discount) / 100)

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

    def get_sum(self):
        return self.count * self.product.price

    class Meta:
        verbose_name = 'جزِئیات محصول'
        verbose_name_plural = 'جزئیات محصولات'

    def __str__(self):
        return self.product.title
