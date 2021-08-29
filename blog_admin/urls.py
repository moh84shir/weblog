from django.urls import path

from . import views

urlpatterns = [
    path('myadmin/', views.admin_main_page),
    path('myadmin/delete-post/<pk>/', views.delete_post),
    path('myadmin/create-post/', views.create_post),
    path('myadmin/edit-post/<pk>/', views.edit_post),
    path('myadmin/edit-settings/', views.edit_settings),
    path('myadmin/user-login/', views.user_login),
    path('myadmin/user-logout/', views.user_logout),
    path('myadmin/user-register/', views.user_register),
    path('myadmin/user-profile/', views.user_profile),
    path('myadmin/edit-user-profile/', views.edit_user_profile),
    path('myadmin/all-users/', views.all_users),
    path('myadmin/delete-user/<pk>', views.delete_user),
    path('myadmin/edit-user/<pk>', views.edit_user),
    path('admin_header', views.admin_header, name='admin_header'),
    path('admin_menubar', views.admin_menubar, name='admin_menubar'),
]