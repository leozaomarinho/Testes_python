from soma_calc import soma,divisao

def test_soma(soma):
    
    sum = soma(2,4)
    assert sum==soma
    
def test_divisao(divisao):
    result = divisao(4,4)
    assert result == 1