from django.db import models

from sagii.apps.base import models as bm


class SetorTipo(models.Model):
    class Meta:
        pass

    nome = models.CharField(max_length=255)


class Setor(models.Model):
    class Meta:
        pass

    nome = models.CharField(max_length=255)

    pj = models.ForeignKey(bm.PessoaJuridica, on_delete=models.PROTECT)

    setor_pai = models.ForeignKey('self',
                                  on_delete=models.PROTECT, related_name='sub_setores', null=True)

    tipo = models.ForeignKey(SetorTipo, on_delete=models.PROTECT)
