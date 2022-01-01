from django.contrib import admin
from .models import products, products_gallery


# Register your models here.
@admin.action(description='تغییر به موجود')
def make_available(modeladmin, request, queryset):
    queryset.update(available=True)


@admin.action(description='تغییر به ناموجود')
def make_unavailable(modeladmin, request, queryset):
    queryset.update(available=False)


@admin.action(description='فعال کردن')
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description='غیرفعال کردن')
def make_deactive(modeladmin, request, queryset):
    queryset.update(active=False)


class product_admin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'title', 'description', 'price', 'available', 'active']
    search_fields = ['title', 'description', 'price']
    list_filter = ['tag', 'category', 'active']
    list_editable = ['active', 'available']
    actions = [make_available, make_unavailable, make_active, make_deactive]

    class Meta:
        model = products


class gallery_admin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'product']
    search_fields = ['product']

    class Meta:
        model = products


admin.site.register(products, product_admin)
admin.site.register(products_gallery, gallery_admin)
