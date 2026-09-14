"""
Programa principal: Resolución de sistemas de ecuaciones lineales 2x2
mediante la Regla de Cramer.

Asignatura: Ciencia de Datos
Cuatrimestre: 7mo
Alumno: [Saimon Josue Tecalco Martinez]
Matrícula: [2403230384]
Fecha: [12/09/2026]
"""

ecuacion_a = {"coef_x": None, "coef_y": None, "resultado": None}
ecuacion_b = {"coef_x": None, "coef_y": None, "resultado": None}


def mostrar_menu():
    """Imprime en consola las opciones del menú principal."""
    print("\n— MENU PRINCIPAL —")
    print("1. Capturar ecuación A")
    print("2. Capturar ecuación B")
    print("3. Mostrar soluciones")
    print("4. Salir")


def main():
    """Controla el ciclo principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "4":
            print("\nFinalizando el programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida o aún no implementada.")


if __name__ == "__main__":
    main()

