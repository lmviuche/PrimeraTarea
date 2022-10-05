#SEGUNDA PREGUNTA

import random


def max_min_de_una_lista():

  lista = []
  for i in range(20):
    number = random.randint(1, 999)
    lista.append(number)

  print(lista)
  return print("El número máximo de la lista es:", max(lista),
               "y el número mínimo es:", min(lista))


#Quite el comentario para probar la función
#max_min_de_una_lista()
