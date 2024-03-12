from intro_testes.soma_calc import soma

def test_soma(soma):
    
    sum = soma(2,4)
    assert sum==soma