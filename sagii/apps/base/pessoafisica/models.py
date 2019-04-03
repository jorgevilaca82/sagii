from enum import Enum, IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br import models as lf_models

from sagii.commons import ChoiceEnumCharValueMeta
from sagii.commons.constants import ONE_SPACE
from ..models.pessoa import Pessoa


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
        null=True,
        blank=True
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

    @nome.setter
    def nome(self, value):
        self.nome_razao_social = value

    def __str__(self):
        _s = nome_abreviado = self.nome.split(ONE_SPACE)
        # obtem o primeiro e último nome
        if len(_s) > 1:
            nome_abreviado = ONE_SPACE.join(_s[::len(_s) - 1])
        return '{} ({})'.format(nome_abreviado, self.cpf)

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('sagii_base:pessoafisica-detail', kwargs={'pk': self.pk})

    def __init__(self, *args, **kwargs):
        instance = super().__init__(*args, **kwargs)
        self._meta.get_field('nome_razao_social').verbose_name = _('Nome Completo')
        return instance


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
