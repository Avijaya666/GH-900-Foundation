"""Unit tests for the calculator engine."""
import unittest
import sys
from pathlib import Path

# Add parent directory to path so we can import core module
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import Calculator


class TestCalculatorBasicOperations(unittest.TestCase):
    """Test basic arithmetic operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
    
    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=5)
        self.assertEqual(self.calc.divide(0, 5), 0)
    
    def test_division_by_zero(self):
        """Test that division by zero raises an error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
        self.assertEqual(self.calc.power(2, -1), 0.5)
    
    def test_square_root(self):
        """Test square root operation."""
        self.assertEqual(self.calc.square_root(16), 4)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertAlmostEqual(self.calc.square_root(2), 1.414213, places=5)
    
    def test_square_root_negative(self):
        """Test that square root of negative number raises an error."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_percentage(self):
        """Test percentage operation."""
        self.assertEqual(self.calc.percentage(100, 50), 50)
        self.assertEqual(self.calc.percentage(200, 25), 50)
        self.assertEqual(self.calc.percentage(100, 0), 0)
        self.assertEqual(self.calc.percentage(50, 100), 50)
    
    def test_reciprocal(self):
        """Test reciprocal operation."""
        self.assertEqual(self.calc.reciprocal(2), 0.5)
        self.assertEqual(self.calc.reciprocal(4), 0.25)
        self.assertEqual(self.calc.reciprocal(1), 1)
        self.assertAlmostEqual(self.calc.reciprocal(3), 0.333333, places=5)
    
    def test_reciprocal_zero(self):
        """Test that reciprocal of zero raises an error."""
        with self.assertRaises(ValueError):
            self.calc.reciprocal(0)
    
    def test_negate(self):
        """Test negate operation."""
        self.assertEqual(self.calc.negate(5), -5)
        self.assertEqual(self.calc.negate(-5), 5)
        self.assertEqual(self.calc.negate(0), 0)
        self.assertEqual(self.calc.negate(3.5), -3.5)


class TestCalculatorGenericCalculate(unittest.TestCase):
    """Test the generic calculate method."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_calculate_addition(self):
        """Test calculate method with addition."""
        self.assertEqual(self.calc.calculate(5, '+', 3), 8)
    
    def test_calculate_subtraction(self):
        """Test calculate method with subtraction."""
        self.assertEqual(self.calc.calculate(5, '-', 3), 2)
    
    def test_calculate_multiplication(self):
        """Test calculate method with multiplication."""
        self.assertEqual(self.calc.calculate(5, '*', 3), 15)
    
    def test_calculate_division(self):
        """Test calculate method with division."""
        self.assertEqual(self.calc.calculate(10, '/', 2), 5)
    
    def test_calculate_power(self):
        """Test calculate method with power."""
        self.assertEqual(self.calc.calculate(2, '**', 3), 8)
    
    def test_calculate_invalid_operator(self):
        """Test that invalid operator raises an error."""
        with self.assertRaises(ValueError):
            self.calc.calculate(5, '%', 3)


class TestCalculatorReset(unittest.TestCase):
    """Test calculator reset functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_reset(self):
        """Test that reset clears calculator state."""
        self.calc.result = 42
        self.calc.previous_result = 100
        self.calc.operation = '+'
        self.calc.should_reset_display = True
        
        self.calc.reset()
        
        self.assertEqual(self.calc.result, 0)
        self.assertEqual(self.calc.previous_result, 0)
        self.assertIsNone(self.calc.operation)
        self.assertFalse(self.calc.should_reset_display)


if __name__ == '__main__':
    unittest.main()
