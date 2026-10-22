"""
Programa: Área de un rectángulo
Autor: Ángel Guillermo Andrade Palacios
Fecha: 17 de octubre de 2026
Descripción: Pide el largo y el ancho de un rectángulo y muestra
su área.
"""
 
 
def calcular_area(largo, ancho):
    """Calcula el área de un rectángulo."""
    return largo * ancho
 
 
if __name__ == "__main__":
    # Entrada de datos
    largo = float(input("Largo del rectángulo en cm: "))
    ancho = float(input("Ancho del rectángulo en cm: "))
 
    #Si el largo o el ancho fueran 0 la multiplicación daría 0, por eso reviso antes
    if largo > 0 and ancho > 0:
        # Proceso
        area = calcular_area(largo, ancho)

        # Salida
        print(f"El área del rectángulo es: {area:.2f} cm²")
    else:
        print("El largo y el ancho deben ser mayores que cero")
     
