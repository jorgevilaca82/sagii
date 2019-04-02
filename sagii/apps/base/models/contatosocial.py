from enum import auto
from django.db import models
from django.utils.translation import gettext_lazy as _
from sagii.commons import AutoNameEnum, ChoiceEnumCharValueMeta

from .pessoa import PessoaRelatedModel

class ContatoSocial(PessoaRelatedModel):

    class Meta:
        verbose_name = _('Contato Social')
        verbose_name_plural = _('Contatos Sociais')
        unique_together = ('pessoa', 'tipo')

    class Tipo(AutoNameEnum, metaclass=ChoiceEnumCharValueMeta):
        WHATSAPP = auto()
        TELEGRAM = auto()
        FACEBOOK = auto()
        INSTAGRAM = auto()
        TWITTER = auto()
        WEBSITE = auto()
        EMAIL = auto()
        SKYPE = auto()
        LINKEDIN = auto()

    tipo = models.CharField(max_length=60, choices=Tipo)
    
    valor = models.CharField(max_length=60)

    def __str__(self):
        return '{}: {}'.format(self.tipo.value.title(), self.valor)

