# Desafio 3 - Manejo de Datos Espaciales

Bienvenido a Desafio 3. Este programa busca encontrar aplicaciones similares a partir de datos de entrada, utilizando KD Tree.

<br></br>

## _Instrucciones de uso_

Para utilizar nuestro programa, se necesita Python 3+, y los siguientes packetes.
* Numpy (pip install numpy)
* Pandas (pip install pandas)

Además de contener el archivo "Desafio3.csv" en la raíz.

Para correr la aplicación, simplemente correr el comando `python main.py`



<center>


<p align="center">
  <img  src="https://i.imgur.com/TLyW9UT.png">
  
</p>
<p align="center">
  Fig 1.1 Comando de ejecución.
</p>


Luego, mostrará la interfaz, en donde hay 4 opciones, para usarlas, el usuario debe ingresar el digito correspondiente. Estas seran explicadas a continuación.


### _1 - Mostrar información de una aplicación específica_

Para buscar una aplicación según nombre o ID, ingrese este luego de confirmar la opción. Este retornará el juego en cuestión con todos sus datos.
<p align="center">
  <img  src="https://i.imgur.com/2GBT4g9.png">
</p>

<p align="center">
  Fig 1.2 Busqueda de la aplicación mediante ID.
</p>

<p align="center">
  <img  src="https://i.imgur.com/U4g7qtC.png">
</p>

<p align="center">
  Fig 1.3 Busqueda de la aplicación mediante Nombre.
</p>



### _2 - Mostrar información de las 10 aplicaciones más parecidas a una aplicación dada_

Para buscar las 10 aplicaciones más parecidas a una aplicación dada, ingrese el ID luego de confirmar la opción. Este retornará las 10 aplicaciones de mas cercanas, desde el mas cercano al mas lejano, con su nombre e ID.

<p align="center">
  <img  src="https://i.imgur.com/JSFyrLe.png">
</p>

<p align="center">
  Fig 1.4 Busqueda de las 10 aplicaciones mas cercanas mediante un ID.
</p>



### _3 - Mostrar información de las 10 aplicaciones más parecidas a vector de atributos_


Para buscar las 10 aplicaciones más parecidas a una aplicación dada, los atributos del vector deben ser entregados luego de confirmar la opción, de la siguiente manera.

<p align="center">
  <img  src="https://cdn.discordapp.com/attachments/825467667955712031/842217743654191134/unknown.png">
</p>

<p align="center">
  Fig 1.5 Busqueda de las 10 aplicaciones mas cercanas según un vector de atributos.
</p>

### _0 - Salir de la aplicación_

Para salir de la aplicación, simplemente ingrese 0 en la terminal.




## _Descripción del problema_

Manuel está interesado en el mercado del desarrollo móvil, por lo que comenzó a recopilar toda la información de las aplicaciones más descargadas de una tienda. Manuel le pide a su equipo (uds.) que le hagan un programa que, a partir de los datos recopilados, obtenga información de aplicaciones similares a las que se encuentra desarrollando.

Nuestra solución al desafío 3 modela el problema con KD Tree, con los datos de las aplicaciones en sus nodos. Con esto, evitamos una comparación exhaustiva de 1 con otros 7000 elementos, reduciendo drasticamente el rendimiento y los tiempos de ejecución. Con esto, se implementaron las funcionalidades requeridas por el desafio:
* Mostrar información de una aplicación específica con un ID o Nombre
* Mostrar información de las 10 aplicaciones más parecidas a una aplicación a traves de un ID o dado una serie de atributos en un vector (price, size_bytes, prime_genre, …)

<br></br>

## _Descripción del algoritmo_



<p align="center">
  <img  src="https://i.imgur.com/1IhGb9i.png">
</p>

<p align="center">
  Fig 2.1 Pseudo codigo Vecinos mas cercanos.
</p>

Para la aplicación del algoritmo k nearest se implemento la solución propuesta en clase con los respectivos cambios que la harán compatible con python.


