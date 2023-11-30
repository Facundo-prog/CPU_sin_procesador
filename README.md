# CPU sin procesador V6
Esta CPU funciona sin un procesador que ejecute las instrucciones, sino que todo el circuito se comporta como un procesador, más bien es un microprocesador en formato grande.

## Compilacion de un programa ASM (ensamblador) a binario
* Ejecutar el archivo "instructions_generator.py" que generará un archivo control.asm (solo se requiere generarlo una vez)
* Ejecutar el archivo "compiler.py" y seleccionar el proyecto que desea compilar en la terminal
* Copiar los archivos generados "control.asm" y "program.asm" a una MicroSD destinada a conectarse a la CPU

## Ejecución de un programa
* Encender la CPU
* Verificar que el led de STATUS parpadee cada 1 segundo (si es mas rapido es porque hay un error en la MicroSD)
* Presionar el boton PROG (programar), el led de STATUS quedara encendido, esperar a que el led empieze a parpadear cada 1 segundo nuevamente (indicando que finalizó la programación)
* Mantener el boton de RESET mientras se habilita la señal de CLOCK. Soltar el boton de RESET para que se ejecute el programa

## Partes que la componen
* Memoria RAM donde se almacenan las instrucciones que tiene que ejecutar y los datos con los cuales tiene que trabajar
* Un circuito de control que orquesta a todos los componentes electrónicos y dicta a qué velocidad funciona el conjunto
* Sistema de carga del programa, en donde mediante una tarjeta MicroSD se guardan las instrucciones y datos en formato binario
* Modulo ALU que se encarga de realizar las operaciones aritmeticas y logicas, además de almacenar datos en los registros
* Entradas y salidas de datos para interactuar con hardware externo.

## Y... ¿Cómo ejecuta el programa?
Para ello se desarrolló un compilador en Python (también llamado analizador léxico) que es capaz de interpretar instrucciones simples (lenguaje ensamblador) y convertirlas en un archivo binario que pueda ejecutar la CPU. Luego ese archivo generado se guarda en la MicroSD y se la inserta en la CPU, presionando el botón de "PROG" se inicia la carga del programa en la memoria RAM de la CPU, y por último, habilitando la señal de "CLOCK" (una señal que coordina todo la electrónica) se ejecuta el programa cargado.
Este proceso lo realiza el famoso microcontrolador Atmega328P o Arduino para los amigos, básicamente tomar el archivo binario y cargarlo a la memoria RAM; no interviene en ningún otro proceso en la CPU.


## Bien, pero... ¿Qué puede hacer?
La respuesta es, no mucho, debido a que está construida con componentes electrónicos simples no se pueden hacer cosas muy complejas. El objetivo no es que sea potente, si no que sea lo mas simple posible para que cualquiera pueda entender que partes intervienen en su funcionamiento.
Pero a pesar de sus limitaciones, es capas de ejecutar programas interesantes. Podemos leer sensores, controlar relevadores, leds, otros circuitos integrados y demás.


## Este es un diagrama de bloques para que entiendas un poco como funciona internamente
![image](https://user-images.githubusercontent.com/63881067/156947993-b42a4ffd-e17b-4b95-ac39-520f419b4e01.png)
![image](https://user-images.githubusercontent.com/63881067/156948033-4300fcc1-0d9f-4c0c-a472-4b054f27ada8.png)


## Y este es el diagrama eléctrico que hace que todo funcione, si lo sé, es un enredo de cables ¿no?
![image](https://user-images.githubusercontent.com/63881067/156948181-3f1eb04a-2ea2-47c6-a826-3dbbf853bf05.png)


## El resultado del diagrama anterior es el siguiente (ignoren el desorden)
![image](https://user-images.githubusercontent.com/63881067/156948329-1508cea9-a604-4232-b6e7-7ce6b95f4907.jpg)

## Conclusión
Si no entendiste ningún diagrama, está bien no te preocupes, hasta yo que lo hice tengo que recordar lo que hacia esacada parte. La idea de este proyecto es mostrar que partes esenciales intervienen en el funcionamiento un microprocesador, como el que ejecuto ciertas instrucciones para que puedas ver esto. En fin, este proyecto no es nada revolucionario, solo demuestra de forma mas simple el funcionamiento de una PC comercial (mucho menos potente).
