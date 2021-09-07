# Como Rodar a Aplicação .

Eu fiz utilizando docker e linux, então abra o terminal, caso for linux e digite a próxima linha.
<br />
docker run -p 3306:3306 --name local_mysql -e MYSQL_ROOT_PASSWORD=bycoders -d mysql:latest
<br />
Verifique se o container está rodando digitando o seguinte comando.
<br />
docker container ls
<br />
Conecte no banco utlizando o usuário root e a senha bycoders.
<br />
Assim que você conseguir conectar no banco crie uma instância chamada importador.
<br />
Faça um clone deste fork e entre na pasta raiz do projeto.
<br />
Crie uma venv utilizando o comando.
<br />
python -m venv venv.
<br />
Ative a venv utlizando o comando source venv/bin/activate e depois disso digite o seguinte comando  pip install requirements.txt.
<br />
Assim que terminar de instalar as dependência, rode os comandos abaixo.
<br />
python manage.py makemigrations e em seguida python manage.py migrate.
<br />
Também é necessário importar o arquivo .sql que coloquei na pasta dump. Ele serve para preencher a tabela tipo_transacao.
<br />

# End-Points.

<br />
A aplicação é bem simples e portanto só conta com dois end-points.
<br />
1 - /api/importador/get_all_cnab/
Este end-point não espera nenhum parâmetro e é utilizado apenas para pegar os dados importados.
<br />
2 - /api/importador/cnab/
Este end-point espera receber um arquivo txt.
<br />


# Um Pouco sobre a aplicação.


<br />
A aplicação foi feita utilizando Django, Django Rest Framework, Mysql e Docker no back-end e no frond end HTML, CSS, Javascript e Bootstrap.
Eu gosto de separar as pastas e arquivos em dois tipos global e local, pela estrutura do projeto da para perceber isso.
<br />

# Arquivo .Env .

<br />
O ideal é que tenha um arquivo desse local e um no servidor, mas como é um teste, eu preferi subir ele no github para você que vai analisar o programa não prceisar criar ele.
<br />
Agradeço desde já pela atenção.