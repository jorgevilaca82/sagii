from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'sagii_base'


urlpatterns = [
    path('', 
        views.HomeView.as_view(), 
        name='home'),
    
    path('pessoafisica/', 
        views.PessoaFisicaListView.as_view(), 
        name='pessoafisica-list'),
    
    path('pessoafisica/create',
        views.PessoaFisicaCreateView.as_view(),
        name='pessoafisica-create'),
    
    path('pessoafisica/<int:pk>/', 
        views.PessoaFisicaDetailView.as_view(), 
        name='pessoafisica-detail'),
    
    path('pessoafisica/<int:pk>/edit',
        views.PessoaFisicaUpdateView.as_view(),
        name='pessoafisica-update'),
    
    path('pessoafisica/<int:pk>/del',
        views.PessoaFisicaUpdateView.as_view(),
        name='pessoafisica-delete')
]