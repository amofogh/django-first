from django.contrib import admin
from .models import site_setting


# Register your models here.
class site_setting_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = site_setting.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(site_setting, site_setting_admin)
