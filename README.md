# Desafío 4 - Redes neuronales para predicciones


Bienvenido a Desafio 4. Este programa busca encontrar predecir el ganador de diversas partidas de League of Legends usando datos de estos y usandalas en una red de neuronal con backpropagation. 

<br></br>

## _Instrucciones de uso_

Para utilizar nuestro programa, se necesita Python 3+, y los siguientes packetes.
* Numpy (pip install numpy)
* Pandas (pip install pandas)
* sklearn (pip install scikit-learn)

Además de contener el archivo "games.csv" en la raíz, el cual conteine los datos de las partidas.

Para correr la aplicación, simplemente correr el comando `python main.py`



<center>


<p align="center">
  <img  src="https://i.imgur.com/FOCjLFY.png">
  
</p>
<p align="center">
  Fig 1.1 Comando de ejecución.
</p>


Luego, este imprimirá cada 10000 iteraciones donde esta ejecutandose en el proceso de train, siguiente realizando la fase test, imprimiendo el ganador de cada partida de la predicción, finalmente mostrando la precisión final de estas.




## _Descripción del problema_

El problema a resolver, es la predicción de partidas de League of Legends usando redes neuronales, entrenando los pesos con una base de datos de partidas, que contiene información tales como campeones, primera sangre, duración del juego y mas.
  

<br></br>

## _Descripción del algoritmo_

Respecto a la carga de datos antes del procedimiento mismo, se carga el archivo "games.csv". La interpretación de estos datos se detallará a continuación:


### _1 - Datos de entrada y de salida._

Luego de la carga del csv, se separó el archivo en las entradas y las clases de salidas, nombrandolas X e Y respectivamente. Para las entradas, no se consideración los datos de ID de la partida y el numero de la temporada, puesto que el primero es irrelevante y el segundo siempre es 9 en la base de datos. Y respecto a las clases de salida, se utilizó la columna "Winner" que indica el equipo ganador, Equipo 1 o Equipo 2, donde en se renombraron 0 y 1 para su futuro uso en la función activación.

Luego, estos fueron normalizados usando min-max, y finalmente X e Y fueron distribuidos de forma random en variables de train y test, el primero con 70% y el otro con 30%. 




<p align="center">
  <img  src="https://i.imgur.com/idD3vl9.png?1">
</p>

<p align="center">
  Fig 1 Interpretación de datos.
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
