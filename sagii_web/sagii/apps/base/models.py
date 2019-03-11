from django.db import models
from enum import IntEnum, Enum, auto
from django.utils.translation import gettext_lazy as _
from sagii.commons import ChoiceEnumCharValueMeta, AutoNameEnum
from localflavor.br import br_states, models as lf_models 
# https://django-localflavor.readthedocs.io/en/latest/localflavor/br/

class Pessoa(models.Model):
    nome_razao_social = models.CharField(max_length=255)

    # ** Sets **
    # contatos_sociais
    # enderecos
    # documentos

    def __str__(self):
        return self.nome_razao_social


class PessoaFisica(Pessoa):

    class Meta:
        verbose_name = _('Pessoa Física')
        verbose_name_plural = _('Pessoas Físicas')
    
    class Genero(Enum):
        MASCULINO = 'M'
        FEMININO = 'F'
    
    SEXO_CHOICES = (
        (Genero.MASCULINO.value, _('Masculino')),
        (Genero.FEMININO.value, _('Feminino')),
    )

    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    class EstadoCivil(IntEnum):
        SOLTEIRO = auto()
        CASADO = auto()
        VIUVO = auto()
        DIVORCIADO = auto()
        UNIAO_ESTAVEL = auto()

    ESTADO_CIVIL_CHOICES = (
        (EstadoCivil.SOLTEIRO.value, _('Solteiro')),
        (EstadoCivil.CASADO.value, _('Casado')),
        (EstadoCivil.VIUVO.value, _('Viúvo')),
        (EstadoCivil.DIVORCIADO.value, _('Divorciado')),
    )

    estado_civil = models.IntegerField(choices=ESTADO_CIVIL_CHOICES)

    class TipoSanguineo(Enum, metaclass=ChoiceEnumCharValueMeta):
        AP = 'A+'
        AN = 'A-'
        BP = 'B+'
        BN = 'B-'
        ABP = 'AB+'
        ABN = 'AB-'
        OP = 'O+'
        ON = 'O-'
    
    tipo_sanguineo = models.CharField(max_length=3, choices=TipoSanguineo)

    natural_cidade = models.CharField(max_length=120)

    natural_uf = lf_models.BRStateField()

    cpf = lf_models.BRCPFField()

    def __str__(self):
        return '{} ({})'.format(self.nome_razao_social, self.cpf)

    def __unicode__(self):
        return self.__str__()

    
class PessoaJuridica(Pessoa):
    cnpj = lf_models.BRCNPJField()


class Endereco(models.Model):

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')
        unique_together = ('pessoa', 'principal')

    class Tipo(IntEnum):
        COMERCIAL = 1
        RESIDENCIAL = 2
        RURAL = 3

    TIPOS_CHOICES = (
        (Tipo.COMERCIAL.value, _('Comercial')),
        (Tipo.RESIDENCIAL.value, _('Residencial')),
        (Tipo.RURAL.value, _('Rural')),
    )

    tipo = models.IntegerField(choices=TIPOS_CHOICES)
    cep = lf_models.BRPostalCodeField()
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=120)
    numero = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    uf = lf_models.BRStateField()

    
    # Define se é o endereço principal
    principal = models.BooleanField()

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='enderecos')


class ContatoSocial(models.Model):

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
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='contatos_sociais')

    def __str__(self):
        return '{}: {}'.format(self.tipo, self.valor)


class DocumentoPessoalTipo(models.Model):
    # RG CTPS CNH TITULO_ELEITOR PASSAPORTE RESERVISTA CERTIDAO_NASCIMENTO
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class DocumentoPessoal(models.Model):
    class Meta:
        unique_together = ('tipo', 'pessoa')

    tipo = models.ForeignKey(DocumentoPessoalTipo, on_delete=models.PROTECT)
    valor = models.CharField(max_length=60)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='documentos')
    observacoes = models.TextField()

    def __str__(self):
        return '{}: {}'.format(self.tipo, self.valor)