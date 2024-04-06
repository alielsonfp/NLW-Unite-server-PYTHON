O pass.in é uma aplicação de gestão de participantes em eventos presenciais.

A ferramenta permite que o organizador cadastre um evento e abra uma página pública de inscrição.

Os participantes inscritos podem emitir uma credencial para check-in no dia do evento.

O sistema fará um scan da credencial do participante para permitir a entrada no evento.

# Requisitos

## Requisitos funcionais

[ ✔ ] O organizador deve poder cadastrar um novo evento;

[ ✔ ] O organizador deve poder visualizar dados de um evento;

[ ✔ ] O organizador deve poder visualizar a lista de participantes;

[ ✔ ] O organizador deve poder se inscrever em um evento;

[ ✔ ] O organizador deve poder visualizar seu crachá de inscrição;

[ ✔ ] O organizador deve poder realizar check-in no evento;

## Regras de negócio

[ ✔ ] O participante só pode se inscrever em um evento uma única vez;

[ ✔ ] O participante só pode se inscrever em eventos com vagas disponíveis;

[ ✔ ] O participante só pode realizar check-in em um evento uma única vez;
Requisitos não-funcionais

[ ✔ ] O check-in no evento será realizado através de um QRCode;

# Especificações da API

 Swagger UI

https://nlw-unite-nodejs.onrender.com/docs/static/index.html

## Banco de dados

Nessa aplicação vamos utilizar banco de dados relacional (SQL). Para ambiente de desenvolvimento seguiremos com o SQLite pela facilidade do ambiente.

## Diagrama ERD

<img src="https://github.com/alielsonfp/NLW-Unite-server-PYTHON/blob/master/erd.svg" alt="Diagrama ERD" width="350" height="auto">

# Como executar

Para clonar este repositório e iniciar o servidor, siga estas etapas:

## Clonando o Repositório

Execute o seguinte comando no terminal para clonar o repositório:

git clone https://github.com/alielsonfp/NLW-Unite-server-PYTHON.git

## Executando a aplicação
Navegue até a pasta do projeto e execute o seguinte comando através do promp de comando para iniciar o servidor:

python app.py
