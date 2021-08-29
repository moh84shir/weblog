from django.conf.urls.static import static
from django.urls import path, include
from blog import settings
from django.contrib import admin
from . import views

urlpatterns = [
    path('', include('blog_posts.urls')),
    path('', include('blog_admin.urls')),
    path('', include('about_me.urls')),
    path('header', views.header, name="header"),
    path('footer', views.footer, name="footer"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
