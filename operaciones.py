def suma():
    try:
     a = int(input("Introduce el primer número: "))
     b = int(input("Introduce el segundo número: "))
     print("{} + {} = {}".format(a,b,a+b))
    except:
        print("Tipo de dato no válido")

def resta():
    try:
       a = int(input("Introduce el primer número: "))
       b = int(input("Introduce el segundo número: "))
       print("{} - {} = {}".format(a,b,a-b))
    except:
        print("Tipo de dato no válido")

def multiplicacion():
    try:
       a = int(input("Introduce el primer número: "))
       b = int(input("Introduce el segundo número: "))
       print("{} * {} = {}".format(a,b,a*b))
    except:
        print("Tipo de dato no válido")

def division():
    try:
       a = int(input("Introduce el primer número: "))
       b = int(input("Introduce el segundo número: "))
       if b==0:
         print("No es posible dividir entre cero")
       print("{} / {} = {}".format(a,b,a/b))
    except:
        print("Tipo de dato no válido")

    