<p align="center">
  <img  src="https://i.imgur.com/3uUdqJ3.png">
</p>

<p align="center">
  Fig 2.2 Mas cercanos en Python.
</p>

En este sector del código observamos que primero se crean las estructuras explicitadas en el pseudocódigo, siendo “vecinos” equivalente a k nearest, “nodos visitados” siendo “nodos explorados”, y la pila S siendo idéntica.

Luego se procede a realizar la “inserción” del nodo para buscar el punto de inicio de la búsqueda.


<p align="center">
  <img  src="https://i.imgur.com/uDHGYhA.png">
</p>

<p align="center">
  Fig 2.3 Pop en la pila no vacia.
</p>

En este sector del codigo observamos la equivalencia a hacer s.pop mientras la pila no este vacía, y se chequea la condición para saber si debería ingresarse a la lista final. Un detalle de la implementación es que los primeros 10 datos observados se ingresan obligatoriamente, y son los datos posteriores los que analizar la distancia propiamente tal.


<p align="center">
  <img  src="https://i.imgur.com/WY2VBp6.png">
</p>

<p align="center">
  Fig 2.4 Comparación de sub-arboles.
</p>

Para terminar, el algoritmo realiza la comparación de los sub-arboles derechos e izquierdo para ver si en ellos podrían haber más candidatos. para esto se comparan la distancia del último elemento que es candidato a mejor con la distancia en la dimensión actual a la línea de separación, de poder existir un candidato ahí se vuelve a realizar la inserción del dato a este subárbol y consecuentemente al ingresarse a la pila S, se explora. 




<br></br>

## _Coevaluación_

| Criterio | Descripción  |  Fabían Pizarro | Rafael Diaz  | Leandro Villalobos |
|---|---|---|---|---|
|A. Asistencia y puntualidad   | Asistió siempre a las reuniones de proyecto y fue puntual.  | 2 | 1  | 1  |
| B. Integración  |  Siempre escucha y comparte las ideas de sus compañeros e intenta integrarlas. Busca cómo mantener la unión en el grupo. |  2 |  -2 | -3  |
| C. Responsabilidad  | Siempre entrega su trabajo a tiempo y el grupo no tiene que modificar sus fechas o plazos.  | -3  |  1 |  1 |
|  D. Contribución |  Siempre ofrece ideas para realizar el trabajo y propone sugerencias para su mejora. Se esfuerza para alcanzar los objetivos del grupo. |  -3 |1   | 3  |
|  E. Resolución de conflictos | En situaciones de desacuerdo o conflicto, siempre escucha otras opiniones y acepta sugerencias. Siempre propone alternativas para el consenso o la solución.  |  2 |  -1 | -2  |

### _Retroalimentación de compañeros_

| | Fabían Pizarro | Rafael Diaz  | Leandro Villalobos | 
|---|---|---|---|
| Fabían Pizarro | | + Disponible a toda hora <br></br> - Cuando le emociona una idea, la sigue ciegamente sin flexibilidad  |  + Buena disposición <br></br> - Dificultad de para comunicar idedas|
| Rafael Diaz  | + Trabaja muy duro y de manera eficiente <br></br> - Dificultad de comunicación para coordinarse con sus compañeros | | + Involucrado en la investigación y desarrollo del trabajo <br></br> - Dificultad de comunicación|
| Leandro Villalobos | + Liderazgo del grupo. <br></br> - A veces avanza sin previo aviso. | + Disponibilidad y comunicación. <br></br> - Sintaxis de pseudo codigo. | |

<br></br>

## _Presentación en video_

[Presentación en YouTube.](https://youtu.be/yUtvO6JW0jM)

[![Desafío 3:
Manejo de datos espaciales
](https://i.imgur.com/16S684v.png)](https://youtu.be/yUtvO6JW0jM "Desafío 3:
Manejo de datos espaciales
")
Copied
