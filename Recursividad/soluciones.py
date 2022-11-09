def rangeCasero(num_ini,num_fin):
    if num_fin == num_ini:
        return [num_fin]
    return rangeCasero(num_ini,num_fin-1) + [num_fin]
print(rangeCasero(4,10))























def sumaHastaN(num):
    if num == 1:
        return 1
    return num + sumaHastaN(num-1)
print(sumaHastaN(5))

def busquedaBinaria(lista,num_a_buscar):
    if len(lista) == 1 and lista[0] != num_a_buscar:
        return False
    if num_a_buscar == lista[len(lista)//2]:
        return True
    if num_a_buscar < lista[len(lista)//2]:
        return busquedaBinaria(lista[:len(lista)//2],num_a_buscar)
    else:
        return busquedaBinaria(lista[len(lista)//2:],num_a_buscar)




print(busquedaBinaria([1,2,3,4,5],5))

def mergeDosListas(lista1,lista2):
    if len(lista1) == 0:
        return lista2
    if len(lista2) == 0:
        return lista1
    if lista1[0] < lista2[0]:
        return [lista1[0]] + mergeDosListas(lista1[1:],lista2)
    else:
        return [lista2[0]] + mergeDosListas(lista1,lista2[1:])
print(mergeDosListas([-1,4,10],[2,3,7]))

def multiplicarElem(lista):
    if len(lista) == 1:
        return lista[0]
    if len(lista) == 0:
        return 0
    return lista[0] * lista[len(lista)-1] + multiplicarElem(lista[1:len(lista)-1])
print(multiplicarElem([1,2,3,0,5]))
# al hacer lista[:alguna posicion] retorna la lista hasta la posicion anterior a alguna posicion

def dividirElem(lista):
    if len(lista) == 1:
        return lista[0]
    if len(lista) == 0:
        return 0
    try:
        return lista[0] / lista[len(lista)-1] + dividirElem(lista[1:len(lista)-1])
    except:
        return lista[0] + dividirElem(lista[1:len(lista)-1])
    
        
print(dividirElem([1,2,3,0,5]))

#def vueltos(lista_monedas,repartir):
    #return

#print(vueltos[1,10,50,100],1000)

###Ejercicios de clases

def ordenaLista(lista):
    if len(lista) == 1:
        return lista
    elem_min = min(lista)
    idx_min = lista.index(elem_min)
    lista.pop(idx_min)
    return [elem_min] + ordenaLista(lista)

print(ordenaLista([1,6,2,9,3]))

def palabraOrdenada(palabra,ord_pal):
    if ord_pal > ord(palabra[0]):
        return False
    if len(palabra) == 1:
        if ord_pal <= ord(palabra[0]):
            return True
        else:
            return False
    return palabraOrdenada(palabra[1:],ord(palabra[0]))

print(palabraOrdenada("HOLA",ord('H')))
print(palabraOrdenada("AHLO",ord('A')))
print(palabraOrdenada("A",ord("A")))
