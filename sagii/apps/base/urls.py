from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'sagii_base'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('pessoafisica/', views.PessoaFisicaListView.as_view(), name='pessoafisica_list')
]