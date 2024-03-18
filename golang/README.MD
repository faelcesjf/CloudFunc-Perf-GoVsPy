## Requisitos

[Docker](https://docs.docker.com/get-docker/)

## Construção do da Imagem Docker

```docker build -t go-img .```

## Run do Container Docker com a imagem construída

```docker run -p8080:8080 -t go-img```

## Endpoint HTTP Trigger

[http://localhost:8080/merge-sort-function](http://localhost:8080/merge-sort-function)
