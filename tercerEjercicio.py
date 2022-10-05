#TERCER PREGUNTA

def euler_sin_recursividad():
  n = int(input("Ingrese el valor de n: "))
  a = 1
  n_factorial = 1
  c = 0

  for i in range(n):
    n_factorial *= a
    b = a / n_factorial
    c += b
    a += 1

  return print("Sin recursividad:", c)


def factorial(n):
  if n > 1:
    return n * factorial(n - 1)
  return 1


def euler_con_recursividad(n):
  if n > 1:
    return n / factorial(n) + euler_con_recursividad(n - 1)
  return 1


#La diferencia la forma recursiva permite que un bloque de instrucciones se ejecute un
#cierto número de veces. Esta cantidad de veces la realizamos llamando a la misma función
#dentro de si mismo. La forma iterativa se basa en la repetición de ciclos, funcionales
#100% en tareas repetitivas como recorrer un arreglo de datos, una lista, etc…

#Quite el comentario para probar el código
#euler_sin_recursividad()
#print("Con recursividad:", euler_con_recursividad(50))