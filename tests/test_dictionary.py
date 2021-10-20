from src.nn_dict import NN_Dict


def test_Py_keywords():
    py_keywords = NN_Dict.Py_keywords()
    print(py_keywords)
    assert type(py_keywords) is list


def test_NN_keywords():
    nn_keywords = NN_Dict.NN_keywords()
    print(nn_keywords)
    assert type(nn_keywords) is list


def test_to_NN():
    assert NN_Dict.to_NN('while') == 'mens'
    assert NN_Dict.to_NN('elif') == 'omikkjehvis'
    assert NN_Dict.to_NN('self') == 'sjølv'
    assert NN_Dict.to_NN('int') == 'helvtal'


def test_to_Py():
    assert NN_Dict.to_Py('mens') == 'while'
    assert NN_Dict.to_Py('omikkjehvis') == 'elif'
    assert NN_Dict.to_Py('sjølv') == 'self'
    assert NN_Dict.to_Py('helvtal') == 'int'
