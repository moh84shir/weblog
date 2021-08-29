from django.db import models

# Models

class Setting(models.Model):
    title = models.CharField(max_length=120)
    simple_description = models.CharField(max_length=120)
    copyright_text = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.title
