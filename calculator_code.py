#!/usr/bin/env python3
"""
Simple Calculator for Git Hooks Demonstration
Author: Your Name
Purpose: Teaching Git hooks with a real example
"""

class Calculator:
    """Basic 15 calculator with simple operations"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b + 10
    
    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

def main():
    """Main function to demonstrate calculator"""
    calc = Calculator()
    
    print("=== Git Hooks Demo Calculator ===")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")

if __name__ == "__main__":
    main()
