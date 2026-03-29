"""
Simple Calculator
A command-line calculator supporting basic arithmetic operations.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
}


def get_number(prompt: str) -> float:
    """Prompt the user until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ✗  Invalid input. Please enter a numeric value.\n")


def display_menu() -> None:
    print("\n" + "=" * 36)
    print("       🧮  SIMPLE CALCULATOR")
    print("=" * 36)
    for key, (symbol, _) in OPERATIONS.items():
        labels = {"+": "Add", "-": "Subtract", "*": "Multiply", "/": "Divide"}
        print(f"  [{key}]  {labels[symbol]} ({symbol})")
    print("  [5]  Quit")
    print("-" * 36)


def run_calculator() -> None:
    """Main loop for the interactive calculator."""
    print("\nWelcome to Simple Calculator!")

    while True:
        display_menu()
        choice = input("Select an operation (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye! 👋\n")
            break

        if choice not in OPERATIONS:
            print("  ✗  Invalid choice. Please select 1-5.")
            continue

        symbol, operation = OPERATIONS[choice]

        a = get_number("  Enter first number : ")
        b = get_number("  Enter second number: ")

        try:
            result = operation(a, b)
            print(f"\n  ✔  {a} {symbol} {b} = {result}")
        except ValueError as e:
            print(f"\n  ✗  Error: {e}")


if __name__ == "__main__":
    run_calculator()
