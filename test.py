from itertools import combinations

class elemento:
    def __init__(self, nombre, peso, calorias):
        self.nombre=nombre
        self.peso= peso
        self.calorias= calorias

def listar_elementos_caloriaspeso(items: list,calorias_min:int ,peso_limite:int ):
    #lista las combinaciones posibles
    n = len(items)
    lista_combinations = []
    for i in range(1,n+1):
      combination = combinations(items, i)
      lista_combinations.extend(combination)
      lista_combinaciones_validas=[]
      for combo in lista_combinations:
        total_peso=sum(item.peso for item in combo)
        total_calorias=sum(item.calorias for item in combo)
        lista_nombre=[item.nombre for item in combo]
        if total_calorias>calorias_min and total_peso<peso_limite:
          combinacion_nombre=','.join(lista_nombre)
          lista_combinaciones_validas.append((combinacion_nombre,total_peso,total_calorias))
          #print(combinacion_nombre)
          #print("Total peso",total_peso)
          #print("Total calorias", total_calorias)
    return lista_combinaciones_validas

def elegir_combinacion(lista_combinaciones:list ):
  #selecciona la mejor combinacion con mas calorias y menos peso
  combinacion=(0,1000,0)
  for elem in lista_combinaciones:
    if elem[2]>=combinacion[2]:
      if elem[1]<combinacion[1]:
        combinacion=(elem[0],elem[1],elem[2])
    #print(elem[0],elem[1],elem[2])
  return combinacion

E1=elemento("E1",5,3)
E2=elemento("E2",3,5)
E3=elemento("E3",5,2)
E4=elemento("E4",1,8)
E5=elemento("E5",2,3)

#Main funtion
peso_input= input("Por favor ingresa el peso máximo: ")
calorias_input= input("Por favor ingresa el mínimo de calorías: ")
try:
    peso_int=int(peso_input)
    calorias_int=int(calorias_input)
except ValueError:
    print('Valor invalido, debe ser un numero entero')    

items=[E1, E2, E3, E4, E5]
total_peso = sum(item.peso for item in items)
#print("Peso Total:", total_peso)

#llamar lista de combinaciones que cumplen los criterios ingresados por el usuario
lista_elementos=listar_elementos_caloriaspeso(items,calorias_int,peso_int)

seleccion=elegir_combinacion(lista_elementos)

print(f"los elementos optimos son: {seleccion[0]} con un peso total de: {seleccion[1]} y brindan: {seleccion[2]} calorias")

