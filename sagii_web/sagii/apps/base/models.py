from django.db import models
from enum import IntEnum, Enum, auto
from django.utils.translation import gettext_lazy as _
from sagii.commons import ChoiceEnumCharValueMeta
# Create your models here.

class Pessoa(models.Model):
    nome_razao_social = models.CharField(max_length=255)


class PessoaFisica(Pessoa):
    
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

    
class PessoaJuridica(Pessoa):
    pass


class Endereco(models.Model):
    class Tipo(IntEnum):
        COMERCIAL = 1
        RESIDENCIAL = 2

    TIPOS_CHOICES = (
        (Tipo.COMERCIAL.value, _('Comercial')),
        (Tipo.RESIDENCIAL.value, _('Residencial')),
    )

    tipo = models.IntegerField(choices=TIPOS_CHOICES)
    cep = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=120)
    numero = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    uf = models.CharField(max_length=2)

    
    # Define se é o endereço principal
    principal = models.BooleanField()

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)