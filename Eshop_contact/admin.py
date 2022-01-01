from django.contrib import admin
from .models import contact_us


# Register your models here.
@admin.action(description='تغییر به خوانده شده')
def make_read(modeladmin, request, queryset):
    queryset.update(is_read=True)


class contact_us_admin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'is_read']
    list_editable = ['is_read']
    search_fields = ['subject', 'text']
    list_filter = ['is_read']
    actions = [make_read]
    readonly_fields = ['full_name', 'email', 'subject', 'text']

    class Meta:
        model = contact_us


admin.site.register(contact_us, contact_us_admin)
