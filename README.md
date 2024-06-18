# Control de Motor a Pasos con Arduino UNO

Este repositorio contiene el código para controlar un motor a pasos utilizando un Arduino UNO y una batería. El programa permite ingresar ángulos a través del monitor serial para mover el motor a pasos en la dirección deseada.

## Características

- **Configuración de Pines**: Define y configura los pines para controlar el motor a pasos.
- **Control Preciso del Motor**: Permite ingresar un ángulo desde el monitor serial y convierte ese ángulo en pasos para mover el motor con precisión.
- **Retroalimentación Serial**: Proporciona retroalimentación a través del monitor serial sobre el movimiento realizado por el motor.

## Archivos Principales

- `setup()`: Configura la comunicación serial y establece la velocidad del motor a pasos.
- `loop()`: Lee el ángulo ingresado desde el monitor serial, lo convierte en pasos, y mueve el motor en consecuencia. Proporciona retroalimentación sobre el movimiento realizado.

## Ejecución

El programa espera a que el usuario ingrese un ángulo a través del monitor serial. Una vez ingresado, el motor a pasos se mueve el número de pasos correspondiente al ángulo especificado y se proporciona retroalimentación a través del monitor serial.

## Instalación y Uso

1. Clona este repositorio: `git clone https://github.com/DanHxH/C--Control-de-Motor-a-Pasos-con-Arduino-UNO.git`
2. Abre el archivo `.ino` en el IDE de Arduino.
3. Conecta tu Arduino UNO y sube el programa.
4. Conecta el motor a pasos según la configuración de pines indicada.
5. Abre el monitor serial, ingresa un ángulo y observa cómo se mueve el motor.

## Requisitos

- Arduino UNO
- Motor a pasos (28BYJ-48 o similar)
- Driver de motor a pasos (ULN2003 o similar)
- Batería para alimentación del motor
- Cables para conexiones

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cualquier cambio o mejora.
