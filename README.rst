=====
SAGII
=====

Sistema Aberto de Gestão Institucional Integrado

Começo Rápido
-----------

1. Adicione uma ou mais aplicações ao seu projeto. é obrigatório a instalação
da app base

    INSTALLED_APPS = [
        ...
        'sagii.apps.base',
        'sagii.apps.academico',
    ]

2. Inclua as urls das aplicações desejadas em seu "urls.py":

    path('base/', include('sagii.apps.base.urls')),

3. Execute `python manage.py migrate` para criar a estrutura de banco de dados.

4. Inicie o servidor de desenvolvimento

5. Acesse o endereço local de desenvolviemento