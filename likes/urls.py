from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from likes import views

urlpatterns = [
    path('likes/', views.index),

]