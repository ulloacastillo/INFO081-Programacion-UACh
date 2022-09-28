## Clase 1: Listas y Strings

### Ejercicio 1: Números primos

Se recibirá como input un String de números enteros (cantidad de números variable) separado por una coma (,). El programa imprimir una lista con los
números que aparecen en el String de entrada y si alguno de estos es primo se debe multiplicar por dos.

```
Input Ej: "12,13,4,9,11"
Output Ej: [12,26,4,9,22]
```

### Ejercicio 2: ඞ Programong Us ඞ
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

### Ejercicio 3: Desafío Sort

Recibirás dos líneas de input (ambas Strings), donde cada línea debe ser tratada como lista. La primera lista tendrá strings y/o números y la 
segunda lista los índices que indican el orden de cada elemento en la lista final. Deberás ordenar la lista original según la secuencia dada por la 
segunda lista e imprimirla.

```
Input Ej: a b c
          1 2 0
Output Ej: ["c","a","b"] 
```
