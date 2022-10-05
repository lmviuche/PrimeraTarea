#CUARTA PREGUNTA

import numpy as np
import sys


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
