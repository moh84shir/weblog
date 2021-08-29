from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('posts/<pk>', views.post_detail),
    path('delete-comment/<pk>', views.delete_comment),
]
