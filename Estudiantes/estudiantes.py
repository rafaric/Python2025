import tkinter as tk
from tkinter import messagebox

notas_estudiantes = {}

#.values() - nos da una lista con solamente los valores del diccionario (6,8,4,9)
#.keys() - nos da una lista con solamente las claves del diccionari ("alejandro","maria","jose","juan")
#.items() - nos da una lista de los pares de valores (("alejandro",6),("maria",8).....)

""" 
def fun_nombre(params): 
  pass # clave para no hacer nada
 """

def ingresar_estudiante():
  """ while True:
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
      print("Por favor, ingrese una nota válida") """
  nombre = entrada_nombre.get().strip()  # .strip() elimina espacios al inicio y al final
  nota = entrada_nota.get().strip()

  if not nombre or not nota:
    messagebox.showwarning("Error", "Por favor, ingrese un nombre y una nota")
    return
  if nombre in notas_estudiantes:
    messagebox.showwarning("Error", f"El estudiante {nombre} ya tiene una nota registrada")
    return
  nota_num = int(nota)
  
  if 0 <= nota_num <= 10:
    notas_estudiantes[nombre] = nota_num
    listbox_estudiantes.insert(tk.END, f"{nombre}: {nota_num}")
    messagebox.showinfo("Éxito", f"Nota registrada para {nombre}")
  else:
    messagebox.showwarning("Error", "La nota debe ser un número entre 0 y 10")
  

def mostrar_notas(titulo, notas):
  print(f"\n{titulo}")
  for nombre, nota in notas.items(): #trae cada uno de los pares de valore del diccionario
    print(f"{nombre}: {nota}")


def calcular_promedio():
    """Calcula y muestra el promedio de las notas."""
    if notas_estudiantes:  # Verificamos si hay datos
        promedio = sum(notas_estudiantes.values()) / len(notas_estudiantes)
        messagebox.showinfo("Promedio de Notas", f"El promedio de las notas es: {promedio:.2f}")
    else:
        messagebox.showwarning("Advertencia", "No hay notas registradas.")




ventana = tk.Tk()
ventana.title("Gestión de Notas de Estudiantes")
ventana.geometry("400x400")

# Frame para el formulario (entradas y botones)
frame_form = tk.Frame(ventana, bg="lightgray")
frame_form.pack(side="top", fill="x", padx=10, pady=10)

tk.Label(frame_form, text="Nombre del estudiante:", bg="lightgray", fg="black", anchor="w").pack(fill="x")
entrada_nombre = tk.Entry(frame_form, bg="white", fg="black")
entrada_nombre.pack(fill="x", pady=5)

tk.Label(frame_form, text="Nota:", bg="lightgray", fg="black", anchor="w").pack(fill="x")
entrada_nota = tk.Entry(frame_form, bg="white", fg="black")
entrada_nota.pack(fill="x", pady=5)

frame_buttons = tk.Frame(frame_form, bg="lightgray")
frame_buttons.pack(fill="x", pady=5)
tk.Button(frame_buttons, text="Agregar Estudiante", command=ingresar_estudiante).pack(side="left", padx=5)
tk.Button(frame_buttons, text="Calcular Promedio", command=calcular_promedio).pack(side="left", padx=5)

# Frame para la lista de estudiantes
frame_lista = tk.Frame(ventana)
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

tk.Label(frame_lista, text="Estudiantes Registrados:", fg="black").pack(pady=5)
listbox_estudiantes = tk.Listbox(frame_lista)
listbox_estudiantes.pack(fill="both", expand=True)

ventana.mainloop()



""" 
ingresar_estudiante("6º A", notas_estudiantes)

mostrar_notas("Notas Registradas: ", notas_estudiantes)

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
   """
#calcular_promedio(notas_6toA)
#calcular_promedio(notas_6toB)
