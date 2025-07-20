#!/usr/bin/env python3
"""
Simple Calculator
A tiny command-line calculator that supports the four basic arithmetic
operations (+, -, *, /) and keeps asking if the user wants to continue.
"""

def get_number(prompt: str) -> float:
    """Prompt until the user enters a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ❌  Invalid number. Try again.")

def get_operation() -> str:
    """Prompt until the user enters a valid operation symbol."""
    valid_ops = {"1", "2", "3", "4"}
    while True:
        print("\n11 = +\n", "2 = -\n", "3 = *\n", "4 = /")
        op = input("Choose operation (1 ,2 ,3 ,4): ").strip()
        if op in valid_ops:
            return op
        print("  ❌  Invalid operation. Choose one of: +  -  *  /")

def calculate(a: float, b: float, op: str) -> float:
    """Return a op b. Raises ZeroDivisionError if needed."""
    if op == "1":
        return a + b
    elif op == "2":
        return a - b
    elif op == "3":
        return a * b
    elif op == "4":
        if b == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        return a / b
    # Should never reach here
    raise ValueError("Unsupported operation")

def main():
    print("=== Simple Calculator ===")
    while True:
        print()

        num1 = get_number("Enter first number:  ")
        num2 = get_number("Enter second number: ")
        op   = get_operation()

        try:
            result = calculate(num1, num2, op)
            print(f"\nResult: {num1} {op} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"\nError: {e}")

        again = input("\nDo another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()