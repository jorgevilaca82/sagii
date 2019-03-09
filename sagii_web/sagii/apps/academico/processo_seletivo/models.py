from django.db import models
from sagii.apps.base.models import PessoaFisica
from enum import IntEnum, auto
from django.utils.translation import gettext_lazy as _

class Candidato(models.Model):

    class Status(IntEnum):
        INSCRITO = auto()

    CANDIDATO_STATUS_CHOICES = (
        (Status.INSCRITO.value, _('Inscrito'))
    )

    pessoa_fisica = models.ForeignKey(PessoaFisica, on_delete=models.PROTECT)
    status = models.IntegerField(choices=CANDIDATO_STATUS_CHOICES)