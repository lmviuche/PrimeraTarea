import random
import numpy as np
import sys

#TAREA NÚMERO UNO

#HECHO POR: Luis Miguel Viuche Madroñero
#CÓDIGO: 20212020082
#FECHA: 04 OCT 2022


#PRIMERA PREGUNTA
def calcular_area_triangulo():

  l = float(input("Ingrese la base: "))
  h = float(input("Ingrese la altura: "))

  if l <= 0 or h <= 0:
    print("Los valores dados no son positivos")
  else:
    area_triangulo = lambda l, h: print("El área del triángulo es:",
                                        (l * h) / 2)

  return area_triangulo(l, h)


#Quite el comentario para probar la función
#calcular_area_triangulo()


#SEGUNDA PREGUNTA
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


#CUARTA PREGUNTA
def gaus_jordan():

  #Leer el número de incógnitas
  n = int(input('Ingrese el número de incognitas: '))

  #Creación de un arrglo con numpy de tamaño n x n+1
  #inicializado en 0 para almacenar la matriz aumentada
  a = np.zeros((n, n + 1))

  #Creación de un arreglo con numpy de tamaño n
  #inicializado en zero para almacenar el vector solución
  x = np.zeros(n)

  #Leer los coeficientes de la matriz
  print('Ingresar los coeficientes de la matriz:')
  for i in range(n):
    for j in range(n + 1):
      a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

  #Aplicación del método Gauss-Jordan
  for i in range(n):
    if a[i][i] == 0.0:
      sys.exit('Error... se encontró una división por cero')

    for j in range(n):
      if i != j:
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
          a[j][k] = a[j][k] - ratio * a[i][k]

  #Se obtiene la solución

  for i in range(n):
    x[i] = a[i][n] / a[i][i]
  print('\nLa solución requerida es: ')
  for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')


#Quite el comentario para probar el código
#gaus_jordan()


#QUINTA PREGUNTA
def hallar_integral():

  acum = 0
  i = 0

  b = int(input("Ingrese el limite superior: "))
  a = int(input("Ingrese el limite inferior: "))
  n = int(input("Ingrese el numero de subintervalos: "))

  T = (b - a) / n

  while i <= n:
    x = (T * i) + a
    f = pow(x, 2)  #La función (x^2)

    acum = acum + (f)
    i = i + 1

  acum = acum * T

  print("El resultado aproximado es: ", acum)


#Quite el comentario para probar la función
#hallar_integral()
