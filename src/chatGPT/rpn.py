"""
Calculadora RPN (Reverse Polish Notation).
Soporta operaciones matemáticas, funciones, pila y memoria.
Incluye manejo de errores mediante RPNError.
"""

import math
import sys


class RPNError(Exception):
    """Excepción personalizada para errores en la calculadora RPN."""

    pass


def check_pila(pila, n=1):
    """Verifica que la pila tenga al menos n elementos."""
    if len(pila) < n:
        raise RPNError("Pila insuficiente")


def manejar_pila(t, pila):
    """Ejecuta operaciones de pila."""
    if t == "dup":
        check_pila(pila)
        pila.append(pila[-1])

    elif t == "swap":
        check_pila(pila, 2)
        pila[-1], pila[-2] = pila[-2], pila[-1]

    elif t == "drop":
        check_pila(pila)
        pila.pop()

    elif t == "clear":
        pila.clear()


def aplicar_funcion(dic, t, pila):
    """Aplica una función matemática o trigonométrica."""
    check_pila(pila)
    pila.append(dic[t](pila.pop()))


def evaluar_rpn(expresion):
    """Evalúa una expresión en notación RPN y devuelve el resultado."""
    pila = []
    memorias = [0] * 10
    tokens = expresion.split()

    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: (
            a / b
            if b != 0
            else (_ for _ in ()).throw(RPNError("División por cero"))
        ),
    }

    funciones = {
        "sqrt": (
            lambda x: math.sqrt(x)
            if x >= 0
            else (_ for _ in ()).throw(RPNError("Raíz negativa"))
        ),
        "log": (
            lambda x: math.log10(x)
            if x > 0
            else (_ for _ in ()).throw(RPNError("Log inválido"))
        ),
        "ln": (
            lambda x: math.log(x)
            if x > 0
            else (_ for _ in ()).throw(RPNError("Log inválido"))
        ),
        "ex": lambda x: math.exp(x),
        "10x": lambda x: 10**x,
        "1/x": (
            lambda x: 1 / x
            if x != 0
            else (_ for _ in ()).throw(RPNError("División por cero"))
        ),
        "chs": lambda x: -x,
    }

    trig = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tg": lambda x: math.tan(math.radians(x)),
        "asin": lambda x: math.degrees(math.asin(x)),
        "acos": lambda x: math.degrees(math.acos(x)),
        "atg": lambda x: math.degrees(math.atan(x)),
    }

    const = {
        "p": math.pi,
        "e": math.e,
        "j": (1 + 5**0.5) / 2,
    }

    i = 0
    while i < len(tokens):
        t = tokens[i]

        try:
            pila.append(float(t))

        except ValueError as exc:

            if t in const:
                pila.append(const[t])

            elif t in ["dup", "swap", "drop", "clear"]:
                manejar_pila(t, pila)

            elif t in funciones:
                aplicar_funcion(funciones, t, pila)

            elif t in trig:
                aplicar_funcion(trig, t, pila)

            elif t == "yx":
                check_pila(pila, 2)
                b, a = pila.pop(), pila.pop()
                pila.append(a**b)

            elif t in ops:
                check_pila(pila, 2)
                b, a = pila.pop(), pila.pop()
                pila.append(ops[t](a, b))

            elif t == "STO":
                if i + 1 >= len(tokens):
                    raise RPNError("Falta índice de memoria para STO") from None

                if not tokens[i + 1].isdigit():
                    raise RPNError("Índice inválido para STO") from None

                idx = int(tokens[i + 1])
                if idx < 0 or idx > 9:
                    raise RPNError("Memoria inválida") from None

                check_pila(pila)
                memorias[idx] = pila.pop()
                i += 1

            elif t == "RCL":
                if i + 1 >= len(tokens):
                    raise RPNError("Falta índice de memoria para RCL") from None

                if not tokens[i + 1].isdigit():
                    raise RPNError("Índice inválido para RCL") from None

                idx = int(tokens[i + 1])
                if idx < 0 or idx > 9:
                    raise RPNError("Memoria inválida") from None

                pila.append(memorias[idx])
                i += 1

            else:
                raise RPNError(f"Token inválido: {t}") from exc

        i += 1

    if len(pila) != 1:
        raise RPNError("Resultado inválido")

    return pila[0]


def main():
    """Punto de entrada del programa."""
    try:
        expr = (
            " ".join(sys.argv[1:])
            if len(sys.argv) > 1
            else input("Ingrese expresión RPN: ")
        )
        print("Resultado:", round(evaluar_rpn(expr), 6))
    except RPNError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()