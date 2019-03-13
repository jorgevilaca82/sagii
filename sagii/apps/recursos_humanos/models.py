from django.db import models

from sagii.apps.base import models as bm # (bm) base models
from sagii.apps.administracao import models as adm # (adm) administracao models
from enum import IntEnum, auto
from django.utils.translation import gettext_lazy as _

class Funcionario(bm.PessoaFisica):
    
    class Meta:
        pass
    
    class Tipo(IntEnum):
        CLT_PERMANENTE = auto()
        CLT_TEMPORARIO = auto()
        PRESTADOR_SERVICO = auto()
        SERVIDOR_PUBLICO = auto()
        ESTAGIARIO = auto()
        TRAINEE = auto()
        MENOR_APRENDIZ = auto()

    FUNCIONARIO_TIPO_CHOICES = (
        (Tipo.CLT_PERMANENTE.value, _('CLT Permanente')),
        (Tipo.CLT_TEMPORARIO.value, _('CLT Temporário')),
        (Tipo.PRESTADOR_SERVICO.value, _('Prestador de Serviço')),
        (Tipo.SERVIDOR_PUBLICO.value, _('Servidor Público')),
        (Tipo.ESTAGIARIO.value, _('Estagiário')),
        (Tipo.TRAINEE.value, _('Trainee')),
        (Tipo.MENOR_APRENDIZ.value, _('Menor Aprendiz')),
    )
    
    tipo = models.IntegerField(choices=FUNCIONARIO_TIPO_CHOICES)

    matricula = models.CharField(max_length=25)

    empregador = models.ForeignKey(bm.PessoaJuridica, on_delete=models.PROTECT)

    setor_lotacao = models.ForeignKey(adm.Setor, on_delete=models.PROTECT)