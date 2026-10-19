"""
Programa: Índice de Masa Corporal (IMC)
Autor: Ángel Guillermo Andrade Palacios
Fecha: 17 de octubre de 2026
Descripción: Pide el peso en kilogramos y la altura en metros, y
calcula el IMC con la fórmula peso / (altura * altura).
"""


def calcular_imc(peso, altura):
    """Calcula el IMC a partir del peso y la altura."""
    return peso / (altura * altura)


if __name__ == "__main__":
    # Entrada de datos
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en metros: "))

    # Si la altura fuera 0 la división daría error, por eso reviso antes
    if peso > 0 and altura > 0:
        # Proceso
        imc = calcular_imc(peso, altura)

        # Salida
        print(f"Tu IMC es: {imc:.2f}")
    else:
        print("El peso y la altura deben ser mayores que cero")
