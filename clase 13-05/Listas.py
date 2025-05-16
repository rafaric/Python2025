lista = [3, 6, 3, 2, 5, "Ricardo", [5, 6, 3, 5, 5, 5, [3,4,5]]]
print(lista)
# Imprimir el primer elemento de la lista
#print(lista[0])
#imprimir el último elemento de la lista
#print(lista[-1])
#imprimir los elementos 3,2,5
#print(lista[2:5])
#imprimir los elementos desde el indice 3 hasta el final
#print(lista[3:])
#imprimir los elementos desde el inicio hasta el elemento con el índice 5
#print(lista[:6])
#agregar
lista.append("Rafael")
lista.insert(2, "Yayo")
#se le pasa el índice a eliminar - Predeterminado (no pasandole ningun valor) último indice.
lista.pop(2)
#se le pasa el VALOR que se desea eliminar - Da error si no existe ese valor en la lista.
#lista.remove("yayo")
print(lista)
#imprimir la lista en orden inverso
print(lista[::-1])