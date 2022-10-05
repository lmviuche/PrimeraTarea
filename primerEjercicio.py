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