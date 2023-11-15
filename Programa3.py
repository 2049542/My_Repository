#Confeccionar una clase que permita carga el nombre y la edad de una persona. 
#Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
class Adulto:
    def inicializar(self, nom, edad):
        self.nombre=nom
        self.edad=edad
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad: ", self.edad)
    def calcular(self):
        if self.edad>=18:
          print (self.nombre, "Es mayor de edad. ")
        else:
            print (self.nombre, "Es menor de edad. ")

#Datos
adulto1=Adulto()
adulto1.inicializar("Rogelio", 52)
adulto1.imprimir()
adulto1.calcular()
