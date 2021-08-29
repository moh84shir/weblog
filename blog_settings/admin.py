from blog_settings.models import Setting
from django.contrib import admin

# display models view for admin site
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'simple_description', 'copyright_text']

    class Meta:
        model = Setting


# register models for admin page
admin.site.register(Setting, SettingsAdmin)