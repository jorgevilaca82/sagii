from enum import IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _

from sagii.commons.validators import PhoneRegexValidator
from .pessoa import PessoaRelatedModel


class Telefone(PessoaRelatedModel):
    class Meta:
        unique_together = ('numero', 'pessoa')

    class Tipo(IntEnum):
        FIXO = auto()
        CEL = auto()

    TELEFONE_TIPO_CHOICES = (
        (Tipo.FIXO.value, _('Tel. Fixo')),
        (Tipo.CEL.value, _('Tel. Celular')),
    )

    tipo = models.IntegerField(choices=TELEFONE_TIPO_CHOICES)

    numero = models.CharField(max_length=120, validators=[PhoneRegexValidator()])

    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.numero
