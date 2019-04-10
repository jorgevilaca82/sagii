from enum import IntEnum, auto
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from sagii.commons.models import AuditableModel
from sagii.apps.base import models as bm


class UnidadeDeEnsino(bm.UnidadeOrganizacional):

    class Tipo(IntEnum):
        CAMPUS = auto()
        POLO = auto()
        ESCOLA = auto()

    TIPO_CHOICES = (
        (Tipo.CAMPUS.value, _('Campus')),
        (Tipo.POLO.value, _('Polo')),
        (Tipo.ESCOLA.value, _('Escola')),
    )

    tipo = models.IntegerField(choices=TIPO_CHOICES)

    sub_unidades = GenericRelation('UnidadeDeEnsino')

    class PorTipoQuerySet(models.QuerySet):

        def campus(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.CAMPUS)

        def polo(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.POLO)

        def escolas(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.ESCOLA)

    por_tipo = PorTipoQuerySet.as_manager()


class AreaUnidadeDeEnsino(AuditableModel):
    class Meta:
        pass

    class Tipo(IntEnum):
        DIRETORIA_DE_ENSINO = auto()
        COORDENACAO_DE_CURSO = auto()

    TIPO_CHOICES = (
        (Tipo.DIRETORIA_DE_ENSINO.value, _('Diretoria de Ensino')),
        (Tipo.COORDENACAO_DE_CURSO.value, _('Coordenação de Curso')),
    )

    tipo = models.IntegerField(choices=TIPO_CHOICES)

    unidade_de_ensino = models.ForeignKey(UnidadeDeEnsino, on_delete=models.PROTECT)

    area_superior = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='sub_areas',
        null=True
    )

    responsavel = models.ForeignKey(bm.PessoaFisica, on_delete=models.PROTECT)

    class PorTipoQuerySet(models.QuerySet):

        def diretorias_de_ensino(self):
            return self.filter(tipo=AreaUnidadeDeEnsino.Tipo.DIRETORIA_DE_ENSINO)

        def coordenacao_de_curso(self):
            return self.filter(tipo=AreaUnidadeDeEnsino.Tipo.COORDENACAO_DE_CURSO)

    por_tipo = PorTipoQuerySet.as_manager()