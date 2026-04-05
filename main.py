from machine import Pin
import time

# Declarar Pines
PIN_LED_VERDE = 16
PIN_LED_ROJO = 4
PIN_BOTON1 = 11
PIN_SALIDA_VLV_TRANSISTOR = 38

# Aquí declarar Tipo de PIN -> Salida LED
led_verde = Pin(PIN_LED_VERDE, Pin.OUT)
led_rojo = Pin(PIN_LED_ROJO, Pin.OUT)

# Aquí declarar Tipo de PIN -> Botón PULL-UP
boton = Pin(PIN_BOTON1, Pin.IN, Pin.PULL_UP)

# Aquí declarar Tipo de PIN -> Salida Transistor
salida_transistor = Pin(PIN_SALIDA_VLV_TRANSISTOR, Pin.OUT)

# Variables de estado del botón 1:
boton_actual = 0
boton_anterior = 0

# Loop principal del programa
while True:
    # Aquí leer estado actual del botón, actualizar valor antiguo, e incorporar detección de flanco
    boton_anterior = boton_actual
    boton_actual = boton.value()
    flanco_ascendente = boton_actual and not boton_anterior

    # Flanco de subida: Abrir/Cerrar Válvula
    if flanco_ascendente:
        x1 = salida_transistor.value()
        salida_transistor.value(1-x1)

    # LED verde = Válvula activa:
    x2 = salida_transistor.value()
    led_verde.value(x2)

    # LED rojo = Nivel bajo de agua (será incorporado a futuro con un sensor de nivel puntual)
    pass

    # Pequeña pausa para evitar uso excesivo de CPU
    time.sleep(0.2)

### FIN DEL LOOP ###