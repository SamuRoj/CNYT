# Experimento Doble Rendija:

Realizado por:
- Sebastián Rodríguez
- Samuel Rojas Yopasa
- Laura Valentina Gutiérrez

## Historia
El experimento de la doble rendija en la física cuántica inició 
con el estudio de la luz, se realizaron diferentes pruebas que llegaron a demostrar que la luz se comportaba como una onda electromagnética, pero tiempo después, alrededor del siglo 20,Thomas Young en 1801 observó como la luz algunas veces se comportaba como una onda y otras como partícula, este hecho generó controversia dentro de la física clásica ya que las ondas y las partículas son diferentes, una partícula está presente en una posición del espacio y tiene masa mientras que una onda no presenta masa y es una perturbación, sin embargo, la luz presentaba los dos comportamientos. Tiempo después, se realizaron experimentos pero con partículas como los electrones y se demostró que tienen un comportamiento similar al de la dualidad de la luz, al ser considerado como una partícula se concluyó que para observar el patrón de la pantalla, el electrón debía estar presente al tiempo sobre las dos rendijas.

## Explicación
Este experimento se prueba colocando una luz sobre una pantalla que tenga dos rendijas, haciendo esto la primer vez se creería que se reflejan dos franjas de luz, sin embargo, se va a encontrar que la luz en este caso se va a comportar como una onda, se comporta como si se tuvieran dos luces diferentes y en la parte del reflejo se podrá observar como las ondas se suman en algunas partes y se cancelan en otras provocando los fenómenos que se conocen como interferencia y superposición.

## Objetivo

El objetivo original del experimento era ver el comportamiento de la luz, para comprobar si se comportaba como onda o partícula, este experimento funcionó para comprobar la posibilidad de la existencia de un multiverso, soportando a la física cuántica y demostrando el fenómeno cuántico de la interferencia, lo que podemos observar en el patrón que genera el anterior experimento, si nosotros pudiéramos saber por qué rendija están pasando los fotones lo convertimos en algo deterministico, dejando de ser cuántico por qué sabemos por qué multiverso está pasando el fotón, por lo cual en nuestro experimento el fotón está chocando con si mismo en muchos universos y pgracias a esto es que podemos observar el patrón que se genera al realizar este experimento.

## Procedimiento de Elaboración
  1. Utilizamos los siguientes elementos para la elaboración del montaje: 
  
      - Láser verde
      - 1 Palo de Balso
      - Cartón 
      - Cinta
      - Cartulina Negra
      - ....

  ![Image text](https://github.com/SamuRoj/CNYT/blob/master/Materiales.jpeg)
    
  2. Realizamos dos cortes paralelos en la cartulina que usamos como pared, los cuales representan las rendijas.
      
  ![Image text](https://github.com/SamuRoj/CNYT/blob/master/Cartulina.jpeg)
  
  3. Tomamos el palo de balso y realizamos una base donde se pondrá el láser.
  
  ![Image text](https://github.com/SamuRoj/CNYT/blob/master/Láser.jpeg)


  4. Ponemos una cartulina negra como pantalla para ver el patrón obtenido y se enciende el láser para observar el resultado.

  ![Image text](https://github.com/SamuRoj/CNYT/blob/master/Resultado1.jpeg)

  ![Image text](https://github.com/SamuRoj/CNYT/blob/master/Prueba.jpeg)

  ![Image text](https://github.com/SamuRoj/CNYT/blob/master/Resultado2.jpeg)

  
  ### Video Doble Rendija
  
  Se encuentra dentro de los archivos del repositorio y se debe descargar.

  ## Simulación usando librería

Librería realizada en Python que contiene la simulación del experimento de la doble rendija.

## Para Empezar

### Prerequisitos

Lenguaje de programación Python, Idle o ejecución del programa desde terminal.

### Instalación y Ejecución

Descarga de los archivos LibQuantum.py, Matrix_Lib.py y Complex_Lib.py en un mismo directorio, además es necesario tener instalada la librería matplotlib.pyplot, para la ejecución de una de las funciones que se encuentra dentro.

### Archivo LibQuantum.py

Contiene las funciones que permiten realizar la simulación de la doble rendija. Algunas de las funciones que se encuentran dentro del archivo son:

```
RoundDecimal(matrix)                    'Recibe una matriz y redondea cada uno de sus valores con 5 dígitos de precisión.'

DoubleSlits(matrix, vector, slits, target, clicks)     'Recibe 5 parámetros permite simular el experimento de la doble rendija'

BarGraph(vector)                        'Recibe un vector y realiza un gráfico de barras de acuerdo al estado del vector.'
```

### Explicación de las pruebas realizadas

Al final del archivo se encuentran la matriz y el vector usados que permiten observar lo que sucede dentro del experimento de la doble rendija, en este caso tomamos una matriz de números complejos que representa un grafo en el que se encuentran las probabilidades de que la partícula esté presente en la posición dada, además se parte de un vector inicial en el que la partícula está presente en la posición 0 al inicio de la simulación, luego de dos clicks de tiempo o más, se observará como el vector resultante justo en la posición 5 presenta una probabilidad de 0 cuando esta debería ser la de mayor valor, aquí se presenta el fenómeno de interferencia en el que la luz se cancela consigo misma por algunas de las razones mencionadas anteriormente y además se observará un gráfico de barras con la distribución de las probabilidades sobre cada una de las posiciones del vector.