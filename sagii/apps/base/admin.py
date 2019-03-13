from django.contrib import admin
from sagii.apps.base import models as bm

# Register your models here.

class EnderecoInline(admin.StackedInline):
    model = bm.Endereco
    extra = 1

    fieldsets = (
        (None, {'fields': (
            ('tipo', 'cep', 'logradouro', 'numero'), 
            ('bairro', 'cidade', 'uf'), 
            ('complemento', 'principal')
        )}),
    )


class ContatoSocialInline(admin.TabularInline):
    model = bm.ContatoSocial
    extra = 1


class DocumentoPessoalInline(admin.TabularInline):
    model = bm.DocumentoPessoal
    extra = 1


class TelefoneInline(admin.TabularInline):
    model = bm.Telefone
    extra = 1


class PessoaAdminMixin(admin.ModelAdmin):
    inlines = (
        DocumentoPessoalInline, 
        EnderecoInline, 
        ContatoSocialInline,
        TelefoneInline,
    )


@admin.register(bm.PessoaFisica)
class PessoaFisicaAdmin(PessoaAdminMixin):
    list_display = ('nome_razao_social', 'cpf', 'estado_civil')

    fieldsets = (
        (None, {'fields': (
            ('cpf', 'nome_razao_social', 'sexo'),
            ('estado_civil', 'tipo_sanguineo'),
            ('natural_cidade', 'natural_uf'),
        )}),
    )
    

@admin.register(bm.PessoaJuridica)
class PessoaJuridicaAdmin(PessoaAdminMixin):
    list_display = ('nome_razao_social', 'cnpj')


@admin.register(bm.DocumentoPessoalTipo)
class DocumentoPessoalTipoAdmin(admin.ModelAdmin):
    pass


@admin.register(bm.RelacaoDependencia)
class RelacaoDependenciaAdmin(admin.ModelAdmin):
    pass