def pedir_pais():
    entrada = input("")
    if len(entrada) == 0:
        return "",[]
    else:
        pais,laminas = entrada.split(": ")
        laminas = laminas.split(",")
        return pais,laminas
album = {}
pais,laminas = pedir_pais()
if pais != "" and laminas !=[]:
    album[pais] = laminas
while pais != "" and len(laminas) != 0:
    pais,laminas = pedir_pais()
    if pais != "" and laminas !=[]:
        album[pais] = laminas
print()
pais_a_buscar = input("")
if pais_a_buscar not in album.keys():
    print("Pais no se encuentra registrado.")
else:
    print(f"Laminas de {pais_a_buscar}: ",len(album[pais_a_buscar]))
laminas_totales = 0
mayor_c_laminas,pais_c_menor = 0,""
menor_c_laminas,pais_c_mayor = 1e1000,""

for pais in album.keys():
    laminas_totales += len(album[pais])
    if len(album[pais])>mayor_c_laminas:
        mayor_c_laminas = len(album[pais])
        pais_c_mayor = pais
    if len(album[pais])<menor_c_laminas:
        menor_c_laminas = len(album[pais])
        pais_c_menor = pais
print(f"Laminas repetidas en total: {laminas_totales}")
print(f"Pais con menos laminas: {pais_c_menor}")
print(f"Pais con mas laminas: {pais_c_mayor}")
