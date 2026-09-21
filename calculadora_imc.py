"""
Programa: Calculadora de IMC (Índice de Masa Corporal)
Autor: Ángel Andrade
Fecha: 20/09/2026
Descripción: Solicita el peso y la altura del usuario, calcula el IMC
y muestra la clasificación según la Organización Mundial de la Salud.
"""


# Constantes
CLASIFICACIONES = [
    (18.5, "Bajo peso"),
    (25.0, "Normal"),
    (30.0, "Sobrepeso"),
    (float("inf"), "Obesidad"),
]


# Funciones
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal.

    Parámetros:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.

    Retorna:
        float: El IMC calculado.
    """
    return peso / (altura * altura)


def clasificar_imc(imc):
    """
    Clasifica el IMC según los rangos de la OMS.

    Parámetros:
        imc (float): El valor del IMC.

    Retorna:
        str: La clasificación correspondiente.
    """
    for limite, clasificacion in CLASIFICACIONES:
        if imc < limite:
            return clasificacion
    return "Obesidad"


def solicitar_datos():
    """
    Solicita al usuario su peso y altura, validando que sean positivos.

    Retorna:
        tuple: (peso, altura) como floats.
    """
    while True:
        try:
            peso = float(input("Ingresa tu peso en kg: "))
            altura = float(input("Ingresa tu altura en metros: "))
            if peso > 0 and altura > 0:
                return peso, altura
            print("Error: el peso y la altura deben ser positivos.")
        except ValueError:
            print("Error: ingresa valores numéricos válidos.")


# Bloque principal
if __name__ == "__main__":
    print("=== CALCULADORA DE IMC ===")
    print("Calcula tu Índice de Masa Corporal y su clasificación.\n")

    # Entrada
    peso_usuario, altura_usuario = solicitar_datos()

    # Proceso
    imc_usuario = calcular_imc(peso_usuario, altura_usuario)
    clasificacion_usuario = clasificar_imc(imc_usuario)

    # Salida
    print(f"\nTu IMC es: {imc_usuario:.2f}")
    print(f"Clasificación: {clasificacion_usuario}")
    print("\n¡Gracias por usar la calculadora!")
