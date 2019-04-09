from enum import IntEnum, auto
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from sagii.apps.base import models as bm


class UnidadeDeEnsino(bm.PessoaJuridica):

    class Tipo(IntEnum):
        INSTITUTO = auto()
        CAMPUS = auto()
        POLO = auto()

    TIPO_CHOICES = (
        (Tipo.INSTITUTO.value, _('Instituto')),
        (Tipo.CAMPUS.value, _('Campus')),
        (Tipo.POLO.value, _('Polo')),
    )

    tipo = models.IntegerField(choices=TIPO_CHOICES)

    sub_unidades = GenericRelation('UnidadeDeEnsino')

    class PorTipoQuerySet(models.QuerySet):

        def institutos(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.INSTITUTO)

        def campus(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.CAMPUS)

        def polo(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.POLO)

    por_tipo = PorTipoQuerySet.as_manager()