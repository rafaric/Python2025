notas_6toA = {}
notas_6toB = {}
#.values() - nos da una lista con solamente los valores del diccionario (6,8,4,9)
#.keys() - nos da una lista con solamente las claves del diccionari ("alejandro","maria","jose","juan")
#.items() - nos da una lista de los pares de valores (("alejandro",6),("maria",8).....)

""" 
def fun_nombre(params): 
  pass # clave para no hacer nada
 """

def ingresar_estudiante(grado, notas):
  while True:
    nombre = input(f"Ingrese el nombre del estudiante de {grado} (o 'salir' para terminar)")
    if nombre.lower() == 'salir':
      break

    if nombre in notas:
      print(f"El estudiante {nombre} ya tiene una nota registrada")
      continue
    nota = input(f"Ingrese la nota de {nombre}: ")

    if nota.isdigit():
      if 0<=int(nota) <=10: # controlamos el valor mínimo y máximo.
        notas[nombre] = int(nota) # con int convierto la cadena de texto en un número
      else:
        print("La nota debe ser un número entre 0 y 10")
    else:
      print("Por favor, ingrese una nota válida")

def mostrar_notas(titulo, notas):
  print(f"\n{titulo}")
  for nombre, nota in notas.items(): #trae cada uno de los pares de valore del diccionario
    print(f"{nombre}: {nota}")


def calcular_promedio(notas):
  return "no hay ganas de calcular"






ingresar_estudiante("6º A", notas_6toA)

mostrar_notas("Notas Registradas: ", notas_6toA)

#Calculo de promedios de la mitad de alumnos
if calcular_promedio({}) > 6:
  print("\nNo hay notas registradas")
else:
  print(f"\nEl promedio de las notas es: {calcular_promedio({})}")
#calculo de promedios de los ultimo años
notas_2018_2024 = {}
if calcular_promedio(notas_2018_2024) == 0:
  print("\nNo hay notas registradas")
else:
  print(f"\nEl promedio de las notas es: {calcular_promedio({})}")
  
#calcular_promedio(notas_6toA)
#calcular_promedio(notas_6toB)
