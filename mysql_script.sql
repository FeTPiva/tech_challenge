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
	id_pedido int not null AUTO_INCREMENT,
    dt_pedido TIMESTAMP,
    dt_entrega TIMESTAMP,
    ds_status varchar(45),
    id_cliente int,    
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
    dt_atualizacao TIMESTAMP,
    primary key (id_produto)
);

drop table if exists categoria_produtos;
CREATE TABLE categoria_produtos(
    id_categoria int not null AUTO_INCREMENT,
    ds_nome varchar(100),
    primary key (id_categoria)    
);


INSERT INTO cliente
  ( ds_cpf,
    ds_nome ,
    ds_email )
VALUES
  ('123', 'Fernanda Piva', 'xxxxx'), 
  ('456', 'fulanito', 'abc@abc');


insert into categoria_produtos
(ds_nome)
VALUES ('lanche'),('acompanhamento'),('bebida'), ('sobremesa');

insert into produto
(ds_nome, id_categoria, val_preco, dt_atualizacao)
VALUES ('x-tudo',1, 10.0, CURRENT_TIMESTAMP()),
('x-veggie',1, 5.5, CURRENT_TIMESTAMP()),
('fritas',2, 5.0, CURRENT_TIMESTAMP()),
('arroz',2, 5.0, CURRENT_TIMESTAMP()),
('suco',3, 6.0, CURRENT_TIMESTAMP()),
('guarana',3, 5.0, CURRENT_TIMESTAMP()),
('brigadeiro de ouro',4, 10.0, CURRENT_TIMESTAMP());


insert into pedido (dt_pedido, dt_entrega, ds_status, id_cliente) values
(CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 'Finalizado', 1);

insert into pedido (dt_pedido, ds_status, id_cliente)
values (CURRENT_TIMESTAMP(), 'Recebido', 1), (CURRENT_TIMESTAMP(), 'Recebido', 1);

INSERT INTO itens_pedido (id_pedido, id_produto)
VALUES (1,1), (1,2),(2,3), (3,1), (3,2), (3,3);