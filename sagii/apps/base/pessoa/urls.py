from django.urls import path, include
from . import views

urlpatterns = [

    path('<int:pessoa_id>/telefone/', include([
        path('', 
            views.telefone.ListView.as_view(), 
            name='pessoa-telefone-list'),
        
        # path('create',
        #     views.CreateView.as_view(),
        #     name='pessoa-telefone-create'),
        
        # path('<int:pk>/', 
        #     views.DetailView.as_view(), 
        #     name='pessoa-telefone-detail'),
        
        # path('<int:pk>/edit',
        #     views.UpdateView.as_view(),
        #     name='pessoa-telefone-update'),
        
        # path('<int:pk>/del',
        #     views.DeleteView.as_view(),
        #     name='pessoa-telefone-delete'),
    ])),
    
]