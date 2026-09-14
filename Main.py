"""
Programa principal: Resolución de sistemas de ecuaciones lineales 2x2
mediante la Regla de Cramer.

Asignatura: Ciencia de Datos
Cuatrimestre: 7mo
Alumno: [Saimon Josue Tecalco Martinez]
Matrícula: [2403230384]
Fecha: [12/09/2026]
"""

from Funciones import (
    calcular_delta,
    calcular_delta_x,
    calcular_delta_y,
    calcular_soluciones,
)

ecuacion_a = {"coef_x": None, "coef_y": None, "resultado": None}
ecuacion_b = {"coef_x": None, "coef_y": None, "resultado": None}


def mostrar_menu():
    """Imprime en consola las opciones del menú principal."""
    print("\n— MENU PRINCIPAL —")
    print("1. Capturar ecuación A")
    print("2. Capturar ecuación B")
    print("3. Mostrar soluciones")
    print("4. Salir")


def solicitar_numero(mensaje):
    """Solicita un número al usuario, validando que sea numérico."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor ingresa un valor numérico.")


def capturar_ecuacion(nombre_ecuacion, ecuacion):
    """Solicita los tres valores de una ecuación y los guarda."""
    print(f"\nCaptura de la ecuación {nombre_ecuacion}")
    ecuacion["coef_x"] = solicitar_numero("Captura coeficiente de X: ")
    ecuacion["coef_y"] = solicitar_numero("Captura coeficiente de Y: ")
    ecuacion["resultado"] = solicitar_numero("Captura resultado de la ecuación: ")
    print(f"Ecuación {nombre_ecuacion} capturada correctamente.")


def mostrar_soluciones(ecuacion_a, ecuacion_b):
    """Calcula y despliega Delta, Delta X, Delta Y, X y Y."""
    if None in ecuacion_a.values() or None in ecuacion_b.values():
        print("\nDebes capturar ambas ecuaciones antes de mostrar soluciones.")
        return

    a1, b1, c1 = ecuacion_a["coef_x"], ecuacion_a["coef_y"], ecuacion_a["resultado"]
    a2, b2, c2 = ecuacion_b["coef_x"], ecuacion_b["coef_y"], ecuacion_b["resultado"]

    delta = calcular_delta(a1, b1, a2, b2)
    delta_x = calcular_delta_x(b1, c1, b2, c2)
    delta_y = calcular_delta_y(a1, c1, a2, c2)

    print("\n--- RESULTADOS ---")
    print(f"Delta   = {delta}")
    print(f"Delta X = {delta_x}")
    print(f"Delta Y = {delta_y}")

    if delta == 0:
        print("El sistema no tiene solución única (Delta = 0).")
        return

    x, y = calcular_soluciones(delta, delta_x, delta_y)
    print(f"X = {x}")
    print(f"Y = {y}")


def main():
    """Controla el ciclo principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            capturar_ecuacion("A", ecuacion_a)
        elif opcion == "2":
            capturar_ecuacion("B", ecuacion_b)
        elif opcion == "3":
            mostrar_soluciones(ecuacion_a, ecuacion_b)
        elif opcion == "4":
            print("\nFinalizando el programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()