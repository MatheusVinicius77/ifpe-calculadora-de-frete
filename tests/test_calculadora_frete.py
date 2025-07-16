
from src.calculadora_frete.CalculadoraFrete import CalculadoraFrete
from src.calculadora_frete.CalculadoraFrete import FreteInvalidoException

import pytest



# -------------------
# Testes Positivos — Frete Grátis (CT1-01 a CT1-06 + CT1-10)
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia",
    [
        (100.01, 0.0),        # CT1-01
        (150.00, 10.0),       # CT1-02
        (500.00, 50.0),       # CT1-03
        (1000.00, 100.0),     # CT1-04
        (999999.99, 0.0),     # CT1-05
        (100.01, 10000.0),    # CT1-06
        (100.01, 0.0),        # CT1-10 — Teste de repetição
    ]
)
def test_calculo_frete_gratis_para_compras_acima_de_100(valor_compra, distancia):
    # Given
    calculadora = CalculadoraFrete(valor_compra, distancia)

    # When
    frete = calculadora.calcular()

    # Then
    assert frete == 0.0


# -------------------
# Testes Negativos — Entradas Inválidas (CT1-07 a CT1-09)
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia, mensagem_esperada",
    [
        (-150.00, 10.0, "Valor da compra deve ser maior que zero."),                  # CT1-07
        (0.00, 50.0, "Valor da compra deve ser maior que zero."),                     # CT1-08
        (100.01, -5.0, "Distância de entrega deve ser maior ou igual a zero."),       # CT1-09
    ]
)
def test_calculo_frete_gratis_entradas_invalidas(valor_compra, distancia, mensagem_esperada):
    with pytest.raises(FreteInvalidoException) as exc_info:
        CalculadoraFrete(valor_compra, distancia)
    assert str(exc_info.value) == mensagem_esperada

# --------------------
# Testes Negativos
# --------------------

@pytest.mark.parametrize(
    "valor_compra, distancia, mensagem_esperada",
    [
        (0, 10, "Valor da compra deve ser maior que zero."),
        (-50, 10, "Valor da compra deve ser maior que zero."),
        (150, -1, "Distância de entrega deve ser maior ou igual a zero."),
        (0, 0, "Valor da compra deve ser maior que zero."),
        (-200, -10, "Valor da compra deve ser maior que zero."),
    ]
)
def test_excecao_valores_invalidos(valor_compra, distancia, mensagem_esperada):
    # Given: Dados inválidos para o cálculo
    
    # When / Then: Espera-se que uma exceção seja lançada ao criar a calculadora
    with pytest.raises(FreteInvalidoException) as exc_info:
        CalculadoraFrete(valor_compra=valor_compra, distancia_entrega=distancia)
    
    assert str(exc_info.value) == mensagem_esperada



# --------------------
# CENÁRIO DE TESTE 02
# -----------------------


@pytest.mark.parametrize(
    "valor_compra, distancia, frete_esperado",
    [
        (70.00, 0.0, 5.00),           # CT2-01
        (100.00, 20.0, 10.00),        # CT2-02 ✅ Corrigido
        (85.00, 10.0, 7.50),          # CT2-03 ✅ Corrigido
        (99.99, 50.0, 17.50),         # CT2-04 (já estava certo)
        (70.00, 15.5, 8.88),          # CT2-05 (conferido, correto)
        (100.00, 0.0, 5.00),          # CT2-06
        (70.00, 1000.0, 255.00),      # CT2-10
    ]
)
def test_calculo_frete_desconto_50_percent(valor_compra, distancia, frete_esperado):
    # Given
    calculadora = CalculadoraFrete(valor_compra, distancia)
    
    # When
    frete = calculadora.calcular()
    
    # Then
    assert round(frete, 2) == frete_esperado
    
    

# -------------------
# Testes Negativos com Parametrize
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia, mensagem_esperada",
    [
        (100.00, -5.0, "Distância de entrega deve ser maior ou igual a zero."),  # CT2-07
        (-70.00, 10.0, "Valor da compra deve ser maior que zero."),              # CT2-08
        (0.00, 5.0, "Valor da compra deve ser maior que zero."),                 # CT2-09
    ]
)
def test_excecao_entradas_invalidas(valor_compra, distancia, mensagem_esperada):
    with pytest.raises(FreteInvalidoException) as exc_info:
        CalculadoraFrete(valor_compra, distancia)
    assert str(exc_info.value) == mensagem_esperada


