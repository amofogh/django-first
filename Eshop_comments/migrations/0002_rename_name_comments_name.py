# Generated by Django 3.2.9 on 2022-01-05 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='Name',
            new_name='name',
        ),
    ]
