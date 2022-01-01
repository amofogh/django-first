from django.contrib import admin
from .models import Tag
from Eshop_products.admin import make_active, make_deactive


# Register your models here.
class Tag_admin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'timestamp', 'active']
    search_fields = ['title']
    list_editable = ['active']
    list_filter = ['active']

    actions = [make_active, make_deactive]

    class Meta:
        model = Tag


admin.site.register(Tag, Tag_admin)
