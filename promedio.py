"""
Programa: Promedio de tres números
Autor: Ángel Guillermo Andrade Palacios
Fecha: 17 de octubre de 2026
Descripción: Pide tres números, calcula su promedio y lo muestra
con dos decimales.
"""

# Constantes
CANTIDAD_NUMEROS = 3


def calcular_promedio(num1, num2, num3):
    """Calcula el promedio de tres números."""
    suma = num1 + num2 + num3
    return suma / CANTIDAD_NUMEROS


if __name__ == "__main__":
    # Entrada de datos
    num1 = float(input("Escribe el primer número: "))
    num2 = float(input("Escribe el segundo número: "))
    num3 = float(input("Escribe el tercer número: "))

    # Proceso
    promedio = calcular_promedio(num1, num2, num3)

    # Salida
    print(f"El promedio de {num1:g}, {num2:g} y {num3:g} es: {promedio:.2f}")
