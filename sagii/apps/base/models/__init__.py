from ..pessoa.models import (
    Pessoa,
    ContatoSocial,
    DocumentoPessoalTipo,
    DocumentoPessoal,
    Endereco,
    Telefone
)
from ..pessoafisica.models import PessoaFisica, RelacaoDependencia
from ..pessoajuridica.models import PessoaJuridica
from ..unidade_organizacional.models import UnidadeOrganizacional

__all__ = [
    'Pessoa',
    'Endereco',
    'ContatoSocial',
    'DocumentoPessoalTipo',
    'DocumentoPessoal',
    'Telefone',
    'PessoaJuridica',
    'PessoaFisica',
    'RelacaoDependencia',
    'UnidadeOrganizacional'
]
