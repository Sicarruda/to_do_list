import pytest
from email_validation import email_validation
from password_validation import password_validation


def test_testando_o_teste():
    assert 1==1


def test_verifica_email_invalidos():
    with pytest.raises(ValueError) as error:
        email_validation('123@')
    assert "não tem a forma correta" in str(error.value)

    with pytest.raises(ValueError) as error:
        email_validation('123@.com')
    assert "não tem a forma correta" in str(error.value)

    with pytest.raises(ValueError) as error:
        email_validation('@123.com')
    assert "não tem a forma correta" in str(error.value)

    with pytest.raises(ValueError) as error:
        email_validation('123@123')
    assert "não tem a forma correta" in str(error.value)
     
    with pytest.raises(ValueError) as error:
        email_validation('123.com')
    assert "não tem a forma correta" in str(error.value)
    
    with pytest.raises(ValueError) as error:
        email_validation('.com')
    assert "não tem a forma correta" in str(error.value)
    
    with pytest.raises(ValueError) as error:
        email_validation('@.com')
    assert "não tem a forma correta" in str(error.value)
    
    with pytest.raises(ValueError) as error:
        email_validation('123@132.c')
    assert "não tem a forma correta" in str(error.value)

    with pytest.raises(ValueError) as error:
        email_validation('')
    assert "não tem a forma correta" in str(error.value)
    
    assert  email_validation('123@123.com') == None


def test_verifica_senha_invalida():
    with pytest.raises(ValueError) as error:
        password_validation('')
    assert "senha menor que 6 caracteres" in str(error.value)

    with pytest.raises(ValueError) as error:
        password_validation('12345')
    assert "senha menor que 6 caracteres" in str(error.value)
    
    with pytest.raises(ValueError) as error:
        password_validation('012345678901234657890')
    assert "senha maior que 20 caracteres" in str(error.value)

    assert password_validation('123456') == None   
