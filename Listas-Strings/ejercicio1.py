def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

string = input("Ingrese string de entrada: ")
numeros = string.split(",") 

for i in range(len(numeros)):
    if es_primo(int(numeros[i])):
        numeros[i] = int(numeros[i]) * 2
    else:
        numeros[i] = int(numeros[i])


print(numeros)
