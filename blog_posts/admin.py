from . import models
from django.contrib import admin

# display modesls for admin page
class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "simple_description"]

    class Meta:
        model = models.Post


# register models for show in admin page
admin.site.register(models.Post, PostAdmin)
