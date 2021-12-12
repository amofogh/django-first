from django.contrib import admin
from .models import Tag


# Register your models here.
class Tag_admin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'timestamp', 'active']

    class Meta:
        model = Tag


admin.site.register(Tag, Tag_admin)
