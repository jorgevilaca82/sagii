from enum import IntEnum

from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br import models as lf_models

from .pessoa import PessoaRelatedModel


class Endereco(PessoaRelatedModel):
    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')
        # unique_together = ('pessoa', 'principal')

    class Tipo(IntEnum):
        COMERCIAL = 1
        RESIDENCIAL = 2
        RURAL = 3

    TIPOS_CHOICES = (
        (Tipo.COMERCIAL.value, _('Comercial')),
        (Tipo.RESIDENCIAL.value, _('Residencial')),
        (Tipo.RURAL.value, _('Rural')),
    )

    tipo = models.IntegerField(choices=TIPOS_CHOICES)

    cep = lf_models.BRPostalCodeField()

    logradouro = models.CharField(max_length=255)

    complemento = models.CharField(max_length=255, blank=True, null=True)

    bairro = models.CharField(max_length=120)

    numero = models.CharField(max_length=120)

    cidade = models.CharField(max_length=120)

    uf = lf_models.BRStateField()

    # Define se é o endereço principal
    principal = models.BooleanField(default=False)

    def get_absolute_url(self):
        from django.urls import reverse
        kwargs = {'pessoa_id': self.pessoa_id, 'pk': self.pk}
        return reverse('sagii_base:pessoa-endereco-detail', kwargs=kwargs)