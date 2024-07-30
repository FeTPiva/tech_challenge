from external.db_info import  ConfDB
import logging


def test_select_all():
    result = ConfDB().select_all_data(table='categoria_produtos' )
    expected = [{'id_categoria': 1, 'ds_nome': 'Lanche'}, {'id_categoria': 2, 'ds_nome': 'Acompanhamento'}, {'id_categoria': 3, 'ds_nome': 'Bebida'}, {'id_categoria': 4, 'ds_nome': 'Sobremesa'}]
    
    assert type(result) == list
    assert expected == result

def test_selec_filter():
    result = ConfDB().select_with_filter(table='categoria_produtos', field='ds_nome', value='Sobremesa')
    expected = [{'id_categoria': 4, 'ds_nome': 'Sobremesa'}]
    assert type(result) == list
    assert expected == result


def test_insert():
    data_test = {'ds_nome': 'Sobremesa2'}
    result = ConfDB().insert_data(table='categoria_produtos', data= data_test)

    assert result == 5

def test_update():
    data_test = {'ds_nome': 'Doce chic'}
    result = ConfDB().update_data(table='categoria_produtos', data= data_test, filter_field='id_categoria', value=5)

    assert result == None


def test_del():
    result = ConfDB().delete_data(table='categoria_produtos', field='id_categoria', value=5)

    assert result == None

