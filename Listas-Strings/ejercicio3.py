lista1 = input().split(" ")

indices = input().split(" ")
for i in range(len(indices)):
    indices[i] = int(indices[i])

nueva_lista = []

for i in range(len(lista1)):
    nueva_lista.insert(indices[i], lista1[i])

print(nueva_lista)

