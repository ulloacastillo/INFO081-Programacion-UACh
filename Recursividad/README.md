## Ejercicios Recursividad  
#### 1. Programar una función recursiva que multiplique el primer y el último elemento de una lista, luego esto sumarlo con el mismo procedimiento aplicado a la lista resultante después de retirar los elementos anteriormente multiplicados.  
```
[1,2,3,0,5]
8
```
#### Ahora hacer lo mismo pero que divida el primer y último elemento.  
```
[1,2,3,0,5]
5.2
```  
#### 2. Se recibe una lista, se debe ordenar y luego buscar un elemento en la lista recursivamente con la siguiente estrategia.
```  
1. Si el elemento de la mitad de la lista es el elemento a buscar retornar True.
2. Si el elemento es menor que el elemento de la mitad de la lista entonces buscar en una nueva lista desde el primer elemento hasta el elemento de la mitad de la lista.  
3. Si el elemento es mayor hacer lo mismo que el paso 2 pero esta vez del elemento de la mitad de la lista hasta el último.
```
```
[1,2,3,4,5] , 5  
True
```  
#### 3. Programar de forma recursiva la suma de 1 hasta un número n.
```
5
15
```  
#### 4. Mezclar dos listas ordenadas de forma recursiva de tal manera que la lista resultante esté también ordenada.  
```
[-1,4,10],[2,3,7]  
[-1, 2, 3, 4, 7, 10]
```  
#### 5. Programar la función range de Python recursivamente con dos argumentos (número inicial y número final).  
```
4,10
[4,5,6,7,8,9,10]
```
##### Desafío, implementar el tercer argumento de salto.

