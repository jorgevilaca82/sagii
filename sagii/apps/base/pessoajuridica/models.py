from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br import models as lf_models

from ..models.pessoa import Pessoa

class PessoaJuridica(Pessoa):

    class Meta:
        verbose_name = _('Pessoa Jurídica')
        verbose_name_plural = _('Pessoas Jurídicas')

    cnpj = lf_models.BRCNPJField(unique=True)

    matriz = models.ForeignKey(
        'self', 
        on_delete=models.PROTECT, 
        related_name='filiais', 
        null=True
    )

    @property
    def razao_social(self):
        return self.nome_razao_social

    @razao_social.setter
    def razao_social(self, value):
        self.nome_razao_social = value

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('sagii_base:pessoajuridica-detail', kwargs={'pk': self.pk})


