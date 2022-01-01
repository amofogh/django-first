from django.contrib import admin
from .models import Category
from Eshop_products.admin import make_active, make_deactive


# Register your models here.

class Category_admin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'slug', 'active']
    search_fields = ['title']
    list_editable = ['active']
    list_filter = ['active']

    actions = [make_active, make_deactive]

    class Meta:
        model = Category


admin.site.register(Category, Category_admin)
