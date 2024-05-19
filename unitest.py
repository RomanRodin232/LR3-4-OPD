import unittest
from reshenie import reshenie

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        result = reshenie(0, 0, 0)
        self.assertEqual(result, "Уравнение верно для любого значения X (x ∈ R)")

    def test_2(self):
        result = reshenie(0, 0, -2)
        self.assertEqual(result, "Уравнение ложно для любого значения X (x ∈ Ø)")

    def test_3(self):
        result = reshenie(0, 2, 0)
        self.assertEqual(result, "Уравнение имеет 1 корень X = 0")

    def test_4(self):
        result = reshenie(0, -4, 4)
        self.assertEqual(result, f"Уравнение имеет 1 корень X = {1.0}")

    def test_5(self):
        result = reshenie(10, 0, 0)
        self.assertEqual(result, "Уравнение имеет 2 повторяющихся кореня X = 0")

    def test_6(self):
        result = reshenie(10, 0, 10)
        self.assertEqual(result, "Действительных корней нет (x ∉ R)")

    def test_7(self):
        result = reshenie(10, 0, -10)
        self.assertEqual(result, f"Данное уравение имеет 2 кореня X1 = {-1.0}, X2 = {1.0}")

    def test_8(self):
        result = reshenie(10, 10, 0)
        self.assertEqual(result, f"Данное уравение имеет 2 кореня X1 = {0.0}, X2 = {-1.0}")

    def test_9(self):
        result = reshenie(1, -5, 4)
        self.assertEqual(result, f"Данное уравение имеет 2 кореня X1 = {1.0}, X2 = {4.0}")

    def test_10(self):
        result = reshenie(2, 4, 2)
        self.assertEqual(result, f"Данное уравение имеет 1 корень X1 = {-1.0}")

    def test_11(self):
        result = reshenie(10, 10, 20)
        self.assertEqual(result, "Действительных корней нет (x ∉ R)")

if __name__ == '__main__':
    unittest.main()