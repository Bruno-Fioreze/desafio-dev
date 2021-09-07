# Como Rodar a Aplicação.

Eu fiz utilizando docker e linux, então abra o terminal, caso for linux e digite a próxima linha.
docker run -p 3306:3306 --name local_mysql -e MYSQL_ROOT_PASSWORD=bycoders -d mysql:latest

Verifique se o container está rodando digitando o seguinte comando.
docker container ls

Conecte no banco utlizando o usuário root e a senha bycoders.
Assim que você conseguir conectar no banco crie uma instância chamada importador.

Faça um clone deste fork e entre na pasta raiz do projeto.

Crie uma venv utilizando o comando.
python -m venv venv.

Ative a venv utlizando o comando source venv/bin/activate e depois disso digite o seguinte comando  pip install requirements.txt.
Assim que terminar de instalar as dependência, rode os comandos abaixo.
python manage.py makemigrations e em seguida python manage.py migrate.
Também é necessário importar o arquivo .sql que coloquei na pasta dump. Ele serve para preencher a tabela tipo_transacao.


# End-Points.

A aplicação é bem simples e portanto só conta com dois end-points.

1 - /api/importador/get_all_cnab/
Este end-point não espera nenhum parâmetro e é utilizado apenas para pegar os dados importados.

2 - /api/importador/cnab/
Este end-point espera receber um arquivo txt.

# Um Pouco sobre a aplicação.

A aplicação foi feita utilizando Django, Django Rest Framework, Mysql e Docker no back-end e no frond end HTML, CSS, Javascript e Bootstrap.
Eu gosto de separar as pastas e arquivos em dois tipos global e local, pela estrutura do projeto da para perceber isso.

# .env

O ideal é que tenha um arquivo desse local e um no servidor, mas como é um teste, eu preferi subir ele no github para você que vai analisar o programa não prceisar criar ele.

Agradeço desde já pela atenção.