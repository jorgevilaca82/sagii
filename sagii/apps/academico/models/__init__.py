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


class DiretoriaEnsino(AuditableModel):
    class Meta:
        pass

    diretor = models.ForeignKey(bm.PessoaFisica, on_delete=models.PROTECT)