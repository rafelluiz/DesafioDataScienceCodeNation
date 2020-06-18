# Comandos Docker

##### Listar Imagens
```
$ sudo docker image ls 
```

##### Listar Containers

```
$ sudo docker container ls 
```

##### Listar todos os Containers

```
$ sudo docker container ls -a
```

##### :no_entry: Remover todos os Containers de uma só vez

```
$ sudo docker container rm $(sudo docker container ls -a -q)
```

#### Criar Imagem Docker
Ex:

```

FROM python:3.8-alpine

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /statsapi

COPY app.py app.py
COPY statsapi/data_store.py statsapi/data_store.py
COPY statsapi/operation.py statsapi/operation.py

EXPOSE 5000

CMD python app.py

```

Salvar como **Dockerfile**

```
$ sudo docker build -t statsapi:0.0.1 . # onde o (.) seria o contexto
```

#### Rodar Imagem depois de criada

```
$ sudo docker run -ti -p 5000:5000 statsapi:0.0.1 # Onde -ti é para interação e -p seria a porta
```

