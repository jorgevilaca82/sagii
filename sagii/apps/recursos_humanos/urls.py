from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'sagii_rh'

urlpatterns = [
    path('', TemplateView.as_view(template_name='recursos_humanos/home.html'), name='home'),
    path('servidor/', views.ServidorPublicoListView.as_view(), name='servidor_list')
]
