from django.urls import path
from .views import about_me


urlpatterns = [
    path("about_me", about_me)
]