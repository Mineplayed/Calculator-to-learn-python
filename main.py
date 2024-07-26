from modules_package.operations import sum,substract,divide,multiply
import os

def welcome():
    print("Welcome to the smallest calculator ever !!!")
    return

def get_both_numbers():
    # ask for the left and right numbers and store them in vars
    num1 = float(input("What's the left number -> "))
    num2 = float(input("What's the right number -> "))

    return num1, num2

def get_operation():
    # ask for the operator and store it in a var
    print("=== Menu ===")
    print("1. Sum")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Choose the operation [1-4]")

    # Verify if the operation is correct
    timer = 0
    while operation not in ["1","2","3","4"]:
        if timer != 5:
            operation = input("ERROR-02 : The operation need to be an integer  between 1 and 4. ")
            timer += 1
        else:
            exit()

    return operation

def run_calculation(operation, num1, num2):
    match operation:
        case '1':
            result = sum(num1, num2)
        case '2':
            result = substract(num1, num2)
        case '3':
            result = multiply(num1, num2)
        case '4':
            result = divide(num1, num2)
        case _:
            print("Choix invalide.")
    return result

def render_result(operation, num1, num2, result):
    print("=== Result ===")
    match operation:
        case "1":
            print(f"The calcul is {num1} + {num2}")
        case "2":
            print(f"The calcul is {num1} - {num2}")
        case "3":
            print(f"The calcul is {num1} * {num2}")
        case "4":
            print(f"The calcul is {num1} / {num2}")
    print(f"The result is {result}")

if __name__ == "__main__":
    os.system("cls")
    welcome()
    os.system("cls")
    operation = get_operation()
    os.system("cls")
    num1, num2 = get_both_numbers()
    os.system("cls")
    result = run_calculation(operation, num1, num2)
    os.system("cls")
    print(render_result(operation, num1, num2, result))