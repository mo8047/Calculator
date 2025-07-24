def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    u_no1 = float(input("Enter the first number: "))
    x=True
    while x:
        u_operation = input("Enter the operation you would like to use '+', '-', '*', '/': ")
        u_no2 = float(input("Enter the second number: "))

        calculation = operation[u_operation](u_no1, u_no2)
        print(f"{u_no1} {u_operation} {u_no2}={calculation}")
        u_next_op = input(f"Would you like to continue another operation with {calculation}(y/n): ")#n for new calculation
        if u_next_op == "y":
            u_no1 = calculation
        else:
            x=False
            calculator()
calculator()

