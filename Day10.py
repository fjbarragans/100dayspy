import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide 
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))

    restart = True

    while restart:
        for symbol in operations:
            print(symbol)

        symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        operation = operations[symbol]

        result = operation(num1,num2)

        print(f"{num1} {symbol} {num2} = {result}")

        decision = input(f"Type 'c' to continue calculating with {result}, type 'r' to restart the calculator, or type another letter to exit: ")

        if decision == 'c':
            num1 = result
        elif decision == 'r':
            restart = False
            os.system('cls')
            calculator()
        else:
            restart = False
            os.system('cls')

calculator()