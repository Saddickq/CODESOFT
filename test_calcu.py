#!/usr/bin/python3
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_invalid_sign(self):
        with self.assertRaises(ValueError):
            calc = Calculator(9, '=', 3)
            result = calc.calculate()

    def test_addition(self):
        calc = Calculator(9, '+', 3)
        result = calc.calculate()
        self.assertEqual(result, 12)

        calc1 = Calculator(100, '+', -63)
        result1 = calc1.calculate()
        self.assertEqual(result1, 37)
        
        calc2 = Calculator(-7, '+', -9)
        result2 = calc2.calculate()
        self.assertEqual(result2, -16)

        
    def test_subtraction(self):
        calc = Calculator(105, '-', 45)
        result = calc.calculate()
        self.assertEqual(result, 60)
        
        calc1 = Calculator(-7, '-', -9)
        result1 = calc1.calculate()
        self.assertEqual(result1, 2)
        
        calc2 = Calculator(6, '-', -9)
        result2 = calc2.calculate()
        self.assertEqual(result2, 15)
        
        calc3 = Calculator(-7, '-', 9)
        result3 = calc3.calculate()
        self.assertEqual(result3, -16)
    
    def test_division(self):
        calc = Calculator(-7, '/', 9)
        result = calc.calculate()
        self.assertEqual(round(result, 2), -0.78)
    
        calc1 = Calculator(10, '/', 3)
        result1 = calc1.calculate()
        self.assertEqual(round(result1, 2), 3.33)
    
        calc2 = Calculator(-8, '/', 2)
        result2 = calc2.calculate()
        self.assertEqual(result2, -4)
    
        calc3 = Calculator(-16, '/', -2)
        result3 = calc3.calculate()
        self.assertEqual(result3, 8)
        
        calc4 = Calculator(0, '/', 80)
        result4 = calc4.calculate()
        self.assertEqual(result4, 0)
        
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calc = Calculator(47, '/', 0)
            result = calc.calculate()
        
    def test_multiplication(self):
        calc = Calculator(5, '*', 3)
        result = calc.calculate()
        self.assertEqual(result, 15)
        
        calc1 = Calculator(4, '*', -3)
        result1 = calc1.calculate()
        self.assertEqual(result1, -12)
        
        calc2 = Calculator(-15, '*', -3)
        result2 = calc2.calculate()
        self.assertEqual(result2, 45)


if __name__ == "__main__":
    unittest.main()