from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from mainpart import views

urlpatterns = [
    path('', views.index),
    path('', include("django.contrib.auth.urls")),
    path('', include("posts.urls")),
    path('', include("likes.urls")),
    path('register/', views.register),
    path('admin/', admin.site.urls),
    path('user/', views.index),
    path('user/<str:username>', views.user),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
