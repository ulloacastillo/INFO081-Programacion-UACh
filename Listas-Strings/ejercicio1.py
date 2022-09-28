def verificar_n_primo(n):
    n = int(n)
    for i in range(2,n):
        if n%i==0:
            return False
    return True

string = input("Ingrese string de entrada: ")
numeros = string.split(",")

lista_salida = []
for numero in numeros:
    if verificar_n_primo(numero):
        lista_salida.append(int(numero)*2)
    else:
        lista_salida.append(int(numero))
print(lista_salida)