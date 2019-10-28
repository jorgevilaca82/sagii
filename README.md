# sagii
## Sistema Aberto de Gestão Institucional Integrado

### Instalação

Instala as dependências. É necessário ter o [nodejs](https://nodejs.org/en/) e o [yarn](https://yarnpkg.com/en/) instalados.
```console
$ yarn
```

Compila assets e agrupa no static_extras dependencias do projeto instaladas pelo yarn

```
$ yarn build
```

Coloca as dependencias no diretório que o django consegue encontrar
```console
python manage.py collectstatic
```

Rode as migrações para que o schema do banco de dados esteja sincronizado com o código.

```console
python manage.py migrate
```

Carregue o banco de dados com os dados iniciais globais e de cada módulo que desejar. Exemplos:

```
$ python manage.py loaddata ./sagii/apps/base/fixtures/documentopessoatipo.yml
```

### Executando o projeto

Instale as depêndencias listadas no arquivo `requirements.txt`

```
$ pip install -r requirements.txt
```

Pode-se ter diferentes arquivos de configuração no projeto. É necessário passar o caminho do arquivo de configuração que desejar. Por convenção o projeto vem com dois arquivos diferentes de configuração, um para desenvolvimento e outro para produção no diretório `sagii/web/settings/enviroments`, são eles:

* `development.py`
* `production.py`

Modifiques-os como desejar.

Para executar o projeto em modo desenvolvimento rode o seguite comando no terminal:

```
python .\manage.py runserver --settings=sagii.web.settings.enviroments.development
```

#### Docker

Para executar o projeto utilizando docker:

```
$ yarn && yarn build
$ cp .env.sample .env  
$ docker-compose up --build
```
use a opção `--build` toda vez que quiser reconstruir as imagens, caso contrário o paramêtro é opcional.

Crie um super usuário:

```
docker exec -it sagii_web_1 python manage.py createsuperuser
```
onde `sagii_web_1` é o nome do container web criado.