# -------------------
# Testes Positivos — Frete integral
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia, frete_esperado",
    [
        (69.99, 0.0, 10.00),       # CT3-01
        (50.00, 20.0, 20.00),      # CT3-02
        (10.00, 10.0, 15.00),      # CT3-03
        (0.01, 50.0, 35.00),       # CT3-04
        (69.99, 15.5, 17.75),      # CT3-05
        (69.99, 0.5, 10.25),       # CT3-06
        (69.99, 1000.0, 510.00),   # CT3-07
    ]
)
def test_calculo_frete_integral(valor_compra, distancia, frete_esperado):
    # Given
    calculadora = CalculadoraFrete(valor_compra, distancia)

    # When
    frete = calculadora.calcular()

    # Then
    assert round(frete, 2) == frete_esperado


# -------------------
# Testes Negativos — Validação de entrada
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia, mensagem_esperada",
    [
        (69.99, -10.0, "Distância de entrega deve ser maior ou igual a zero."),  # CT3-08
        (-10.00, 5.0, "Valor da compra deve ser maior que zero."),               # CT3-09
        (0.00, 10.0, "Valor da compra deve ser maior que zero."),                # CT3-10
    ]
)
def test_excecao_entradas_invalidas_cenario3(valor_compra, distancia, mensagem_esperada):
    with pytest.raises(FreteInvalidoException) as exc_info:
        CalculadoraFrete(valor_compra, distancia)
    assert str(exc_info.value) == mensagem_esperada
    


# -------------------
# Testes Negativos — Validação de entradas inválidas (CT4-01 a CT4-04)
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia, mensagem_esperada",
    [
        (-100.00, 10.0, "Valor da compra deve ser maior que zero."),             # CT4-01
        (0.00, 5.0, "Valor da compra deve ser maior que zero."),                 # CT4-02
        (50.00, -1.0, "Distância de entrega deve ser maior ou igual a zero."),   # CT4-03
        (-1.00, -1.0, "Valor da compra deve ser maior que zero."),               # CT4-04 (Valor inválido é checado primeiro)
    ]
)
def test_excecao_validacao_entradas_invalidas(valor_compra, distancia, mensagem_esperada):
    with pytest.raises(FreteInvalidoException) as exc_info:
        CalculadoraFrete(valor_compra, distancia)
    assert str(exc_info.value) == mensagem_esperada


# -------------------
# Testes Positivos — Entradas válidas e cálculo correto (CT4-05 a CT4-10)
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia",
    [
        (50.00, 0.0),         # CT4-05
        (0.01, 0.0),          # CT4-06
        (99999.99, 10.0),     # CT4-07
        (99999.99, 0.0),      # CT4-08
        (100.00, 10000.0),    # CT4-09
        (0.000001, 1.0),      # CT4-10
    ]
)
def test_entradas_validas_calculo_frete(valor_compra, distancia):
    # Given
    calculadora = CalculadoraFrete(valor_compra, distancia)

    # When
    frete = calculadora.calcular()

    # Then
    assert frete >= 0  # O frete deve ser calculado sem exceção e ser um valor não negativo


# -------------------
# Testes Positivos — Limites e Bordas Válidas (CT5-01 a CT5-08)
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia, frete_esperado",
    [
        (100.00, 0.0, 5.00),         # CT5-01 — 50% desconto
        (100.01, 0.0, 0.00),         # CT5-02 — Frete grátis
        (70.00, 0.0, 5.00),          # CT5-03 — 50% desconto
        (69.99, 0.0, 10.00),         # CT5-04 — Frete integral
        (9999999.00, 0.0, 0.00),     # CT5-05 — Frete grátis
        (0.01, 0.0, 10.00),          # CT5-06 — Frete integral (mínimo válido)
        (50.00, 100000.0, 50010.00), # CT5-07 — Distância muito grande
        (69.99, 0.0, 10.00),         # CT5-08 — Distância mínima e frete integral
    ]
)
def test_valores_limite_e_borda_positivos(valor_compra, distancia, frete_esperado):
    # Given
    calculadora = CalculadoraFrete(valor_compra, distancia)

    # When
    frete = calculadora.calcular()

    # Then
    assert round(frete, 2) == frete_esperado


# -------------------
# Testes Negativos — Limites inválidos (CT5-09 e CT5-10)
# -------------------

@pytest.mark.parametrize(
    "valor_compra, distancia, mensagem_esperada",
    [
        (0.00, 0.0, "Valor da compra deve ser maior que zero."),             # CT5-09 — Valor inválido
        (100.00, -0.01, "Distância de entrega deve ser maior ou igual a zero."), # CT5-10 — Distância negativa
    ]
)
def test_valores_limite_e_borda_invalidos(valor_compra, distancia, mensagem_esperada):
    with pytest.raises(FreteInvalidoException) as exc_info:
        CalculadoraFrete(valor_compra, distancia)
    assert str(exc_info.value) == mensagem_esperada
