# 🧮 Simple Calculator

> A lightweight, beginner-friendly command-line calculator built with Python — no dependencies required.

---

## 📋 Description

**Simple Calculator** is a Python command-line application that performs the four essential arithmetic operations: addition, subtraction, multiplication, and division. It is designed to be easy to read, easy to extend, and a great starting point for anyone learning Python.

Key highlights:
- Clean, modular code — each operation is its own function
- Input validation — non-numeric entries are handled gracefully
- Division-by-zero protection with a clear error message
- Infinite loop interface — run as many calculations as you want

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/simple-calculator.git

# 2. Navigate into the project folder
cd simple-calculator

# 3. Run the calculator
python calculator.py
```

---

## 💡 Examples

### Example 1 — Addition
```
Select an operation (1-5): 1
  Enter first number : 12
  Enter second number: 8

  ✔  12.0 + 8.0 = 20.0
```

### Example 2 — Division
```
Select an operation (1-5): 4
  Enter first number : 100
  Enter second number: 4

  ✔  100.0 / 4.0 = 25.0
```

### Example 3 — Division by zero (handled)
```
Select an operation (1-5): 4
  Enter first number : 9
  Enter second number: 0

  ✗  Error: Cannot divide by zero.
```

### Example 4 — Invalid input (handled)
```
  Enter first number : hello
  ✗  Invalid input. Please enter a numeric value.

  Enter first number : 5
```

---

## 📁 Project Structure

```
simple-calculator/
├── calculator.py       # Core calculator logic and CLI interface
├── test_calculator.py  # Unit tests (optional, see below)
└── README.md           # Project documentation
```

---

## 🧪 Running Tests

```bash
python -m unittest test_calculator.py -v
```

Expected output:
```
test_add             ... ok
test_subtract        ... ok
test_multiply        ... ok
test_divide          ... ok
test_divide_by_zero  ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
