from django.db import models
from django.db.models.signals import pre_save, post_save

from Eshop_tag.utils import unique_slug_generator


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(max_length=150, verbose_name='عنوان در url')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/category/{self.slug}'


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Category)
