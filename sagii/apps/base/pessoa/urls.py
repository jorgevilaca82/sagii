from django.urls import path, include

from . import views

# base_module = 'sagii.apps.base'

urlpatterns = [

    path('<int:pessoa_id>/', include([

        path('telefone/', include([

            path('',
                views.telefone.ListView.as_view(),
                name='pessoa-telefone-list'),

            path('create',
                views.telefone.CreateView.as_view(),
                name='pessoa-telefone-create'),

            path('<int:pk>/',
                views.telefone.DetailView.as_view(),
                name='pessoa-telefone-detail'),

            path('<int:pk>/edit',
                views.telefone.UpdateView.as_view(),
                name='pessoa-telefone-update'),

            path('<int:pk>/del',
                views.telefone.DeleteView.as_view(),
                name='pessoa-telefone-delete'),

        ])),


        path('contatosocial/', include([

            path('',
                views.contatosocial.ListView.as_view(),
                name='pessoa-contatosocial-list'),

            path('create',
                views.contatosocial.CreateView.as_view(),
                name='pessoa-contatosocial-create'),

            path('<int:pk>/',
                views.contatosocial.DetailView.as_view(),
                name='pessoa-contatosocial-detail'),

            path('<int:pk>/edit',
                views.contatosocial.UpdateView.as_view(),
                name='pessoa-contatosocial-update'),

            path('<int:pk>/del',
                views.contatosocial.DeleteView.as_view(),
                name='pessoa-contatosocial-delete'),

        ])),

        path('endereco/', include([

            path('',
                views.endereco.ListView.as_view(),
                name='pessoa-endereco-list'),

            path('create',
                views.endereco.CreateView.as_view(),
                name='pessoa-endereco-create'),

            path('<int:pk>/',
                views.endereco.DetailView.as_view(),
                name='pessoa-endereco-detail'),

            path('<int:pk>/edit',
                views.endereco.UpdateView.as_view(),
                name='pessoa-endereco-update'),

            path('<int:pk>/del',
                views.endereco.DeleteView.as_view(),
                name='pessoa-endereco-delete'),

        ])),

        path('documento/', include([

            path('',
                views.documento.ListView.as_view(),
                name='pessoa-documento-list'),

            path('create',
                views.documento.CreateView.as_view(),
                name='pessoa-documento-create'),

            path('<int:pk>/',
                views.documento.DetailView.as_view(),
                name='pessoa-documento-detail'),

            path('<int:pk>/edit',
                views.documento.UpdateView.as_view(),
                name='pessoa-documento-update'),

            path('<int:pk>/del',
                views.documento.DeleteView.as_view(),
                name='pessoa-documento-delete'),

        ])),

    ])),

]
