class circulo:
    def __init__(self, radio):
        self._radio=radio
        self._pi=3.1415

    def calcularPerimetro(self):
        return 2*self._pi*self._radio
    
    def calcularArea(self):
        return self._pi*self._radio**2
    
c1=circulo(2.5)
print(c1.calcularArea())
print(c1.calcularPerimetro())
print(f"la consonante PI es={c1._pi}")
