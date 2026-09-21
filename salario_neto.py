"""
Programa: Cálculo del salario neto de un empleado
Autor: Ángel Andrade
Fecha: 20/09/2026
Descripción: Solicita el salario bruto mensual, el porcentaje de
impuestos y las deducciones adicionales, y calcula el salario neto.
"""


# Constantes
PORCENTAJE_MAXIMO = 100


# Funciones
def solicitar_numero(mensaje, maximo=None):
    """
    Solicita un número mayor o igual a cero al usuario.

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el dato.
        maximo (float): Valor máximo permitido (opcional).

    Retorna:
        float: El número ingresado por el usuario.
    """
    while True:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Error: el valor no puede ser negativo.")
            elif maximo is not None and numero > maximo:
                print(f"Error: el valor no puede ser mayor que {maximo}.")
            else:
                return numero
        except ValueError:
            print("Error: ingresa un valor numérico válido.")


def calcular_impuesto(salario_bruto, porcentaje):
    """
    Calcula el impuesto a partir del salario bruto.

    Parámetros:
        salario_bruto (float): Salario bruto mensual.
        porcentaje (float): Porcentaje de impuestos (por ejemplo, 16).

    Retorna:
        float: El monto del impuesto.
    """
    return salario_bruto * (porcentaje / 100)


def calcular_salario_neto(salario_bruto, impuesto, deducciones):
    """
    Calcula el salario neto del empleado.

    Parámetros:
        salario_bruto (float): Salario bruto mensual.
        impuesto (float): Monto del impuesto.
        deducciones (float): Deducciones adicionales.

    Retorna:
        float: El salario neto.
    """
    return salario_bruto - impuesto - deducciones


# Bloque principal
if __name__ == "__main__":
    print("=== CÁLCULO DEL SALARIO NETO ===\n")

    # Entrada
    bruto = solicitar_numero("Ingresa el salario bruto mensual: $")
    porcentaje_impuestos = solicitar_numero(
        "Ingresa el porcentaje de impuestos (0-100): ", PORCENTAJE_MAXIMO
    )
    deducciones_extra = solicitar_numero(
        "Ingresa las deducciones adicionales: $"
    )

    # Proceso
    monto_impuesto = calcular_impuesto(bruto, porcentaje_impuestos)
    neto = calcular_salario_neto(bruto, monto_impuesto, deducciones_extra)

    # Salida
    print("\n--- RESUMEN ---")
    print(f"Salario bruto:           ${bruto:>12,.2f}")
    etiqueta = f"Impuesto ({porcentaje_impuestos:g}%):"
    print(f"{etiqueta:<25}${monto_impuesto:>12,.2f}")
    print(f"Deducciones adicionales: ${deducciones_extra:>12,.2f}")
    print(f"Salario neto:            ${neto:>12,.2f}")
    if neto < 0:
        print("Aviso: las deducciones son mayores que el salario disponible.")
