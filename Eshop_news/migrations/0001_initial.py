# Generated by Django 3.2.9 on 2022-01-06 10:58

import Eshop_news.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='موضوع خبر')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Eshop_news.models.upload_image_path, verbose_name='عکس خبر')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='زمان انتشار/ویرایش')),
                ('description', models.TextField(verbose_name='خبر')),
            ],
        ),
    ]
