### Clase 1: Listas y Strings

### Ejercicio 1: Números primos

A los ayudantes de Programación no les gustan para nada los números primos, por ello se pide hacer un programa que reemplace los números primos.
Se recibirá como input un String de números enteros (cantidad de números variable) separado por una coma (,). El programa imprimir una lista con los
números que aparecen en el String de entrada y si alguno de estos es primo se debe multiplicar por dos.

Input Ej: "12,13,4,9,11"
Output Ej: [12,26,4,9,22]

### Ejercicio 2: ඞ Programong Us ඞ

"Programong Us" es un nuevo juego en donde 10 personas en conjunto deben arreglar un datacenter, pero hay un problema: Un integrante del equipo es un impostor y está desconectando todos los cables del datacenter.
Tu misión es descubrir cuál es el nombre del impostor y el numero de pasillo en el que fue descubierto desconectando los cables.
Se recibirán dos chats. El primero tendrá un número entero n en la primera línea y en las siguientes n lineas habrán mensajes de jugadores (entre ellos el impostor). El impostor siempre mandará un mensaje que diga: "yo no fui", de esta forma se descubre al impostor.

El segundo chat también tendrá un número entero n en su primera linea y en las otras n lineas tendra mensajes de los jugadores. Para encontrar
el número de pasillo en el cual se vió al impostor se debe buscar en los mensajes el nombre del impostor y cuando se encuentre se debe separar el número del pasillo del resto del mensaje. 

Input Ej Primer Chat: 5
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
Output Ej: "El impostor es Rojo y fue visto por última vez en el pasillo 10"

### Ejercicio 3: Desafío Sort

Recibirás dos líneas de input (ambas Strings), donde cada línea debe ser tratada como lista. La primera lista tendrá strings y/o números y la 
segunda lista los índices que indican el orden de cada elemento en la lista final. Deberás ordenar la lista original según la secuencia dada por la 
segunda lista e imprimirla.

Input Ej: a b c
          1 2 0
Output Ej: ["c","a","b"] 
