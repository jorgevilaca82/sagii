from django.db import models

from sagii.commons.models import AuditableModel


class Pessoa(AuditableModel):
    class Meta:
        pass

    nome_razao_social = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_razao_social


class PessoaRelatedModel(AuditableModel):
    class Meta:
        abstract = True

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_related',
        related_query_name='%(app_label)s_%(class)ss',
    )
