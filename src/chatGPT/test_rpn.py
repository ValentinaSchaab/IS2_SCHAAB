import unittest
from rpn import evaluar_rpn, RPNError


class TestRPN(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(evaluar_rpn("3 4 +"), 7)

    def test_expresion_compleja(self):
        self.assertEqual(evaluar_rpn("5 1 2 + 4 * + 3 -"), 14)

    def test_division_por_cero(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 0 /")

    def test_error_pila(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 +")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("abc")

    def test_10x(self):
        self.assertEqual(evaluar_rpn("2 10x"), 100)

    def test_dup(self):
        self.assertEqual(evaluar_rpn("3 dup +"), 6)

    def test_swap(self):
        self.assertEqual(evaluar_rpn("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(evaluar_rpn("3 4 drop"), 3)

    def test_error_dup(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("dup")

    def test_error_swap(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 swap")

    def test_error_drop(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("drop")

        # 🔹 FUNCIONES
    def test_sqrt(self):
        self.assertEqual(evaluar_rpn("9 sqrt"), 3)

    def test_log(self):
        self.assertEqual(evaluar_rpn("100 log"), 2)

    def test_ln(self):
        self.assertAlmostEqual(evaluar_rpn("1 ln"), 0, places=5)

    def test_ex(self):
        self.assertAlmostEqual(evaluar_rpn("1 ex"), 2.71828, places=5)

    def test_inverso(self):
        self.assertEqual(evaluar_rpn("4 1/x"), 0.25)

    # 🔹 TRIGONOMETRÍA
    def test_sin(self):
        self.assertAlmostEqual(evaluar_rpn("90 sin"), 1, places=5)

    def test_cos(self):
        self.assertAlmostEqual(evaluar_rpn("0 cos"), 1, places=5)

    def test_atg(self):
        self.assertAlmostEqual(evaluar_rpn("1 atg"), 45, places=5)

    # 🔹 CONSTANTES
    def test_pi(self):
        self.assertAlmostEqual(evaluar_rpn("p"), 3.141592, places=5)

    def test_e(self):
        self.assertAlmostEqual(evaluar_rpn("e"), 2.71828, places=5)

    # 🔹 MEMORIA
    def test_sto_rcl(self):
        self.assertEqual(evaluar_rpn("5 STO 01 RCL 01"), 5)

    # 🔴 ERRORES IMPORTANTES
    def test_error_log_negativo(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("-1 log")

    def test_error_sqrt_negativo(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("-9 sqrt")

    def test_error_division_cero(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("5 0 /")

        # 🔹 MÁS FUNCIONES
    def test_chs(self):
        self.assertEqual(evaluar_rpn("5 chs"), -5)

    def test_tg(self):
        self.assertAlmostEqual(evaluar_rpn("45 tg"), 1, places=5)

    def test_asin(self):
        self.assertAlmostEqual(evaluar_rpn("1 asin"), 90, places=5)

    def test_acos(self):
        self.assertAlmostEqual(evaluar_rpn("0 acos"), 90, places=5)

    # 🔹 CLEAR BIEN
    def test_clear_error(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 4 clear")

    # 🔹 MEMORIA ERROR
    def test_error_sto_sin_indice(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("5 STO")

    def test_error_yx(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("2 yx")

    def test_error_rcl_sin_indice(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("RCL")

if __name__ == "__main__":
    unittest.main()