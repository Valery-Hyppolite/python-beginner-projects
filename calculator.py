from replit import clear
from Art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

#def squareroote(n1):
    (n1)^0.5

#def xsquare(n1):
    (n1)^2


operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("what's the first number "))
    for key in operation:
        print(key)
    continue_calculating = True
    
    while continue_calculating == True:
        operation_symbol = input("Pick an aperation from line above: ")
        num2 = float(input("what's the next number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        contniue_option = input("would you like to continue calculating? type 'y' or 'n' ")
        if contniue_option == 'n':
            continue_calculating == False
            clear()
            calculator()
        elif contniue_option == True:
            num1 = answer

calculator()
