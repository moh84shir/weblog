from django.contrib import admin
from . import models


class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'post']


    class Meta:
        model = models.Comment

# Register Models
admin.site.register(models.Comment, CommentAdmin)
