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
