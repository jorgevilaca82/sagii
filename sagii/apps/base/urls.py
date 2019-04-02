from django.urls import path, include

from . import views
from .pessoa import urls as pessoa_urls
from .pessoafisica import urls as pessoafisica_urls
from .pessoajuridica import urls as pessoajuridica_urls

app_name = 'sagii_base'

base_module = 'sagii.apps.base'

urlpatterns = [
    path('',
         views.HomeView.as_view(),
         name='home'),

    path('pessoafisica/', include(pessoafisica_urls)),
    path('pessoajuridica/', include(pessoajuridica_urls)),
    path('pessoa/', include(pessoa_urls)),
]
