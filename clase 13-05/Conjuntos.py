lista = [3, 5, 2, 4, 5, 5, 2, 3]
conjunto = set(lista)
conjunto2 = {5,7,1,3,4,9}
conjunto3 = {"hola", "mundo", "desde", "el", "informatorio"}
conjunto.add(10)
#conjunto.update({1, 1, 1, 1, 1})
conjunto3.update({2025})
print(conjunto3)

conjunto4 = conjunto
print(conjunto)
if 7 in conjunto2:
  print("el número 7 se encuentra dentro del conjunto 2")

for i in conjunto2:
  if i == 7:
    print("el número 7 se encuentra dentro del conjunto 2")
#print(conjunto2)
#print(conjunto3)