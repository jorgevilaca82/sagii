# from django.contrib import admin
from django.urls import path

from . import pessoafisica
from . import pessoajuridica

from .. import views

app_name = 'sagii_base'

urlpatterns = [
    path('', 
        views.HomeView.as_view(), 
        name='home'),
] \
    + pessoafisica.urlpatterns \
    + pessoajuridica.urlpatterns
