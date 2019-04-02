from django.urls import path

from . import views

urlpatterns = [
    # Pessoa Jurídica URLs
    path('',
         views.ListView.as_view(),
         name='pessoajuridica-list'),

    path('create',
         views.CreateView.as_view(),
         name='pessoajuridica-create'),

    path('<int:pk>/',
         views.DetailView.as_view(),
         name='pessoajuridica-detail'),

    path('<int:pk>/edit',
         views.UpdateView.as_view(),
         name='pessoajuridica-update'),

    path('<int:pk>/del',
         views.DeleteView.as_view(),
         name='pessoajuridica-delete'),
]
