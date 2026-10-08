# Sistema de Loja de Eletrónicos - Semana 06 (POO)

Este projeto implementa um sistema de gestão de produtos aplicando os pilares da Programação Orientada a Objetos (POO): Abstração, Encapsulamento, Herança e Polimorfismo.

## Diagrama de Classes

```mermaid
classDiagram
    class Produto {
        <<abstract>>
        - _nome : str
        - _preco_base : float
        + calcular_preco_final()* float
        + __str__() str
        + __repr__() str
        + __eq__(outro) bool
        + __lt__(outro) bool
    }

    class Smartphone {
        + bateria_mah : int
        + calcular_preco_final() float
        + __str__() str
    }

    class PerifericoGamer {
        + tem_rgb : bool
        + calcular_preco_final() float
        + __str__() str
    }
    
    class JogoDigital {
        + plataforma : str
        + calcular_preco_final() float
        + __str__() str
    }

    Produto <|-- Smartphone
    Produto <|-- PerifericoGamer
    Produto <|-- JogoDigital