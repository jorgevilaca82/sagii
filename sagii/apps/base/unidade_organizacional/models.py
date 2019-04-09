from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from sagii.commons.models import AuditableModel
from .. import models as bm


class UnidadeOrganizacional(AuditableModel):

    sigla = models.CharField(max_length=20)

    nome = models.CharField(max_length=140)

    # TODO: futuro implementar o campo e nas urls
    # slug = models.SlugField()

    # opcional no caso de subsetores
    pessoa_juridica = models.ForeignKey(bm.PessoaJuridica)

    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,null=True)

    object_id = models.PositiveIntegerField(null=True)

    uo_superior = GenericForeignKey('content_type', 'object_id')

    sub_uos = GenericRelation('UnidadeOrganizacional')