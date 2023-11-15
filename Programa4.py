#Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: 
#inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. 
#El nombre de la clase llamarla Triangulo.
class Triangulo:
    def inicializar(self, l1, l2, l3):
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3

    def imprimir(self):
        print("Ingresa el lado 1 del triángulo:", self.lado1)
        print("Ingresa el lado 2 del triángulo:", self.lado2)
        print("Ingresa el lado 3 del triángulo:", self.lado3)

    def calcular(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")

# Datos
triangulo1 = Triangulo()
triangulo1.inicializar(10, 10, 10)  
triangulo1.imprimir()
triangulo1.calcular()
        
            
    
       