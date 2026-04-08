from machine import Pin
import time

print("Sistema de Control de Válvula - Iniciando")

# Declarar Pines
PIN_LED_VERDE = 16
PIN_LED_ROJO = 4
PIN_BOTON1 = 11
PIN_SALIDA_VLV_TRANSISTOR = 42

# Aquí declarar Tipo de PIN -> Salida LED
led_verde = Pin(PIN_LED_VERDE, Pin.OUT)
led_rojo = Pin(PIN_LED_ROJO, Pin.OUT)

# Aquí declarar Tipo de PIN -> Botón PULL-UP
boton = Pin(PIN_BOTON1, Pin.IN, Pin.PULL_UP)

# Aquí declarar Tipo de PIN -> Salida Transistor
pin_transistor = Pin(PIN_SALIDA_VLV_TRANSISTOR, Pin.OUT)

# Variables de estado:
boton_actual = 1
boton_anterior = 1
orden_activacion = 0  # 0 = Válvula cerrada, 1 = Válvula abierta

# Loop principal del programa
print("Entrando en loop principal")
while True:
    print(boton.value())
    # Aquí leer estado actual del botón, actualizar valor antiguo, e incorporar detección de flanco
    boton_anterior = boton_actual
    boton_actual = boton.value()
    flanco_descendente = boton_anterior and not boton_actual

    # Flanco de subida: Toggle Válvula (Abrir/Cerrar)
    if flanco_descendente:
        orden_activacion = 1 - orden_activacion
        pin_transistor.value(orden_activacion)
        print("Botón presionado. Válvula toggleada a:", orden_activacion)

    # LED verde = Válvula activa:
    led_verde.value(orden_activacion)

    # LED rojo = Voltage en la salida del transistor:
    led_rojo.value(pin_transistor.value())

    # Pequeña pausa para evitar uso excesivo de CPU
    time.sleep(0.001)

### FIN DEL LOOP ###