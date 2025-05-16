notas_estudiantes = {}
#.values() - nos da una lista con solamente los valores del diccionario (6,8,4,9)
#.keys() - nos da una lista con solamente las claves del diccionari ("alejandro","maria","jose","juan")
#.items() - nos da una lista de los pares de valores (("alejandro",6),("maria",8).....)

while True:
  nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar)")
  if nombre.lower() == 'salir':
    break

  if nombre in notas_estudiantes:
    print(f"El estudiante {nombre} ya tiene una nota registrada")
    continue
  nota = input(f"Ingrese la nota de {nombre}: ")

  if nota.isdigit():
    if 0<=int(nota) <=10: # controlamos el valor mínimo y máximo.
      notas_estudiantes[nombre] = int(nota) # con int convierto la cadena de texto en un número
    else:
      print("La nota debe ser un número entre 0 y 10")
  else:
    print("Por favor, ingrese una nota válida")

print("\nNotas registradas: ")
for nombre, nota in notas_estudiantes.items(): #trae cada uno de los pares de valore del diccionario
  print(f"{nombre}: {nota}")

if notas_estudiantes:
  promedio = sum(notas_estudiantes.values()) / len(notas_estudiantes)
  print(f"\nEl promedio de las notas es: {promedio}")
else:
  print("\nNo hay notas registradas")




  