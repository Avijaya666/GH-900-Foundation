"""Calculator engine - core business logic for arithmetic operations."""


class Calculator:
    """A simple calculator that performs basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator with a result of 0."""
        self.result = 0
        self.previous_result = 0
        self.operation = None
        self.should_reset_display = False
    
    def add(self, num1: float, num2: float) -> float:
        """Add two numbers.
        
        Args:
            num1: First number
            num2: Second number
            
        Returns:
            Sum of num1 and num2
        """
        return num1 + num2
    
    def subtract(self, num1: float, num2: float) -> float:
        """Subtract two numbers.
        
        Args:
            num1: First number
            num2: Second number
            
        Returns:
            Difference of num1 and num2
        """
        return num1 - num2
    
    def multiply(self, num1: float, num2: float) -> float:
        """Multiply two numbers.
        
        Args:
            num1: First number
            num2: Second number
            
        Returns:
            Product of num1 and num2
        """
        return num1 * num2
    
    def divide(self, num1: float, num2: float) -> float:
        """Divide two numbers.
        
        Args:
            num1: First number (dividend)
            num2: Second number (divisor)
            
        Returns:
            Quotient of num1 and num2
            
        Raises:
            ValueError: If attempting to divide by zero
        """
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    
    def power(self, base: float, exponent: float) -> float:
        """Raise base to the power of exponent.
        
        Args:
            base: The base number
            exponent: The exponent
            
        Returns:
            base raised to the power of exponent
        """
        return base ** exponent
    
    def square_root(self, num: float) -> float:
        """Calculate the square root of a number.
        
        Args:
            num: The number
            
        Returns:
            Square root of num
            
        Raises:
            ValueError: If num is negative
        """
        if num < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return num ** 0.5
    
    def percentage(self, num: float, percent: float) -> float:
        """Calculate percentage of a number.
        
        Args:
            num: The number
            percent: The percentage value
            
        Returns:
            The percentage of num
        """
        return (num * percent) / 100
    
    def reciprocal(self, num: float) -> float:
        """Calculate the reciprocal (1/x) of a number.
        
        Args:
            num: The number
            
        Returns:
            Reciprocal of num
            
        Raises:
            ValueError: If num is zero
        """
        if num == 0:
            raise ValueError("Cannot calculate reciprocal of zero")
        return 1 / num
    
    def negate(self, num: float) -> float:
        """Negate a number (multiply by -1).
        
        Args:
            num: The number
            
        Returns:
            Negated number
        """
        return -num
    
    def calculate(self, num1: float, operator: str, num2: float) -> float:
        """Perform a calculation with two operands and an operator.
        
        Args:
            num1: First operand
            operator: Operator string ('+', '-', '*', '/', '**')
            num2: Second operand
            
        Returns:
            Result of the calculation
            
        Raises:
            ValueError: If operator is invalid or operation is invalid
        """
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '**': self.power,
        }
        
        if operator not in operations:
            raise ValueError(f"Invalid operator: {operator}")
        
        return operations[operator](num1, num2)
    
    def reset(self):
        """Reset the calculator to initial state."""
        self.result = 0
        self.previous_result = 0
        self.operation = None
        self.should_reset_display = False
