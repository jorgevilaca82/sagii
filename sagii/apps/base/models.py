from enum import Enum, IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br import br_states
from localflavor.br import models as lf_models

from sagii.commons import AutoNameEnum, ChoiceEnumCharValueMeta, PhoneRegexValidator

# https://django-localflavor.readthedocs.io/en/latest/localflavor/br/


class Pessoa(models.Model):

    class Meta:
        pass
    
    nome_razao_social = models.CharField(max_length=255)

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

    sexo = models.CharField(
        max_length=1, 
        choices=SEXO_CHOICES, 
        null=True, 
        blank=True
    )

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

    estado_civil = models.IntegerField(
        choices=ESTADO_CIVIL_CHOICES, 
        default=EstadoCivil.SOLTEIRO.value
    )

    class TipoSanguineo(Enum, metaclass=ChoiceEnumCharValueMeta):
        AP = 'A+'
        AN = 'A-'
        BP = 'B+'
        BN = 'B-'
        ABP = 'AB+'
        ABN = 'AB-'
        OP = 'O+'
        ON = 'O-'
    
    tipo_sanguineo = models.CharField(
        max_length=3, 
        choices=TipoSanguineo, 
        blank=True, 
        null=True
    )

    natural_cidade = models.CharField(max_length=120, blank=True, null=True)

    natural_uf = lf_models.BRStateField(blank=True, null=True)

    class NacionalidadeTipo(Enum, metaclass=ChoiceEnumCharValueMeta):
        BRASILEIRO = 'BR'
        ESTRANGEIRO = 'EST'

    NACIONALIDADE_TIPO_CHOICES = (
        (NacionalidadeTipo.BRASILEIRO.value, _('Brasileiro')),
        (NacionalidadeTipo.ESTRANGEIRO.value, _('Estrangeiro')),
    )

    nacionalidade = models.CharField(
        max_length=3,
        choices=NACIONALIDADE_TIPO_CHOICES,
        default=NacionalidadeTipo.BRASILEIRO.value,
        blank=True,
        null=True
    )

    falecido = models.BooleanField(default=False)

    cpf = lf_models.BRCPFField(unique=True)

    dependentes = models.ManyToManyField(
        'self',
        through='RelacaoDependencia',
        through_fields=('responsavel', 'dependente'),
        symmetrical=False
    )

    @property
    def nome(self):
        return self.nome_razao_social

    def __str__(self):
        return '{} ({})'.format(self.nome, self.cpf)

    def __unicode__(self):
        return self.__str__()


class RelacaoDependencia(models.Model):

    responsavel = models.ForeignKey(
        PessoaFisica,
        on_delete=models.PROTECT,
        related_name='_deps'
    )

    dependente = models.ForeignKey(
        PessoaFisica,
        on_delete=models.CASCADE,
        related_name='responsaveis'
    )

    class GrauParentesco(IntEnum):
        PAI_MAE = auto()
        AVO = auto()
        TIO = auto()
        OUTRO = auto()

    GRAU_PARENTESCO_CHOICES = (
        (GrauParentesco.PAI_MAE.value, _('Pai/Mãe')),
        (GrauParentesco.AVO.value, _('Avô/Avó')),
        (GrauParentesco.TIO.value, _('Tio/Tia')),
        (GrauParentesco.OUTRO.value, _('Outro')),
    )

    grau_parentesco = models.IntegerField(
        choices=GRAU_PARENTESCO_CHOICES, 
        null=True
    )

    grau_parentesco_outro = models.CharField(
        max_length=60, 
        blank=True, 
        null=True
    )
    

class PessoaJuridica(Pessoa):

    class Meta:
        verbose_name = _('Pessoa Jurídica')
        verbose_name_plural = _('Pessoas Jurídicas')

    cnpj = lf_models.BRCNPJField()

    matriz = models.ForeignKey(
        'self', 
        on_delete=models.PROTECT, 
        related_name='filiais', 
        null=True
    )

    @property
    def razao_social(self):
        return self.nome_razao_social


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
    
    complemento = models.CharField(max_length=255, blank=True, null=True)
    
    bairro = models.CharField(max_length=120)
    
    numero = models.CharField(max_length=120)
    
    cidade = models.CharField(max_length=120)
    
    uf = lf_models.BRStateField()

    # Define se é o endereço principal
    principal = models.BooleanField(default=False)

    pessoa = models.ForeignKey(
        Pessoa, 
        on_delete=models.CASCADE, 
        related_name='enderecos'
    )


class ContatoSocial(models.Model):

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
    
    pessoa = models.ForeignKey(
        Pessoa, 
        on_delete=models.CASCADE, 
        related_name='contatos_sociais'
    )

    def __str__(self):
        return '{}: {}'.format(self.tipo.value.title(), self.valor)


class DocumentoPessoalTipo(models.Model):

    class Meta:
        verbose_name = _('Documento Pessoal Tipo')
        verbose_name_plural = _('Documentos Pessoais Tipos')

    # RG CTPS CNH TITULO_ELEITOR PASSAPORTE RESERVISTA CERTIDAO_NASCIMENTO
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class DocumentoPessoal(models.Model):

    class Meta:
        unique_together = ('tipo', 'pessoa')
        verbose_name = _('Documento Pessoal')
        verbose_name_plural = _('Documentos Pessoais')

    tipo = models.ForeignKey(DocumentoPessoalTipo, on_delete=models.PROTECT)
    
    valor = models.CharField(max_length=60)
    
    pessoa = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, 
        related_name='documentos'
    )
    
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.tipo, self.valor)


class Telefone(models.Model):

    class Meta:
        unique_together = ('numero', 'pessoa')

    class Tipo(IntEnum):
        FIXO = auto()
        CEL = auto()

    TELEFONE_TIPO_CHOICES = (
        (Tipo.FIXO.value, _('Tel. Fixo')),
        (Tipo.CEL.value, _('Tel. Celular')),
    )

    tipo = models.IntegerField(choices=TELEFONE_TIPO_CHOICES)

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='telefones')
    
    numero = models.CharField(max_length=120, validators=[PhoneRegexValidator()])
    
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.numero
