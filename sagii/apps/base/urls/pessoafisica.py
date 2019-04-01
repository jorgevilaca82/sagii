from django.urls import path
from .. import views

urlpatterns = [
    # Pessoa Física URLs
    path('pessoafisica/', 
        views.pessoafisica.ListView.as_view(), 
        name='pessoafisica-list'),
    
    path('pessoafisica/create',
        views.pessoafisica.CreateView.as_view(),
        name='pessoafisica-create'),
    
    path('pessoafisica/<int:pk>/', 
        views.pessoafisica.DetailView.as_view(), 
        name='pessoafisica-detail'),
    
    path('pessoafisica/<int:pk>/edit',
        views.pessoafisica.UpdateView.as_view(),
        name='pessoafisica-update'),
    
    path('pessoafisica/<int:pk>/del',
        views.pessoafisica.DeleteView.as_view(),
        name='pessoafisica-delete'),
]