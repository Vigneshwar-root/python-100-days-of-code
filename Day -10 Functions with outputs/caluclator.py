

#Calculator
#add
def add(n1,n2):
    return n1 + n2
#subtract
def subtract(n1,n2):
    return n1 - n2
#multiply
def multiply(n1,n2):
    return n1 * n2
#divide
def divide(n1,n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# function = operations["*"]
# function(2,3)

# print(function(1,2))
def calculator():
    num1 = float(input("What is the first number?: "))

    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above:")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer} \n")
        continue_flag = input(f"type 'y' to continue calculating with {answer}: or type 'n' to start a new calculation ")

        if continue_flag == 'y':
            num1 = answer
        elif continue_flag == 'n':
            calculator()
            should_continue = False
        else:
            should_continue = False

calculator()
