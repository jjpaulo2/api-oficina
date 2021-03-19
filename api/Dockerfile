FROM python:3.9-buster
LABEL author='João Paulo Carvalho <jjpaulo2@protonmail.com>'

# DEFININDO O DIRETÓRIO PADRÃO DE COMANDOS E O
# LUGAR ONDE SERÁ MONTADO O VOLUME COMPARTILHADO

WORKDIR /api
VOLUME /api

# COPIANDO O ARQUIVO `requirements.txt`

COPY requirements.txt requirements.txt

# INSTALANDO AS DEPENDÊNCIAS DO PROJETO

RUN python -m pip install -r requirements.txt

# DEIXANDO A PORTA 8000 ACESSÍVEL

EXPOSE 8000

# EXECUTANDO O SERVIDOR UVICORN

CMD python -m uvicorn main:app \
    --reload \
    --host 0.0.0.0 \
    --port 8000