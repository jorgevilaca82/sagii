from django.db import models
from sagii.apps.base.models import PessoaFisica
from enum import IntEnum, auto
from django.utils.translation import gettext_lazy as _

# import de models para inclusão nas migrations
from .processo_seletivo.models import * # no-qa 

class Aluno(models.Model):
    """
    A Pessoa Física só se torna um aluno quando está devidamente
    associada um curso. Uma Pessoa Física pode ser aluno de mais de um curso,
    mas nunca mais que dois e sem conflito de turnos
    """

    class Status(IntEnum):
        MATRICULADO = auto()
        EVADIDO = auto()

    ALUNO_STATUS_CHOICES = (
        (Status.MATRICULADO.value, _('Matriculado')),
        (Status.EVADIDO.value, _('Evadido')),
    )

    status = models.IntegerField(choices=ALUNO_STATUS_CHOICES)

    # RA - Registro de Aluno (identificador de matricula)
    ra = models.CharField(max_length=255)
    pessoa_fisica = models.ForeignKey(PessoaFisica, on_delete=models.PROTECT)
    