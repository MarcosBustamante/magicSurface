#! bash/bin

echo "Iniciando o deploy"

echo "minificando os arquivos"
source ./ci/msMinify.sh

echo "fazendo o deploy"
appcfg.py update . --oauth2

