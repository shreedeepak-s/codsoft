def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error We can't divide by 0"
    else:
        return x / y

def main():
    print("Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Input is not valid.Enter a numeric value")
        return
    print("\nChoose any operation:")
    print("a. Add")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")
    choice = input("Enter the operation (a/b/c/d): ")
    if choice == "a":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == "b":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "c":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "d":
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid choice reenter the choices")

if __name__ == "__main__":
    main()
