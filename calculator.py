"""
Windows Calculator Application - Main Entry Point
Phase 1: Core Calculator Logic
"""

from core import Calculator


def demonstrate_calculator():
    """Demonstrate basic calculator operations."""
    calc = Calculator()
    
    print("=" * 50)
    print("Windows Calculator Application - Phase 1")
    print("Core Arithmetic Operations Demo")
    print("=" * 50)
    
    # Basic operations
    print("\n--- Basic Arithmetic Operations ---")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"7 * 6 = {calc.multiply(7, 6)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
    
    # Advanced operations
    print("\n--- Advanced Operations ---")
    print(f"2 ^ 8 (power) = {calc.power(2, 8)}")
    print(f"√16 (square root) = {calc.square_root(16)}")
    print(f"25% of 200 = {calc.percentage(200, 25)}")
    print(f"1/8 (reciprocal) = {calc.reciprocal(8)}")
    print(f"-(-42) (negate) = {calc.negate(-42)}")
    
    # Generic calculate method
    print("\n--- Generic Calculate Method ---")
    result = calc.calculate(100, '+', 50)
    print(f"calculate(100, '+', 50) = {result}")
    
    result = calc.calculate(15, '**', 2)
    print(f"calculate(15, '**', 2) = {result}")
    
    # Error handling demo
    print("\n--- Error Handling ---")
    try:
        result = calc.divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    try:
        result = calc.square_root(-5)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print("\n" + "=" * 50)
    print("Phase 1 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    demonstrate_calculator()
