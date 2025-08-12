
Atividade de teste de software

Como não consegui instalar corretamente o pacote mutmut, usei o pytest para verificar os erros. No primeiro teste troquei o 'return 50.00 <= valor <= 500.00:' por 'return 50.00 < valor <= 500.00' e o teste retornou:

(.venv) PS C:\voucher-mutmut-suite> $env:PYTHONPATH="src"; pytest -q
F.........                                                                                                                         [100%]
=============================================================== FAILURES ================================================================
______________________________________________________ test_valores_validos[50.0] _______________________________________________________ 

valor = 50.0

    @pytest.mark.parametrize("valor", [
        50.0,                  # limite inferior inclusivo
        75.0,                  # dentro do intervalo
        500.0,                 # limite superior inclusivo
        50.1,                  # ligeiramente acima do limite inferior
        499.9,           # ligeiramente abaixo do limite superior
    ])
    def test_valores_validos(valor):
>       assert validar_voucher(valor) is True
E       assert False is True
E        +  where False = validar_voucher(50.0)

tests\test_voucher_AVL.py:14: AssertionError
======================================================== short test summary info ==        ======================================================   



FAILED tests/test_voucher_AVL.py::test_valores_validos[50.0] - assert False is True 

Depois de corrigir o erro as 10 condições de valores limites passaram no teste:

(.venv) PS C:\voucher-mutmut-suite> $env:PYTHONPATH="src"; pytest -q
..........                                                                                                                         [100%]
10 passed in 0.67s



1 failed, 9 passed in 0.96s
