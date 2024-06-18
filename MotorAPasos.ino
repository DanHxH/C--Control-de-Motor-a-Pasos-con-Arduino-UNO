#include <Stepper.h>

const int pasosPorVuelta = 2048;
Stepper motor(pasosPorVuelta, 8, 10, 9, 11);
const int angulosPorVuelta = 360; // Grados en una vuelta completa

void setup() {
  Serial.begin(9600); // Inicia la comunicación serial
  motor.setSpeed(10); // Establece la velocidad del motor
  Serial.println("Ingresa el ángulo a mover:");
}

void loop() {
  if (Serial.available() > 0) {
    int angulo = Serial.parseInt(); // Lee el ángulo desde el monitor serial
    int pasos = map(angulo, 0, angulosPorVuelta, 0, pasosPorVuelta); // Convierte el ángulo a pasos

    motor.step(pasos); // Mueve el motor el número de pasos calculado
    delay(500); // Espera un poco para evitar movimientos continuos

    Serial.print("Motor movido ");
    Serial.print(angulo);
    Serial.println(" grados.");
  }
}
