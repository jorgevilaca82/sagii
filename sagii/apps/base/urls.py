from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'sagii.apps.base'
urlpatterns = [
    path('', views.index, name='index'),
]