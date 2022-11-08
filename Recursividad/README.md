## Ejercicios Recursividad  
### Los ejercicios están ordenados de forma creciente en términos de dificultad (al menos para nosotros). Recordar todo lo que hemos visto  
###### Puede que tengan que usar excepciones

#### 1. Programar la función range de Python recursivamente con dos argumentos (número inicial y número final).  
```
4,10
[4,5,6,7,8,9,10]
```
##### Desafío, implementar el tercer argumento de salto.  

#### 2. Programar de forma recursiva la suma de 1 hasta un número n.
```
5
15
```  
#### 3. Se recibe una lista, se debe ordenar y luego buscar un elemento en la lista recursivamente con la siguiente estrategia.
```  
1. Si el elemento de la mitad de la lista es el elemento a buscar retornar True.
2. Si el elemento es menor que el elemento de la mitad de la lista entonces buscar en una nueva lista desde el primer elemento hasta el elemento de la mitad de la lista.  
3. Si el elemento es mayor hacer lo mismo que el paso 2 pero esta vez del elemento de la mitad de la lista hasta el último.
```
```
[1,2,3,4,5] , 5  
True
``` 
#### 4. Mezclar dos listas ordenadas de forma recursiva de tal manera que la lista resultante esté también ordenada.  
```
[-1,4,10],[2,3,7]  
[-1, 2, 3, 4, 7, 10]
```  


#### 5. Programar una función recursiva que multiplique el primer y el último elemento de una lista, luego esto sumarlo con el mismo procedimiento aplicado a la lista resultante después de retirar los elementos anteriormente multiplicados.  
```
[1,2,3,0,5]
8
```
#### Ahora hacer lo mismo pero que divida el primer y último elemento.  
```
[1,2,3,0,5]
5.2
```  


#### 6.(Ejercicio díficil) Programe una función recursiva que retorne la cantidad de combinaciones correctas para devolver un vuelto dada una lista (con los valores de monedas a utilizar) y el vuelto.   
```  
[1,10,50,100],1000
4246
```
```
[1,2],2
2
```
