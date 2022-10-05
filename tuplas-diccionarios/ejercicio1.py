entrada = [1,2,1,"Hola","chao","Hola",2,2,"Hola"]
dictsalida = {}
for elem in entrada:
    if elem not in dictsalida.keys():
        dictsalida[elem] = 1
    else:
        dictsalida[elem] += 1
for key in dictsalida.keys():
    print(f"El elemento {key} esta repetido {dictsalida[key]} veces.")