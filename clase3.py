import random

#Ejercicio 1

def mi_funcion(palabra):
 palabra1= palabra.strip().split(" ")
 print("La longitud de la última palabra es: {}".format(len(palabra1[-1])))

mi_funcion("Mundial Sudafrica")


#Ejercicio 2

texto = input("Ingrese un texto: ")

def mayuscul(cita):
  palabra2= cita.title().split(sep = " ")
  print(palabra2)

mayuscul(texto)


#Ejercicio 3

class Circulo:
    def __init__(self, radio_circulo):
        self.radio_circulo = radio_circulo
        
    def area_circulo(self):
        are=3.14*self.radio_circulo
        print("El área del círculo es: {}".format(are))

circulo1 = Circulo(4)
circulo1.area_circulo()


#Ejercicio 4

class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho

    def area_rectangulo(self):
        arect=self.largo*self.ancho
        print("El área del rectángulo es: {}".format(arect))

rectangulo1 = Rectangulo(6,4)
rectangulo1.area_rectangulo()


#Ejercicio 5

class Alumno:
    def __init__(self,nombre_alumn, num_registro):
        self.nombre_alumn = nombre_alumn
        self.num_registro = num_registro

    def Display(self):
        print("Nombre del estudiante: {}".format(self.nombre_alumn))
        print("Número de registro: {}".format(self.num_registro))

    def setAge(self, edad):
        print("La edad del alumno {} es: {}".format(self.nombre_alumn,edad))
    
    def setNota(self, nota):
        print("La nota del estudiante es: {}".format(nota))

alumno1 = Alumno("Jose Fernandez", "18170456")
alumno1.Display()
alumno1.setAge(21)
alumno1.setNota(15)


#Ejercicio 6

calificaciones = input("Ingrese las calificaciones del estudiante:")
calif = calificaciones.split(sep = ",")

for indice,nombre in enumerate(calif):
    try:
      print(int(calif[indice].split(".")[0]))
    except:
        print("Error en la calificación ingresada")
        break


#Ejercicio 7

n = input("Ingrese el número de filas a generar: ")
matriz = []
z = 0
for x in range(n):
    matriz.append([])

for x in range(n):
    for y in range(x+1):
        if y==0 or y==x:
            matriz[x].append(1)
        else:
            z=matriz[x-1][y]+matriz[x-1][y-1]
            matriz[x].append(z)
    print(str(matriz[x]))
input()



#Ejercicio 8

from aleatoriop8 import num_aleatorio
sep = num_aleatorio()

from aleatoriop8 import mostrar_aleatorio
mostrar_aleatorio(sep)

from aleatoriop8 import ordenar_aleatorio
ordenar_aleatorio(sep)


#Ejercicio 9

from aleatoriop9 import numer_aleatorio
numer = numer_aleatorio()

from aleatoriop9 import decisi_aleatorio
decisi_aleatorio(numer)

#Ejercicio 10
from operaciones import division
from operaciones import suma
from operaciones import resta
from operaciones import multiplicacion
suma()
resta()
multiplicacion()
division()