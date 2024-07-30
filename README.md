# Tech challenge - fase 2 - grupo 2

## O que é o projeto?
Este é o repositório dos projetos da pós Software Architecture da Fiap


## Objetivos

Com a ideia de criar rotas de uma lanchonete onde o cliente realiza pedido e pegamento, com a cozinha recebendo ele de forma eletronica, foi criada api python em FastApi


## Links

Miro com DDD, Event Storming e Desenho da arquitetura

```https://miro.com/app/board/uXjVKFny-xg=/?share_link_id=986615193565 ```


Acessando o swagger

``` http://localhost:8000/docs ``` 

Video

``` https://youtu.be/RqmwtUJ_qmw ```


## Arquitetura

![Desenho da arquitetura](img/desenho.png?raw=true "Title")


## Buildando a aplicação


Pré requisito - Docker e Kubernetes disponíveis na máquina local

<br>

1. Banco de dados

   
   Primeiro passo para garantir a execução da aplicação é subir o banco de dados mysql.
   Nessa versão do Tech Challenge ele funciona a partir de uma imagem Docker `my-mysql-image`, responsável por executar um script com alimentação de dados e criação de tabelas inicial.
   A partir dela o MySQL é instanciado via Kubernetes, com uso de um service, deployment e HPA.

   Criando imagem Docker
   
   `docker build -f db/Dockerfile -t my-mysql-image . `
   
   
   Com a imagem criada execute os comandos do kubernetes:

   ```
   kubectl apply -f db/mysql-deployment.yaml
   kubectl apply -f db/mysql-service.yaml
   kubectl apply -f db/mysql-hpa.yaml
   ```

   Com isso seu banco de dados deverá estar rodando, com 1 pod

   <br>

2. API

   
   A API foi feita com python + FastAPI. Para subir a aplicação, de forma similar ao banco de dados, é necessário criar a imagem docker local e em seguida subir a API pelo Kubernets.

   Criando imagem Docker
   
   `docker build -t api_img . `

   
   Com a imagem criada execute os comandos do kubernetes:

   
   ```
   kubectl apply -f fastapi-deployment.yaml
   kubectl apply -f fastapi-service.yaml
   kubectl apply -f fastapi-hpa.yaml
   ```
   

   Na API é necessário também realizar port forwarding para acessar seu swagger localmente.
   
   Para isso execute:
   
   `kubectl port-forward service/fastapi-service 8000:8000`

   
   Com isso a API pode ser consultada no endereço `http://localhost:8000/docs`

