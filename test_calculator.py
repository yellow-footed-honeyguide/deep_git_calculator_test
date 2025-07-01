#!/usr/bin/env python3
"""
Tests for Calculator class
Run with: pytest test_calculator.py -v
"""

import pytest
from calculator_code import Calculator

class TestCalculator:
    """Test cases for Calculator operations"""
    
    def setup_method(self):
        """Set up test calculator instance"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation"""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction operation"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(-1, -1) == 0
    
    def test_multiply(self):
        """Test multiplication operation"""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0
    
    def test_divide(self):
        """Test division operation"""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-10, 2) == -5
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception"""
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)
