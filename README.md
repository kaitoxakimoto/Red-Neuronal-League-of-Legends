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




### _2 - Estructura de la red neuronal._

Para la red neuronal, se creo una clase llamada "Neural Network". Para su construcción, este recibe un array con numeros correspondientes a las capas de la red, el primero siendo las capas de entrada, el ultimo la capa de salidas, y las restante de enmedio las capas ocultas.

<p align="center">
  <img  src="https://i.imgur.com/CwLO82m.png">
</p>

<p align="center">
  Fig 2 Estructura de la red.
</p>

La estructura usada por el equipo fue [n, n*2 + 1, n/2 + 1, 1]. Donde n es el numero de datos de entrada, en este caso 58, la primera capa oculta el doble de la entrada + 1, la siguiente la mitad de estas + 1, y finalmente la capa de salida, la cual contiene la clase que indica cual equipo fue ganador.




<p align="center">
  <img  src="https://upload.wikimedia.org/wikipedia/commons/6/64/RedNeuronalArtificial.png">
</p>

<p align="center">
  Fig 3 Red neuronal.
</p>

Un ejemplo parecido es la imagen anterior, donde n es 58, m es n*2 + 1 y la unica capa de salida.

Siguiente, se iniciaron los pesos de las capas, asignandoles valores entre -1 y 1.



### _3 - Proceso de training._

Para el proceso de training, este recibe los sigueintes parametros, los datos de la capa de entrada (X), los datos de los valores esperados de la clase (Y), la tasa de aprendizaje y la cantidad de interaciones. Si no se indican las ultimas dos, estos son 2% y 100000.

Luego, se agrega un array de 1 como bias, y por cada iteración se realiza el producto punto entre un dato random de la entrada y los pesos ocultos, los cuales pasan la función de activación, que en este caso, usamos sigmoid. Este dato, es una predicción con la cual se compara con el valor esperado para calcular el error. 


Siguiente, comieza el calculo de los deltas, el cual comienza desde la segunda capa hasta la ultima.


<p align="center">
  <img  src="https://i.imgur.com/NTZBe9z.png">
</p>

<p align="center">
  Fig 4 Training.
</p>

A continuación, se invierten los deltas y se realiza el paso de backpropagation, en donde se actualizan las capas y deltas, y mas importante, los pesos, donde estos se suman a la gradiente multiplicado por la tasa de aprendizaje, distribuyendose por toda la red, en cada una de las iteraciones, acercandose cada vez mas los valores esperados.



<p align="center">
  <img  src="https://i.imgur.com/2rmRrRn.png">
</p>

<p align="center">
  Fig 5 Actualización de la red y sus pesos.
</p>


### _4 - Predicción_

Una vez realizado el proceso de training, ya se tienen los pesos ocultos entrenados para realizar las prediciones. Para esto, la función recibe los datos de test de las entradas. Para el calculo de las estimaciones, se realiza el producto punto de las entradas por todos los pesos ocultos, aplicandose su función de activación. 
Debido a que estas predicciones no tienen un valor fijo entre 0 y 1 como los datos esperados, sino numeros decimales muy cercanos a estos, los datos fueron redondeados a int, quedando así como 0 y 1 para el calculo de la metrica de precisión.


<p align="center">
  <img  src="https://i.imgur.com/63DkmbM.png">
</p>

<p align="center">
  Fig 5 Actualización de la red y sus pesos.
</p>


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

[Presentación en YouTube.](https://www.youtube.com/watch?v=UwikvGJ8IwQ)

[![Desafío 3:
Manejo de datos espaciales
](https://i.imgur.com/sgLmpYo.png)](https://www.youtube.com/watch?v=UwikvGJ8IwQ "Desafío 3:
Manejo de datos espaciales
")
Copied
