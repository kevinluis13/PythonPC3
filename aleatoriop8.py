import random

def num_aleatorio():
    lista=[]
    for i in range(0,20):
        if i==20:
            break
        else:
         save = random.randint(0,100)
         lista.append(save)
    return lista
    

def mostrar_aleatorio(lista):
    print(lista)

def ordenar_aleatorio(lista):
    lista.sort()
    print(lista)

num_aleatorio()