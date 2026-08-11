import unittest

from calculator import evaluate_expression


class CalculatorTests(unittest.TestCase):
    def test_basic_arithmetic(self):
        self.assertEqual(evaluate_expression("2 + 3"), 5)
        self.assertEqual(evaluate_expression("7 - 4"), 3)
        self.assertEqual(evaluate_expression("6 * 7"), 42)
        self.assertEqual(evaluate_expression("8 / 2"), 4)

    def test_precedence_and_parentheses(self):
        self.assertEqual(evaluate_expression("2 + 3 * 4"), 14)
        self.assertEqual(evaluate_expression("(2 + 3) * 4"), 20)

    def test_negative_and_decimal_values(self):
        self.assertEqual(evaluate_expression("-5 + 3"), -2)
        self.assertEqual(evaluate_expression("2.5 + 1.5"), 4.0)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            evaluate_expression("2 +")


if __name__ == "__main__":
    unittest.main()
