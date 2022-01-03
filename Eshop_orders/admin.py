from django.contrib import admin

# Register your models here.
from Eshop_orders.models import order_detail, order


class order_detail_admin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'count']
    readonly_fields = ['__str__', 'order', 'count']

    class Meta:
        model = order_detail

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class order_admin(admin.ModelAdmin):
    list_display = ['owner', 'ref_id', 'payment_date', 'is_paid']
    readonly_fields = ['__str__', 'ref_id', 'owner', 'is_paid', 'payment_date']
    list_filter = ['is_paid']
    search_fields = ['ref_id']

    class Meta:
        model = order

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(order, order_admin)
admin.site.register(order_detail, order_detail_admin)
