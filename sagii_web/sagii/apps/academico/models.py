from django.db import models
from sagii.apps.base import models as bm # (bm) base models
from sagii.apps.recursos_humanos import models as rhm
from enum import IntEnum, auto
from django.utils.translation import gettext_lazy as _
from sagii.apps.base import models as bm
from sagii.apps.administracao import models as adm
from sagii.apps.recursos_humanos import models as rhm

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
    pessoa_fisica = models.ForeignKey(bm.PessoaFisica, on_delete=models.PROTECT)
    

class Professor(rhm.Funcionario):
    
    class Meta:
        pass
    
    class Titulacao(IntEnum):
        GRADUACAO = auto()
        ESPECIALIZACAO = auto()
        MESTRADO = auto()
        DOUTORADO = auto()
        POS_DOUTORADO = auto()
    
    PROFESSOR_TITULACAO_CHOICES = (
        (Titulacao.GRADUACAO.value, _('Gradução')),
        (Titulacao.ESPECIALIZACAO.value, _('Especialização')),
        (Titulacao.MESTRADO.value, _('Mestrador')),
        (Titulacao.DOUTORADO.value, _('Doutorado')),
        (Titulacao.POS_DOUTORADO.value, _('Pós Doutorado')),
    )
    
    titulacao = models.IntegerField(choices=PROFESSOR_TITULACAO_CHOICES)


class Campus(bm.PessoaJuridica):
    pass


class DiretoriaEnsino(adm.Setor):
    
    class Meta:
        pass

    diretor = models.ForeignKey(rhm.Funcionario, on_delete=models.PROTECT)


class Curso(models.Model):
        
    class Meta:
        pass

    # Diretoria de Ensino (de)
    de = models.ForeignKey(DiretoriaEnsino, on_delete=models.PROTECT)