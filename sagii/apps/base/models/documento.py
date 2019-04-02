from django.db import models
from django.utils.translation import gettext_lazy as _

from .pessoa import PessoaRelatedModel

class DocumentoPessoalTipo(models.Model):

    class Meta:
        verbose_name = _('Documento Pessoal Tipo')
        verbose_name_plural = _('Documentos Pessoais Tipos')

    # RG CTPS CNH TITULO_ELEITOR PASSAPORTE RESERVISTA CERTIDAO_NASCIMENTO
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class DocumentoPessoal(PessoaRelatedModel):

    class Meta:
        unique_together = ('tipo', 'pessoa')
        verbose_name = _('Documento Pessoal')
        verbose_name_plural = _('Documentos Pessoais')

    tipo = models.ForeignKey(DocumentoPessoalTipo, on_delete=models.PROTECT)
    
    valor = models.CharField(max_length=60)
    
    observacoes = models.CharField(max_length=140, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.tipo, self.valor)
