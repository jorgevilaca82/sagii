from enum import IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _

from sagii.apps.base.models import PessoaFisica


class InscricaoCandidato(models.Model):
    class Status(IntEnum):
        DEFERIDA = auto()
        INDEFERIDA = auto()
        DEFERIDA_APOS_RECURSO = auto()

    CANDIDATO_STATUS_CHOICES = (
        (Status.DEFERIDA.value, _('Deferida')),
        (Status.INDEFERIDA.value, _('Indeferida')),
        (Status.DEFERIDA_APOS_RECURSO.value, _('Deferida após recurso')),
    )

    pessoa_fisica = models.ForeignKey(PessoaFisica, on_delete=models.PROTECT)
    status = models.IntegerField(choices=CANDIDATO_STATUS_CHOICES)
