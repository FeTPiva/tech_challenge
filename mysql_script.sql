  
 
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
    dt_time TIMESTAMP,
    ds_status varchar(45),
    id_cliente int,
    primary key (id_pedido)
);

drop table if exists produto;
CREATE TABLE produto(
    id_produto int not null AUTO_INCREMENT,
    ds_nome varchar(100),
    id_categoria int,
    val_preco float,
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
(ds_nome, id_categoria, val_preco)
VALUES ('x-tudo',1, 10.0),
('x-veggie',1, 5.5),
('fritas',2, 5.0),
('arroz',2, 5.0),
('suco',3, 6.0),
('guarana',3, 5.0),
('brigadeiro de ouro',4, 10.0);

