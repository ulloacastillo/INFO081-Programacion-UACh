def es_anagrama(palabra1,palabra2):
    if len(palabra1) != len(palabra2):
        return False
    palabra1 = [i for i in palabra1]
    palabra2 = [i for i in palabra2]
    palabra1.sort()
    palabra2.sort()
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            return False
    return True

palabras = ["cero","mocasin","lugar","conversacion","cosa","poder","amor"]
frase = input("Ingresa tu frase: ").split(" ")
dictsalida = {}
for palabra in frase:
    for pal_clave in palabras:
        if es_anagrama(palabra,pal_clave):
            dictsalida[pal_clave] = palabra
print(dictsalida)
