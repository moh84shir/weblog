from django.db import models


class AboutMe(models.Model):
    about = models.TextField()

    def __str__(self) -> str:
        return "درباره ی من"
