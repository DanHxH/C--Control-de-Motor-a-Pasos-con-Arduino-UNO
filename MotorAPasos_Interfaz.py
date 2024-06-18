import tkinter as tk
from tkinter import messagebox
import serial.tools.list_ports
import serial
import time

class MotorControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Motor Control")

        self.serial_port = self.detect_serial_port()
        if self.serial_port is None:
            messagebox.showerror("Error", "No se encontró un puerto COM disponible.")
            self.root.quit()  # Cerrar la aplicación si no se detecta un puerto COM
            return

        self.ser = serial.Serial(self.serial_port, 9600, timeout=1)
        time.sleep(2)  # Esperar a que el puerto serial esté listo

        self.angle_var = tk.StringVar()

        self.create_widgets()

    def detect_serial_port(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            return port.device
        return None

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Ingrese el ángulo de giro:").pack(side=tk.LEFT)
        angle_entry = tk.Entry(frame, textvariable=self.angle_var)
        angle_entry.pack(side=tk.LEFT)

        send_button = tk.Button(frame, text="Enviar", command=self.send_angle)
        send_button.pack(side=tk.LEFT)

        self.root.bind("<Return>", lambda event: self.send_angle())

    def send_angle(self):
        try:
            angle = int(self.angle_var.get())
            self.ser.write(f"{angle}\n".encode())
            self.angle_var.set("")  # Limpiar la caja de texto después de enviar
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

    def on_closing(self):
        self.ser.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MotorControlApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
