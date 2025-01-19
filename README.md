# Tech challenge - fase 1 - grupo 5x

## O que é o projeto?
Este é o repositório do trabalho da fase 1 de Software Architecture da Fiap


## Objetivos

Com a ideia de criar rotas de uma lanchonete onde o cliente realiza pedido e pagamento, com a cozinha recebendo ele de forma eletronica, foi criada api python em FastApi integrando a um banco de dados MySQL


## Links

Miro com DDD e Event Storming

```https://miro.com/app/board/uXjVKFny-xg=/?share_link_id=986615193565 ```

## Buildando a aplicação

``` docker compose up -d --build ``` 

## Acessando o swagger

``` http://localhost:8000/docs ``` 


## Detalhamentos da entrega

### DDD e Event Storming

Ambos fluxos estão documentados no Miro. Fluxo de pedido e pagamento está separado de
preparação e entrega pelos frames, com as etapas até a versão agregada final.
Uma observação é que devido a múltiplos caminhos possíveis da aplicação, principalmente em
pedido e pagamento, dividi em vários quadros o agregado ‘Pedido’, porém a nível de arquitetura
todos os pedidos são a mesma entidade.
Na parte de DDD mantive os fluxos juntos, pensando no ponto que ficaria mais simples para
uma pessoa de negócios entender, do que algo apartado por mais que no futuro a aplicação
possa vir a ser separada em microserviços.
