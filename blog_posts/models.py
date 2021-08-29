from django.contrib.auth.models import User
from django.db import models


# Models
class Post(models.Model):
    """ models for post in weblog """
    title = models.CharField(max_length=40)
    simple_description = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def get_url(self):
        return f"/posts/{self.pk}"

    def __str__(self) -> str:
        return self.title
