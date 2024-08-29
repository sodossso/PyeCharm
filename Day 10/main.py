
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={"+":add,
            "-":subtract,
            "*":multiply,
            "/":divide,
            }

decision="n"
while decision=="n":
    import art
    print(art.logo)
    n1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    operation_key=input("Pick an operation: ")
    n2=float(input("What's the next number?: "))
    result=operations[operation_key](n1,n2)
    print(f"{n1} {operation_key} {n2} = {result}")
    decision=input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
    if decision=="y":
        n1=result
    while decision=="y":
        for key in operations:
            print(key)
        operation_key = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = operations[operation_key](n1, n2)
        print(f"{n1} {operation_key} {n2} = {result}")
        decision = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
        if decision == "y":
            n1 = result

#Instead of a while loop could also create a calculator function which gets called inside of the loop through function recurring.
#Given that I only realised this post checking the solution for the challenge, I'll keep the code I wrote on my own bove.