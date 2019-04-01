from django.urls import path
from .. import views

urlpatterns = [
    # Pessoa Jurídica URLs
    path('pessoajuridica/', 
        views.pessoajuridica.ListView.as_view(), 
        name='pessoajuridica-list'),
    
    path('pessoajuridica/create',
        views.pessoajuridica.CreateView.as_view(),
        name='pessoajuridica-create'),
    
    path('pessoajuridica/<int:pk>/', 
        views.pessoajuridica.DetailView.as_view(), 
        name='pessoajuridica-detail'),
    
    path('pessoajuridica/<int:pk>/edit',
        views.pessoajuridica.UpdateView.as_view(),
        name='pessoajuridica-update'),
    
    path('pessoajuridica/<int:pk>/del',
        views.pessoajuridica.DeleteView.as_view(),
        name='pessoajuridica-delete'),   
]