## Clase 1: Listas y Strings

### 7⃣ Ejercicio 1: Números primos

Se recibirá como input un String de números enteros (cantidad de números variable) separado por una coma (,). El programa imprimir una lista con los
números que aparecen en el String de entrada y si alguno de estos es primo se debe multiplicar por dos.

```
Input Ej: "12,13,4,9,11"
Output Ej: [12,26,4,9,22]
```

### ඞ Ejercicio 2: ඞ Programong Us 
Se te ha encargado la misión de descubrir a un impostor que se encuentra en un chat de WhatsApp. Tras largas investigaciones se ha descubierto que los impostores usar muy a menudo la frase "yo no fui" por lo que se te ha encargado leer los chats de este grupo de WhatsApp para saber el nombre del impostor. Para ello debes utilizar el primer chat para saber el nombre del impostor. El input de este chat consta de un número entero `n` seguido de `n` lineas que contienen los mensajes de los jugadores.

Adicionalmente se te pide que encuentres el día en que el impostor fue econtrado en un segundo chat.
El segundo chat también tendrá un número entero n en su primera linea y en las otras n lineas tendra mensajes de los jugadores. Para encontrar
el número del dia en el cual se vió al impostor se debe buscar en los mensajes el nombre del impostor y cuando se encuentre se debe separar el número del dia del resto del mensaje. 

Input
```
Ej Primer Chat: 5
                  Rojo: yo no fui
                  Verde: quien fue ?
                  Azul: yaaaa po cabros
                  Morado: Hola
                  Naranjo: Yo soy el impostor
 Ej Segundo Chat: 4
                  Rojo: yo vi al Azul en el 11 ! Ojo con el !
                  Verde: Nop, Rojo estaba en el pasillo 10
                  Naranjo: Que se sho
                  Morado: Naranjo estaba en el 4
```
Output
```
Ej: "El impostor es Rojo y fue visto por última vez en el día 10"
```

### ‼ Ejercicio 3: Desafío Sort

Recibirás dos líneas de input (ambas Strings), donde cada línea debe ser tratada como lista. La primera lista tendrá strings y/o números y la 
segunda lista los índices que indican el orden de cada elemento en la lista final. Deberás ordenar la lista original según la secuencia dada por la 
segunda lista e imprimirla.

```
Input Ej: a b c
          1 2 0
Output Ej: ["c","a","b"] 
```

### ⚖️ Ejercicio 4: Palabras equilibradas

### Parte A

Una palabra equilibrada es aquella que tiene tantas consonantes como vocales, como por ejemplo:
* Roja
* Morado
* Tapo

De igual manera existen palabras que son semi-equilibradas que son aquellas palabras que tienen una consonante más que vocales y vice versa, como por ejemplo:
* Tapiz
* araña
* computadoRa

Y finalmente las palabras que no sean ni equilibradas ni semi-equilibradas, se consideran no equilibradas:
* zapaTillas
* HelicopTeroS
* Etc


Para ello se le solicita escribir una funcion que reciba como parámetro una palabra y retorne si esta es `Equilibrada`, `Semi-Equilibrada` o `No Equilibradas`.

### Parte B

Por otro lado, podemos extender esto a palabras `k-equilibradas`, estas son palabras que cumplen que si al separarla cada k posiciones, todas sus porciones forman palabras equilibradas.

Una palabra se considera `semi-k-equilibrada` si no es k-equilibrada y al separarla cada k posiciones, todas sus porciones forman palabras equilibradas o semi-equilibradas.

Por último, una palabra que no sea k-equilibrada ni semi-k-equilibrada se considera `no-k-equilibrada`.

Por ejemplo:

* La palabra `siesta` es k-equilibrada cuando k vale 2, ya que se separa en las palabras si-es-ta, y todas estas palabras son equilibradas.
* La palabra `siesta` es semi-k-equilibrada cuando k vale 3, ya que se separa en las palabras sie-sta, y todas estas palabras son semi-equilibradas.
* La palabra `siesta` es k-equilibrada cuando k vale 4, ya que se separa en las palabras sies-ta, y todas estas palabras son equilibradas.
* La palabra `baile` es semi-k-equilibrada cuando k vale 2, ya que se separa en las palabras ba-il-e, ba e il son equilibradas, pero la palabra e es semi-equilibrada.
* La palabra `instrumento` es no-k-equilibrada cuando k vale 5, ya que se separa en las palabras instr-ument-o, como instr es no equilibrada, entonces inmediatamente la palabra es no-k-equilibrada.


En esta parte debes implementar la función kequilibrada(palabra, k), la cual recibe como parámetro un string palabra y un entero k, retorna el string "k-equilibrada" si la palabra es k-equilibrada, el string "semi-k-equilibrada" si la palabra es semi-k-equilibrada y el string "no-k-equilibrada" si la palabra es no-k-equilibrada.

