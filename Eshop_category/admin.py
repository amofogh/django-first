from django.contrib import admin
from .models import Category


# Register your models here.

class Category_admin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'slug', 'active']

    class Meta:
        model = Category


admin.site.register(Category, Category_admin)
