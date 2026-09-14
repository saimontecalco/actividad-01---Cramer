"""
Módulo de funciones auxiliares para la Regla de Cramer (sistema 2x2).

Asignatura: Ciencia de Datos
Cuatrimestre: 7mo
Alumno: [Saimon Josue Tecalco Martinez]
Matrícula: [2403230384]
Fecha: [12/09/2026]
"""
def calcular_determinante(a1, b1, a2, b2):
    """Calcula el determinante de una matriz 2x2."""
    return (a1 * b2) - (a2 * b1)


def calcular_delta(a1, b1, a2, b2):
    """Calcula el determinante principal del sistema (delta)."""
    return calcular_determinante(a1, b1, a2, b2)


def calcular_delta_x(b1, c1, b2, c2):
    """Calcula el determinante de X (delta_x)."""
    return calcular_determinante(c1, b1, c2, b2)


def calcular_delta_y(a1, c1, a2, c2):
    """Calcula el determinante de Y (delta_y)."""
    return calcular_determinante(a1, c1, a2, c2)


def calcular_soluciones(delta, delta_x, delta_y):
    """Calcula los valores finales de x e y. Devuelve (None, None) si delta es 0."""
    if delta == 0:
        return None, None
    x = delta_x / delta
    y = delta_y / delta
    return x, y


def sistema_completo(delta):
    """Verifica si el sistema tiene solución única (delta distinto de 0)."""
    return delta != 0