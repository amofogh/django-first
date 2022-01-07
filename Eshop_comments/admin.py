from django.contrib import admin

# Register your models here.
from Eshop_comments.models import comments


class comments_admin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'product', 'time']
    search_fields = ['name', 'email', 'text']
    list_filter = ['time']

    class Meta:
        model = comments


admin.site.register(comments, comments_admin)
