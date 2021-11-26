import random

def numer_aleatorio():
    return random.randint(1,100)

def decisi_aleatorio(num):
    prim = int(input("Ingrese un número: "))
    if prim==num:
        print("Has ganado")
    else:
        if prim>num:
            print("El número {} es mayor que {}".format(prim,num))
        else:
            print("El número {} es menor que {}".format(prim,num))
