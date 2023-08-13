import os

class elemento:
    def __init__(self, peso, calorias):
        self.peso= peso
        self.calorias= calorias

def calcular_calorias():

    return min(calorias)


E1=elemento(5,3)
E2=elemento(3,5)
E3=elemento(5,2)
E4=elemento(1,8)
E5=elemento(2,3)

#Main funtion
peso_input= input("Por favor ingresa el peso máximo: ")
calorias_input= input("Por favor ingresa el mínimo de calorías: ")

try:
    peso_int=int(peso_input)

except ValueError:
    print('Valor invalido, debe ser un numero entero')    