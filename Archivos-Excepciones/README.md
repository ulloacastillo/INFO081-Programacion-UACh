### Ejercicio 1:
Se reciben n lineas en un archivo de texto. Cada linea consta de k numeros separados por una coma. El objetivo es encontrar la linea que tenga mayor porcentaje de números de la sucesión de fibonacci en ella en relación a su longitud.
Formula de la sucesión de fibonacci: Fib n = Fib n-1 + Fib n-2 con Fib 0 = 1 Fib 1 = 1

Ejemplo de Arhivo:
  ```
  1,2,b,5,a,10,15    
  9,2,7,1,z  
  ```
Output:
  La línea 1 tiene mayor porcentaje de numeros de fibonacci. La razón es: 0.6 y tiene 2 excepciones.


### Ejercicio 2:

Deberás escribir un programa que lea el contenido del archivo basededatos_pokemones.txt. Cada línea del archivo tiene los datos de un pokemon y tiene una estructura de valores separados por comas como se ve en un ejemplo:

```
Bulbasaur,Hierba,49,49,45,0
Ivysaur,Hierba,62,63,60,0
Pikachu,Electrico,35,55,40,0
Mewtwo,Psiquico,-,-,-,1
```

La estructura es así: "nombre,tipo,atque,defensa,velocidad,legendario".

Tu desafio será recibir por consola el nombre de un pokemón, buscarlo en el archivo e imprimir una linea "nombre (tipo): dano (es_legendario)" donde nombre será el nombre del pokemon, tipo su tipo, dano sus puntos de daño (explicados más adelante) y es_legendario tomará el valor de "es legendario" en caso de que el pokemon sea legendario y será "no es legendario" en caso contrario.

Los puntos de daño se calculan como la parte entera de la siguiente fórmula:(ataque / defensa) * velocidad.

Además, si no encuentras a un pokemon con el nombre solicitado deberás imprimir "No hay registro de nombre_pokemon en la base de datos" donde nombre_pokemon es el nombre ingresado mediante input.

En el caso de que el pokemón sea de tipo legendario (no se tienen registro de sus datos), se debe manejar con excepciones el cálculo de los puntos de daños para evitar posibles errores.


### Ejercicio 3:

Se tiene una red social que guarda su base de datos en archivos csv. Ellos desean encontrar dentro de sus usarios el/la que posea la mayor cantidad de seguidores y luego su publicación que tenga más likes. Para ello estarán disponibles 2 archivos:

* El archivo usuarios.csv contiene la información de usuarios, donde cada línea representa a un usuario y tiene 3 valores separados por coma: su identificador [entero positivo que representa al usuario), su nombre y su ocupación (trabajo), en ese orden. Un ejemplo de este archivo sería el siguiente.

```
190,Cynthia Brown,Quimico Farmaceutico
806,Kathy Padilla,Ingeniero en sistemas
652,Ashley Smith,Profesor
```

* Para encontrar cuál de estos usuarios es el que tiene más seguidores tendrás a disposicion el archivo seguimientos.csv en el que cada linea contiene dos identificadores de usuarios separados por comas en que la interpretación es "seguidor,seguido". Un ejemplo de este archivo sería el siguiente.

```
806,190
190,806
652,190
```

* Una vez encontrado al usuario con más seguidores deberás encontrar su publicación con más likes. Para esto se te entrega el archivo publicaciones.csv en que cada línea representa a una publicacion y tiene 3 valores separados por coma: el identificador del usuario que realizó la publicación, el contenido de su publicación y la cantidad de likes que recibió, en ese orden. Un ejemplo de este archivo sería el siguiente.

```
190,Trabajando para usted,3874
652,Paseando con la kuky,75400
652,¡Ay! no puede ser más lindo,56783
806,L@s estudiantes de INFO081 son sec@s,12666
```


