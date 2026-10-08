from abc import ABC, abstractmethod

# 1. Classe Abstrata (Mãe)
class Produto(ABC):
    def __init__(self, nome: str, preco_base: float):
        # Chama os setters para aplicar as validações desde o início
        self.nome = nome
        self.preco_base = preco_base

    # 2. Encapsulamento com @property e Setters
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("O nome do produto não pode ser vazio.")
        self._nome = valor

    @property
    def preco_base(self):
        return self._preco_base

    @preco_base.setter
    def preco_base(self, valor):
        if valor < 0:
            raise ValueError("O preço base não pode ser negativo!")
        self._preco_base = valor

    # Método abstrato que as classes filhas são obrigadas a implementar
    @abstractmethod
    def calcular_preco_final(self) -> float:
        pass

    # 3. Métodos Especiais (Dunder)
    def __str__(self):
        return f"{self.nome} - Preço Base: R$ {self.preco_base:.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}(nome='{self.nome}', preco_base={self.preco_base})"

    def __eq__(self, outro):
        if isinstance(outro, Produto):
            return self.preco_base == outro.preco_base
        return False

    def __lt__(self, outro):
        if isinstance(outro, Produto):
            return self.calcular_preco_final() < outro.calcular_preco_final()
        raise TypeError("A comparação de ordenação deve ser feita entre Produtos.")

# 4. Classes Filhas (Herança e super)
class Smartphone(Produto):
    def __init__(self, nome: str, preco_base: float, bateria_mah: int):
        super().__init__(nome, preco_base)
        self.bateria_mah = bateria_mah

    # Polimorfismo: Imposto de 10%
    def calcular_preco_final(self) -> float:
        return self.preco_base * 1.10

    def __str__(self):
        return f"[Smartphone] {super().__str__()} ({self.bateria_mah}mAh) -> Final: R$ {self.calcular_preco_final():.2f}"


class PerifericoGamer(Produto):
    def __init__(self, nome: str, preco_base: float, tem_rgb: bool):
        super().__init__(nome, preco_base)
        self.tem_rgb = tem_rgb

    # Polimorfismo: Imposto de 5%
    def calcular_preco_final(self) -> float:
        return self.preco_base * 1.05

    def __str__(self):
        rgb = "Com RGB" if self.tem_rgb else "Sem RGB"
        return f"[Periférico] {super().__str__()} ({rgb}) -> Final: R$ {self.calcular_preco_final():.2f}"


class JogoDigital(Produto):
    def __init__(self, nome: str, preco_base: float, plataforma: str):
        super().__init__(nome, preco_base)
        self.plataforma = plataforma

    # Polimorfismo: Isento de impostos
    def calcular_preco_final(self) -> float:
        return self.preco_base

    def __str__(self):
        return f"[Jogo - {self.plataforma}] {super().__str__()} -> Final: R$ {self.calcular_preco_final():.2f}"


# 5. Testes e Demonstração
if __name__ == "__main__":
    print(f"{'='*50}\nTESTE DE ENCAPSULAMENTO (EXCEÇÕES)\n{'='*50}")
    try:
        # Tentativa de criar um produto com preço negativo
        p_invalido = Smartphone("Telemóvel Estragado", -500, 3000)
    except ValueError as e:
        print(f"Erro capturado com sucesso: {e}")

    print(f"\n{'='*50}\nDEMONSTRAÇÃO DE POLIMORFISMO\n{'='*50}")
    # Criação de pelo menos 10 instâncias
    catalogo = [
        Smartphone("Samsung Galaxy S25 Ultra", 7500.00, 5000),
        Smartphone("iPhone 15 Pro", 7000.00, 3274),
        Smartphone("Motorola Edge", 2500.00, 4500),
        PerifericoGamer("Teclado Mecânico Redragon Kumara K552W", 250.00, True),
        PerifericoGamer("Headset FIFINE AmpliGame H6", 300.00, True),
        PerifericoGamer("Earbuds QCY T13", 150.00, False),
        PerifericoGamer("Rato Logitech G Pro", 450.00, True),
        JogoDigital("Counter-Strike 2 (Prime)", 75.00, "Steam"),
        JogoDigital("Valorant (Passe de Batalha)", 40.00, "Riot Games"),
        JogoDigital("Fortnite (Pack V-Bucks)", 25.00, "Epic Games")
    ]

    # Iterando sobre a lista (o método comportar-se-á de forma diferente para cada classe)
    for produto in catalogo:
        print(produto)

    print(f"\n{'='*50}\nDEMONSTRAÇÃO DE ORDENAÇÃO (Dunder __lt__)\n{'='*50}")
    # Usa o método __lt__ internamente para ordenar pelo preço final
    catalogo_ordenado = sorted(catalogo)
    for p in catalogo_ordenado:
        print(f"R$ {p.calcular_preco_final():8.2f} | {p.nome}")