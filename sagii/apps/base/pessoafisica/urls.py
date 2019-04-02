from django.urls import path

from . import views

urlpatterns = [
    # Pessoa Física URLs
    path('',
         views.ListView.as_view(),
         name='pessoafisica-list'),

    path('create',
         views.CreateView.as_view(),
         name='pessoafisica-create'),

    path('<int:pk>/',
         views.DetailView.as_view(),
         name='pessoafisica-detail'),

    path('<int:pk>/edit',
         views.UpdateView.as_view(),
         name='pessoafisica-update'),

    path('<int:pk>/del',
         views.DeleteView.as_view(),
         name='pessoafisica-delete'),
]
