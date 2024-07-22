SET sql_mode = '';
 
drop table if exists cliente;

 CREATE TABLE cliente(
    id_cliente int not null AUTO_INCREMENT,
    ds_cpf varchar(45),
    ds_nome varchar(200),
    ds_email varchar(45),
    primary key (id_cliente)
);

drop table if exists pedido ;
CREATE TABLE pedido(
	  id_pedido int not null,
    dt_pedido TIMESTAMP NULL DEFAULT NULL,
    ds_status varchar(45),
    id_cliente int,
    dt_atualizacao TIMESTAMP,
    primary key (id_pedido)
);

drop table if exists itens_pedido;
CREATE table itens_pedido(
  id_itens_pedido int not null AUTO_INCREMENT,
  id_pedido int,
  id_produto int,
  primary key(id_itens_pedido)
);

drop table if exists produto;
CREATE TABLE produto(
    id_produto int not null AUTO_INCREMENT,
    ds_nome varchar(100),
    id_categoria int,
    val_preco float,
    ds_descricao varchar(100),
    primary key (id_produto)
);

drop table if exists categoria_produtos;
CREATE TABLE categoria_produtos(
    id_categoria int not null AUTO_INCREMENT,
    ds_nome varchar(100),
    primary key (id_categoria)    
);

drop table if exists pagamento;
CREATE table pagamento(
  id_pagamento int not null AUTO_INCREMENT,
  val_valor float,
  ds_status TINYINT(1),
  id_pagamento_externo int,
  primary key(id_pagamento)
);

INSERT INTO cliente
  ( ds_cpf,
    ds_nome ,
    ds_email )
VALUES
  ('007.029.330-90', 'Fernanda Piva', 'xxxxx'), 
  ('080.850.056-20', 'fulanito', 'abc@abc');

insert into categoria_produtos
(ds_nome)
VALUES ('Lanche'),('Acompanhamento'), ('Bebida'), ('Sobremesa');

insert into produto
(ds_nome, id_categoria, val_preco, ds_descricao)
VALUES ('x-tudo',1, 10.0, 'Melhor x-tudo do mundo'),
('x-veggie',1, 5.5, 'É vegetariano? td bem, temos um x-veggie pra você'),
('fritas',2, 5.0, 'Melhor fritas do mundo'),
('arroz',2, 5.0, 'Melhor arroz do mundo'),
('suco',3, 6.0, 'suco padrão de laranja'),
('guarana',3, 5.0, 'guaraná do Brasil'),
('brigadeiro de ouro',4, 20.0, 'brigadeiro que vale o preço pago');


insert into pedido (id_pedido, dt_pedido, ds_status, id_cliente, dt_atualizacao) values
(1, CURRENT_TIMESTAMP(), 'Finalizado', 1, CURRENT_TIMESTAMP()),
(2, CURRENT_TIMESTAMP(), 'Recebido', 1, CURRENT_TIMESTAMP()),
(3, CURRENT_TIMESTAMP(), 'Recebido', 1, CURRENT_TIMESTAMP());

INSERT INTO itens_pedido (id_pedido, id_produto)
VALUES (1,1), (1,2),(2,3), (3,1), (3,2), (3,3);


INSERT INTO pagamento (val_valor, ds_status, id_pagamento_externo)
VALUES (8000.5,0,1), (14.1,1,1), (22.5,1,1);
