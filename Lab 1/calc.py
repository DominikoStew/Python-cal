def separator():
    print("-" * 30)


def print_menu():
    separator()
    print("Welcome to PyCalc")
    separator()

    print("[1] - Add")
    print("[2] - Substract")
    print("[3] - Multiply")
    print("[4] - Divide")
    print('[x] - Close')
    separator()


def sum(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

# Instruction


val = ""
while(val != 'x'):
    print_menu()
    val = input("Please choose an option: ")
    num1 = int(input("Please input num1: "))
    num2 = int(input("Please input num2: "))

    if(val == '1'):
        res = sum(num1, num2)
        print("Result: " + str(res))

    if(val == '2'):
        res = sub(num1, num2)
        print("Result: " + str(res))

    if(val == '3'):
        res = multiply(num1, num2)
        print("Result: " + str(res))

    elif(val == '4'):
        if(num2 == 0):
            print("Error: You can't divide by 0.")
            input("Press Enter to continue...")
            continue
        res = divide(num1, num2)
        print("Result: ", str(res))
        separator()


input("Press Enter to continue...")
print("\n" * 4)
