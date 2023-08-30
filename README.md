# CPU sin procesador
Esta CPU funciona sin un procesador que ejecute las instrucciones, sino que todo el circuito se comporta como un procesador, más bien es un microprocesador en formato grande.

## Compilacion de un programa ASM (ensamblador) a binario
* Ejecutar el archivo "generador_lista_control.py"
* Ejecutar el archivo "analizador_lexico.py" y seleccionar el proyecto que desea compilar en la terminal
* Copiar los archivos de la carpeta "archivosSD" a una MicroSD destinada a conectarse a la CPU
* Encender la CPU, presionar el boton PROG (programar) y encender la señal de CLOCK para que se ejecute el programa

## Partes que la componen
* Memoria RAM donde se almacenan las instrucciones que tiene que ejecutar y los datos con los cuales tiene que trabajar
* Un circuito de control que orquesta a todos los componentes electrónicos y dicta a qué velocidad funciona el conjunto
* Sistema de carga del programa, en donde mediante una tarjeta micro SD se guardan las instrucciones en formato binario
* Entradas y salidas de datos para interactuar con hardware externo

## Y... ¿Como hago para decirle que tiene que hacer?
Para ello se desarrolló un compilador en Python (también llamado analizador léxico) que es capaz de interpretar instrucciones simples y convertirlas en un archivo binario que fuera ejecutar la CPU. Luego ese archivo generado se guarda en la micro SD y se la inserta en la CPU, presionando el botón de "Cargar programa" que se encuentra en el circuito se inicia la carga del mismo en la memoria RAM de la CPU, y por último, habilitando la señal de "Clock" (una señal que coordina todo la electrónica) se ejecuta el programa cargado.
De este proceso se encarga el famoso microcontrolador Atmega328P o Arduino para los amigos, básicamente tomar el archivo binario y cargarlo a la memoria RAM; no hace nada más en la CPU.


## Bien, pero... ¿Qué puede hacer?
La respuesta es, no mucho, debido a que está construida con componentes electrónicos simples no se pueden hacer cosas muy complejas. Pero bueno, es una CPU sin procesador, no se le puede pedir mucho ¿no?
Pero a pesar de sus limitaciones, es capaz de ejecutar un mini juego que prueba tu rapidez con un botón. Con puntos ganados e intentos fallidos he, no cualquier jueguito simple. Además, se pueden leer sensores, controlar relevadores, leds, otros circuitos integrados y demás.


## Este es un diagrama de bloques para que entiendas un poco como funciona internamente
![image](https://user-images.githubusercontent.com/63881067/156947993-b42a4ffd-e17b-4b95-ac39-520f419b4e01.png)
![image](https://user-images.githubusercontent.com/63881067/156948033-4300fcc1-0d9f-4c0c-a472-4b054f27ada8.png)


## Y este es el diagrama eléctrico que hace que todo funcione, si lo sé, es un enredo de cables ¿no?
![image](https://user-images.githubusercontent.com/63881067/156948181-3f1eb04a-2ea2-47c6-a826-3dbbf853bf05.png)


## El resultado del diagrama anterior es el siguiente (ignoren el desorden)
![20210105_134637](https://user-images.githubusercontent.com/63881067/156948329-1508cea9-a604-4232-b6e7-7ce6b95f4907.jpg)

## Conclusión
Si no entendiste ningún diagrama, está bien no te preocupes, hasta yo que lo hice tengo que recordar lo que hacia esa parte. La idea de este proyecto es mostrar que partes esenciales intervienen en el funcionamiento un procesador, como el que ejecuto ciertas instrucciones para que puedas ver esto. En fin, este proyecto no es nada revolucionario, solo un puñado de componentes electrónicos y lucecitas de colores, pero para una persona curiosa del tema es la entrada a el mundo de la electrónica y la programación.
