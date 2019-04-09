from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from localflavor.br import models as lf_models

from ..pessoa.models import Pessoa


class PessoaJuridica(Pessoa):
    class Meta:
        verbose_name = _('Pessoa Jurídica')
        verbose_name_plural = _('Pessoas Jurídicas')

    cnpj = lf_models.BRCNPJField(unique=True)

    # matriz = models.ForeignKey(
    #     'self',
    #     on_delete=models.PROTECT,
    #     related_name='filiais',
    #     null=True
    # )

    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,null=True)

    object_id = models.PositiveIntegerField(null=True)

    matriz = GenericForeignKey('content_type', 'object_id')

    filiais = GenericRelation('PessoaJuridica')


    @property
    def razao_social(self):
        return self.nome_razao_social

    @razao_social.setter
    def razao_social(self, value):
        self.nome_razao_social = value

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('sagii_base:pessoajuridica-detail', kwargs={'pk': self.pk})

    def __init__(self, *args, **kwargs):
        instance = super().__init__(*args, **kwargs)
        self._meta.get_field('nome_razao_social').verbose_name = _('Razão Social')
        return instance
