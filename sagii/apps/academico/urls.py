from django.urls import path, include
from django.views import generic

app_name = 'sagii_academico'

base_module = 'sagii.apps.academico'

home_view = generic.TemplateView.as_view(template_name='academico/home.html')

urlpatterns = [
    path('', home_view, name='home'),
    path('aluno/', home_view, name='aluno-list'),
    path('professor/', home_view, name='professor-list'),
]
