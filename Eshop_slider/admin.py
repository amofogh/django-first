from django.contrib import admin
from .models import slider
from Eshop_products.admin import make_active, make_deactive


# Register your models here.
class slider_admin(admin.ModelAdmin):
    list_display = ['title', 'link', 'active']
    list_editable = ['active']
    list_filter = ['active']
    actions = [make_active, make_deactive]


admin.site.register(slider, slider_admin)
