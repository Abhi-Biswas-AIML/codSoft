def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    if y == 0:
        return "Division by zero error!!!"
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("***************************************")
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divi(num1, num2))
        
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation.lower() != 'y':
            break
    else:
        print("Invalid Input")