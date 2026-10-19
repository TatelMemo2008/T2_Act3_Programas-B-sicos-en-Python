"""
Programa: Salario neto de un empleado
Autor: Ángel Guillermo Andrade Palacios
Fecha: 17 de octubre de 2026
Descripción: Pide el salario bruto mensual, el porcentaje de
impuestos y las deducciones adicionales, y calcula el salario neto.
"""


def calcular_impuesto(salario_bruto, porcentaje):
    """Calcula cuánto se paga de impuesto."""
    return salario_bruto * (porcentaje / 100)


if __name__ == "__main__":
    # Entrada de datos
    salario_bruto = float(input("Salario bruto mensual: $"))
    porcentaje = float(input("Porcentaje de impuestos: "))
    deducciones = float(input("Deducciones adicionales: $"))

    # Proceso
    impuesto = calcular_impuesto(salario_bruto, porcentaje)
    salario_neto = salario_bruto - impuesto - deducciones

    # Salida
    print(f"Impuesto: ${impuesto:.2f}")
    print(f"Deducciones adicionales: ${deducciones:.2f}")
    print(f"Salario neto: ${salario_neto:.2f}")
