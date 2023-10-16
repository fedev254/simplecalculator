while True:
    print("User Guidlines:")

    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    print("====Let's Get Started=====")
    user_input= input("Enter your choice")

    if user_input=="quit":
        break
    elif user_input== "add":
        num1= int (input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result= num1 + num2
        print(result)
    elif user_input == "subtract":
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result = num1 - num2
        print(result)
    elif user_input == "multiply":
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result = num1 * num2
        print(result)
    elif user_input == "divide":
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result = num1 / num2
        print(result)
    else:
        print("Invalid Input")


