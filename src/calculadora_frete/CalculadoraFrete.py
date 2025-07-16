class FreteInvalidoException(Exception):
    pass

class CalculadoraFrete:
    VALOR_FIXO = 10.0
    VALOR_POR_KM = 0.5

    def __init__(self, valor_compra: float, distancia_entrega: float):
        if valor_compra <= 0:
            raise FreteInvalidoException("Valor da compra deve ser maior que zero.")
        if distancia_entrega < 0:
            raise FreteInvalidoException("Distância de entrega deve ser maior ou igual a zero.")

        self.valor_compra = valor_compra
        self.distancia_entrega = distancia_entrega

    def calcular(self) -> float:
        frete_base = self.VALOR_FIXO + (self.VALOR_POR_KM * self.distancia_entrega)
        desconto = self.__calcular_desconto()
        frete_final = frete_base * (1 - desconto)
        return frete_final

    def __calcular_desconto(self) -> float:
        if self.valor_compra > 100:
            return 1.0  # frete grátis
        elif 70 <= self.valor_compra <= 100:
            return 0.5  # 50% desconto
        else:
            return 0.0  # sem desconto