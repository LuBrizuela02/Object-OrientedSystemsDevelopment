""" Clase 7 - Ejercicio 12
Brizuela, Ludmila """

from abc import ABC, abstractmethod
import math

# Creación de la clase abstracta FiguraGeometrica
class FiguraGeometrica(ABC):
    def __init__(self, color_fondo: str, color_borde: str):
        self.color_fondo = color_fondo
        self.color_borde = color_borde

# Definición de los métodos abstractos de la clase
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

# Creación de las subclases Rectángulo, Circulo y Triángulo, las cuales heredan de la superclase 
class Rectangulo(FiguraGeometrica):
    def __init__(self, color_fondo: str, color_borde: str, base: float, altura: float):
        super().__init__(color_fondo, color_borde)
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
class Circulo(FiguraGeometrica):
    def __init__(self, color_fondo: str, color_borde: str, radio: float):
        super().__init__(color_fondo, color_borde)
        self.radio = radio

    def area(self) -> float:
        return math.pi * (self.radio ** 2)
    
    def perimetro(self) -> float:
        return (2 * math.pi) * self.radio
    
class Triangulo(FiguraGeometrica):
    def __init__(self, color_fondo: str, color_borde: str, base: float, altura: float):
        super().__init__(color_fondo, color_borde)
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2
    
    def perimetro(self) -> float:
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        return self.base + self.altura + hipotenusa

# Ejemplo de uso
def main():
    rectangulo = Rectangulo("Azul", "Blanco", 5, 8)
    print(f"Área del Rectángulo: {rectangulo.area()}. Perímetro del Rectángulo: {rectangulo.perimetro()}.")

if __name__ == "__main__":
    main()