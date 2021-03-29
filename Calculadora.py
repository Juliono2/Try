class Calculadora:
    def __init__ (self):
        self.valor_1 = 0 
        self.valor_2 = 0
        self.resultado =0

    def sumar(self):
        """metodo encargado de la suma entre dos valores"""
        self.resultado = self.valor_1 + self.valor_2
    
    def restar(self):
        """metodo encargado de la resta entre dos valores"""
        self.resultado = self.valor_1 - self.valor_2
    
    def multiplicar(self):
        """metodo encargado de la multiplicacion entre dos valores"""
        self.resultado = self.valor_1 * self.valor_2
    
    def dividir(self):
        """metodo encargado de la division entre dos valores"""
        self.resultado = self.valor_1 / self.valor_2