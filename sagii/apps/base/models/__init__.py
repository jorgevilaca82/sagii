from .pessoa import Pessoa
from .endereco import Endereco
from .contatosocial import ContatoSocial
from .documento import DocumentoPessoalTipo, DocumentoPessoal
from .telefone import Telefone
from ..pessoajuridica.models import PessoaJuridica
from ..pessoafisica.models import PessoaFisica, RelacaoDependencia

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