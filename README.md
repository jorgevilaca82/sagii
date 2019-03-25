# sagii
Sistema Aberto de Gestão Institucional Integrado

instalação

yarn # instala as dependencias
yarn build # compila assets e agrupa no static_extras dependencias do projeto instaladas pelo yarn
python manage.py collectstatic # coloca as dependencias no diretório que o django consegue encontrar