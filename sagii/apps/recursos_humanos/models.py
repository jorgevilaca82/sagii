from enum import IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _

from sagii.apps.administracao import models as adm  # (adm) administracao models
from sagii.apps.base import models as bm  # (bm) base models


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

    class ServidorManager(models.Manager):
        def get_queryset(self):
            return (super().get_queryset()
                    .filter(tipo=Funcionario.Tipo.SERVIDOR_PUBLICO))

    servidores = ServidorManager()

    class FuncionariosQuerySet(models.QuerySet):
        def clt_permanentes(self):
            return self.filter(tipo=Funcionario.Tipo.CLT_PERMANENTE)

        def clt_temporarios(self):
            return self.filter(tipo=Funcionario.Tipo.CLT_TEMPORARIO)

        def prestadores_de_servico(self):
            return self.filter(tipo=Funcionario.Tipo.PRESTADOR_SERVICO)

        def servidores_publicos(self):
            return self.filter(tipo=Funcionario.Tipo.SERVIDOR_PUBLICO)

        def estagiarios(self):
            return self.filter(tipo=Funcionario.Tipo.ESTAGIARIO)

        def trainees(self):
            return self.filter(tipo=Funcionario.Tipo.TRAINEE)

        def menores_aprendiz(self):
            return self.filter(tipo=Funcionario.Tipo.MENOR_APRENDIZ)

    funcionarios = FuncionariosQuerySet.as_manager()

    @classmethod
    def get_display_of_tipo(cls, tipo):
        return dict(cls.FUNCIONARIO_TIPO_CHOICES).get(tipo)
