## Ejercicios Recursividad  


#### 0. Crear una funcion recursiva `imprime_palabra(palabra, contador)` que imprima una palabra una cantidad definida de veces por el parámetro `contador` y que cuando haya mostrado esa cantidad de palabras imprima el mensaje "fin".

Solución
```
def imprime_palabra(palabra, contador):
    if contador == 0:  # caso base: no llamar a la función si esto ocurre
        print("fin") # Hemos llegado al caso base y la función dejará de llamarse!
        return
    else: # si no ocurre el caso base, hacer algo y llamar a la función

        print(palabra)
        imprime_palabra(palabra, contador-1) # se retorna el valor de la funcion
imprime_palabra("palabra", 3)

```


#### 1. Programar la función range de Python recursivamente con dos argumentos (número inicial y número final).  
```
4,10
[4,5,6,7,8,9,10]
```
##### Desafío, implementar el tercer argumento de salto.  

#### 2. Programar de forma recursiva la funcion `suma_range(n)` que retorna la suma de 1 hasta un número n.
Ejemplo
```
num = 10
print(suma_range(num))
```
Salida
```
55
```
 

#### 3. Programar de forma recursiva la funcion `suma_digitos(n)` que dado un número n retorne la suma de sus dígitos.

Ejemplo
```
num = 12345
print(suma_de_digitos(num))
```

Salida
```
15
```

#### 4. Crear la función máximo común divisor de manera recursiva, que dado 2 números `a` y `b` retorne el M.C.D entre estos dos números.

Ejemplo 
```
num1 = 16
num2 = 36
print(mcd(num1, num2))
```

Salida
```
4
```

#### 5. Se recibe una lista, se debe ordenar y luego buscar un elemento en la lista recursivamente con la siguiente estrategia.
```  
1. Si el elemento de la mitad de la lista es el elemento a buscar retornar True.
2. Si el elemento es menor que el elemento de la mitad de la lista entonces buscar en una nueva lista desde el primer elemento hasta el elemento de la mitad de la lista.  
3. Si el elemento es mayor hacer lo mismo que el paso 2 pero esta vez del elemento de la mitad de la lista hasta el último.
```
```
[1,2,3,4,5] , 5  
True
``` 
#### 6. Mezclar dos listas ordenadas de forma recursiva de tal manera que la lista resultante esté también ordenada.  
```
[-1,4,10],[2,3,7]  
[-1, 2, 3, 4, 7, 10]
```  


#### 7. Programar una función recursiva que multiplique el primer y el último elemento de una lista, luego esto sumarlo con el mismo procedimiento aplicado a la lista resultante después de retirar los elementos anteriormente multiplicados.  
```
[1,2,3,0,5]
8
```
#### Ahora hacer lo mismo pero que divida el primer y último elemento.  
```
[1,2,3,0,5]
5.2
```  


#### 8.(Desafio) Programe una función recursiva que retorne la cantidad de combinaciones correctas para devolver un vuelto dada una lista (con los valores de monedas a utilizar) y el vuelto.   
```  
[1,10,50,100],1000
4246
```
```
[1,2],2
2
```
