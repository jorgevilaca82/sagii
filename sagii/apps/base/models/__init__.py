from .contatosocial import ContatoSocial
from .documento import DocumentoPessoalTipo, DocumentoPessoal
from .endereco import Endereco
from .pessoa import Pessoa
from .telefone import Telefone
from ..pessoafisica.models import PessoaFisica, RelacaoDependencia
from ..pessoajuridica.models import PessoaJuridica

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
]
