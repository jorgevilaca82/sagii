from django.contrib import admin
from sagii.apps.base import models as bm

# Register your models here.

@admin.register(bm.PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('nome_razao_social', 'cpf', 'estado_civil')


@admin.register(bm.Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    pass


@admin.register(bm.DocumentoPessoal)
class DocumentoPessoalAdmin(admin.ModelAdmin):
    pass


@admin.register(bm.DocumentoPessoalTipo)
class DocumentoPessoalTipoAdmin(admin.ModelAdmin):
    pass


@admin.register(bm.ContatoSocial)
class ContatoSocialAdmim(admin.ModelAdmin):
    list_display = ('tipo', 'valor')