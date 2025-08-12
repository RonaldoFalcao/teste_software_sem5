
# Suite de testes para `validar_voucher` com mutmut

Este repositório contém a função `validar_voucher` e uma suíte de testes **killers** para eliminar todos os mutantes gerados pelo [mutmut](https://github.com/boxed/mutmut).

## Regra de negócio

Voucher válido **apenas** para compras com valor entre **R$ 50,00** e **R$ 500,00**, **inclusive**.

```python
def validar_voucher(valor: float) -> bool:
    """Válido para valores entre 50.00 e 500.00 (inclusive)."""
    return 50.00 <= valor <= 500.00
```

## Como executar

### 1) Clonar e instalar dependências
```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2) Executar testes
```bash
pytest -q
```

### 3) Rodar mutmut
```bash
# 1. Rodar mutantes
mutmut run

# 2. Ver resultados
mutmut results

# (opcional) HTML interativo:
mutmut html
python -m http.server -d html
```

### 4) Configuração (pyproject.toml)
Este projeto já inclui uma configuração mínima do mutmut direcionando a pasta `src/loja`:
```toml
[tool.mutmut]
paths_to_mutate = "src/loja"
tests_dir = "tests"
runner = "python -m pytest -q"
backup = false
```
> Ajuste `paths_to_mutate` se mover a função.

## Estratégia para matar mutantes

- **Testes de fronteira inclusiva**: garantem que `50.00` e `500.00` são **válidos** e valores imediatamente fora são **inválidos**. Isso mata mutações que trocam `<=` por `<` ou `>=`.
- **Fuzzing baseado em propriedades (Hypothesis)**: verifica a especificação para uma ampla faixa de floats, capturando inversões lógicas (`not`), troca de operadores e mutações inesperadas.
- **Valores especiais**: `NaN` e `±inf` devem ser **inválidos** (comparações com `NaN` resultam em `False`).
- **Tipos inválidos**: entradas não numéricas devem levantar `TypeError` (comportamento nativo do Python ao comparar com float). Isso ajuda a detectar mutantes que mexam na expressão booleana de forma a mascarar exceções.

## Estrutura
```
src/
  loja/
    __init__.py
    voucher.py
tests/
  test_voucher_boundaries.py
  test_voucher_properties.py
  test_voucher_specials_and_types.py
.github/
  workflows/
    ci.yml
pyproject.toml
requirements.txt
README.md
```

## CI
Um workflow do GitHub Actions está incluído para rodar `pytest` e `mutmut` no push.

---

> Objetivo de avaliação: **`mutmut results`** deve retornar **0 sobreviventes** com esta suíte.
