import os

import art


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

answer = 0
end = 2

while end != 3:
    if end == 2:
        _ = os.system('cls')
        print(art.logo)
        n1 = float(input("Enter first number: "))
        end = 1
    if end == 1:
        n2 = float(input("Enter next number: "))
        print("Available operations are: ", end='')
        for k in operations:
            print(k, end=',')
        op = input("\nSelect operation: ")
        answer = operations[op](n1, n2)
        print("\n{} {} {} = {}\n".format(n1, op, n2, answer))
        n1 = answer
    else:
        print("Wrong choice! Exiting!")
        exit()
    print("\tPress 1 to continue calculations with {}".format(answer))
    print("\tPress 2 to discard {} and start new calculation".format(answer))
    print("\tPress 3 to exit.")
    end = int(input("Enter Choice: "))
print("Exiting!")
