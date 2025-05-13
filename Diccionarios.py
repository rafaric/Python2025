estudiante = {
    "nombre": "Rafael",
    "edad": 20,
    "curso": "Introducción a Python"
}

#print(estudiante["curso"])
estudiante.update({"email": "rafa@pyhton.com"})
#print(estudiante["email"])
estudiante["curso"] = "Introducción a Desarrollo Web"
#print(estudiante["curso"])
estudiante.pop("edad")
#print(estudiante)
print(estudiante.keys())
print(estudiante.values())
print(estudiante.items())