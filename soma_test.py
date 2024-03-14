from soma_calc import soma,divisao


class Matematica():
    def test_soma(soma):
        
        sum = soma(2,4)
        assert sum == 6
        
    def test_divisao(divisao):
        result = divisao(4,4)
        assert result == 1
    
