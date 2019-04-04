from django.shortcuts import get_object_or_404
from ... import models as bm

def find_pessoa(pk):
    return get_object_or_404(bm.Pessoa, pk=pk)

from . import (
    telefone,
    contatosocial,
    endereco,
    documento
)

