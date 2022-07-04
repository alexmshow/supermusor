from django.urls import path

from posts import views


urlpatterns = [
    path('create/', views.create),
    path('lazy_load_posts/', views.lazy_load_posts)
]
