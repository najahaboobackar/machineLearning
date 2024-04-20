while True:
    n = input("Enter the operation (+, -, *, /): ")
    if n in ('+', '-', '*', '/'):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if n == '+':
            c = a + b
        elif n == '-':
            c = a - b
        elif n == '*':
            c = a * b
        elif n == '/':
            if b != 0:
                c = a / b
            else:
                print("Error: Division by zero!")
                continue  # Restart the loop without executing the next part
        print("Result:", c)
    else:
        print("Invalid operation!")
