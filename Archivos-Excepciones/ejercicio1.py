def listaFibonacci(numero):
    listafibonacci = [1,1]
    while listafibonacci[len(listafibonacci)-1] < numero:
        listafibonacci.append(listafibonacci[len(listafibonacci)-1] + listafibonacci[len(listafibonacci)-2])
    return listafibonacci

archivo = open("Archivos-Excepciones/ejercicio1.txt","r")
lineas = archivo.readlines()
max_porcentaje = 0
linea_max = 0
n_excepts_max = 0
for i,linea in enumerate(lineas):
    numeros = linea.split(",")
    numeros_int = []
    n_excepts = 0
    for num in numeros:
        try:
            numeros_int.append(int(num))
        except:
            n_excepts += 1
    numero_max = max(numeros_int)
    lista_fib_linea = listaFibonacci(numero_max)
    contador = 0
    for numero in numeros_int:
        if numero in lista_fib_linea:
            contador += 1
    if (contador/len(numeros_int)) > max_porcentaje:
        max_porcentaje = (contador/len(numeros_int))
        linea_max = i + 1
        n_excepts_max = n_excepts

print(f"La línea {linea_max} tiene mayor porcentaje de numeros de fibonacci. La razón es: {max_porcentaje} y tiene {n_excepts_max} excepciones.")
archivo.close()