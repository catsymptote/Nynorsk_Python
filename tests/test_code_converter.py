from src.code_converter import Converter


def test_init():
    con = Converter()

    assert type(con) is Converter


def test_to_NN():
    con = Converter()
    code = '''
    for idx in range(10):
        print(idx)
    '''

    expected_code = '''
    forkvar idx inni massetall(10):
        skrivut(idx)
    '''

    new_code = con.to_NN(code)
    assert expected_code == new_code


def test_to_Py():
    con = Converter()
    expected_code = '''
    for idx in range(10):
        print(idx)
    '''

    code = '''
    forkvar idx inni massetall(10):
        skrivut(idx)
    '''

    new_code = con.to_Py(code)
    assert expected_code == new_code
