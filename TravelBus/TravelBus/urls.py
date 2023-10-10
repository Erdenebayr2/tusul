from django.contrib import admin
from django.urls import path
from BusApp import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
]
