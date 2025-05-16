a= {1, 2, 3, 4}
b= {3, 4, 5, 6}

# metodo symmetric_difference
diferencia_simetrica = a.symmetric_difference(b)
print("Diferencia simétrica:", diferencia_simetrica)

# metodo con operador ^
diferencia_simetrica2 = a ^ b
print("Diferencia simétrica con operador ^:", diferencia_simetrica2)

#Distinción con diferencia:
diferencia = a.difference(b)
print("Diferencia:", diferencia)
diferencia2 = b.difference(a)
print("Diferencia en b:", diferencia2)