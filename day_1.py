def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def get_operator():
    operators = ['+', '-', '*', '/']
    while True:
        operator = input("Enter an operator(+,-,/,*) : ")
        if operator in operators:
            return operator
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0 :
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operator."


def main():
    print("Welcome to the simple calculator!")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operator = get_operator()
    
    result = calculate(num1, num2, operator)
    print(f"The result of {num1} {operator} {num2} is: {result}\n")

    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
    else:
        main()


if __name__ == "__main__":
    main()

