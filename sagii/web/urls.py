from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

patterns = [

    path('auth/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),

    path('base/', include('sagii.apps.base.urls')),

    path('rh/', include('sagii.apps.recursos_humanos.urls')),

    path('', RedirectView.as_view(pattern_name='sagii_base:home'), name='home'),
]

urlpatterns = (
    patterns +
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
