from django.contrib import admin
from .models import products


# Register your models here.

class product_admin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'title', 'description', 'price', 'active']

    class Meta:
        model = products


admin.site.register(products, product_admin)
