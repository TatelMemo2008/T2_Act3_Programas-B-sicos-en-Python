8"""
Programa: Cálculo del promedio de tres números
Autor: Ángel Andrade
Fecha: 20/09/2026
Descripción: Solicita tres números al usuario y calcula su promedio
sumándolos y dividiendo el resultado entre tres.
"""


# Constantes
CANTIDAD_NUMEROS = 3


# Funciones
def solicitar_numero(mensaje):
    """
    Solicita un número al usuario (entero o decimal).

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el dato.

    Retorna:
        float: El número ingresado por el usuario.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingresa un valor numérico válido.")


def calcular_promedio(num1, num2, num3):
    """
    Calcula el promedio de tres números.

    Parámetros:
        num1 (float): Primer número.
        num2 (float): Segundo número.
        num3 (float): Tercer número.

    Retorna:
        float: El promedio de los tres números.
    """
    return (num1 + num2 + num3) / CANTIDAD_NUMEROS


# Bloque principal
if __name__ == "__main__":
    print("=== PROMEDIO DE TRES NÚMEROS ===\n")

    # Entrada
    numero1 = solicitar_numero("Ingresa el primer número: ")
    numero2 = solicitar_numero("Ingresa el segundo número: ")
    numero3 = solicitar_numero("Ingresa el tercer número: ")

    # Proceso
    promedio = calcular_promedio(numero1, numero2, numero3)

    # Salida
    print(f"\nNúmeros ingresados: {numero1}, {numero2}, {numero3}")
    print(f"El promedio es: {promedio:.2f}")
