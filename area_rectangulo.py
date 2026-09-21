"""
Programa: Cálculo del área de un rectángulo
Autor: Ángel Andrade
Fecha: 20/09/2026
Descripción: Solicita la base y la altura de un rectángulo y calcula
su área con la fórmula base × altura.
"""


# Funciones
def solicitar_numero(mensaje):
    """
    Solicita un número positivo al usuario.

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el dato.

    Retorna:
        float: El número ingresado por el usuario.
    """
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            print("Error: el valor debe ser mayor que cero.")
        except ValueError:
            print("Error: ingresa un valor numérico válido.")


def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.

    Parámetros:
        base (float): Longitud de la base.
        altura (float): Longitud de la altura.

    Retorna:
        float: El área del rectángulo.
    """
    return base * altura


# Bloque principal
if __name__ == "__main__":
    print("=== ÁREA DE UN RECTÁNGULO ===\n")

    # Entrada
    base = solicitar_numero("Ingresa la base del rectángulo: ")
    altura = solicitar_numero("Ingresa la altura del rectángulo: ")

    # Proceso
    area = calcular_area(base, altura)

    # Salida
    print(f"\nBase: {base:.2f}")
    print(f"Altura: {altura:.2f}")
    print(f"El área del rectángulo es: {area:.2f}")
