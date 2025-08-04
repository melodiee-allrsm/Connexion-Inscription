
from django.contrib import admin
from django.urls import path
from Site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('inscription/',views.inscription),
]
