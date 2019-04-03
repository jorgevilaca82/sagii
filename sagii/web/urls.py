from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
class SagiiAuthenticationForm(AuthenticationForm):
    from django.utils.translation import gettext, gettext_lazy as _
    from django.contrib.auth.forms import UsernameField
    from django import forms
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': _('Username')
        }))

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _("Password")
        }),
    )

patterns = [

    path('auth/login/', LoginView.as_view(authentication_form=SagiiAuthenticationForm), name='login'),

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
