from django.db import models
from os import path


def get_filename(filepath):
    basename = path.basename(filepath)
    name, ext = path.splitext(basename)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename(filename)

    new_name = f'{instance.title}{ext}'
    return f'products/{new_name}'


class slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    link = models.URLField(verbose_name='لینک')
    image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر')
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'اسلایدرها'
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self.title
