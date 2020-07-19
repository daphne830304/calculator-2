"""CLI application for a prefix-notation calculator."""
#import pdb; pdb.set_trace()

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
from functools import reduce


# Replace this with your code
def calculator():
    while True:
        userinput = input('Enter numbers:')
        token = userinput.split(' ')      
        oper = token[0]
        if len(token) == 2:
            num1 = int(token[1])
        if len(token) == 3:
            num1 = int(token[1])
            num2 = int(token[2])
        if len(token) >3:
            print('incorrect input')
        if token[0] == 'q':
            break
        elif token[0] == "+":
            add(num1, num2)
        elif token[0] == "-":
            subtract(num1, num2)
        elif oper == "square":
            print(square(num1))
        elif oper == "*":
            print(multiply(num1,num2))
        elif oper == "/":
            print(divide(num1,num2))
        elif oper == "cube":
            print(cube(num1))
        elif oper == "pow":
            print(power(num1, num2))
        elif oper == "mod":
            print(mod(num1,num2))

#def further():
    while True:
        userinput = input('Enter numbers:')
        token = userinput.split(' ')      
        oper = token[0]
        num1 = float(token[1])
        if len(token) == 3:
            num2 = float(token[2])
        if len(token) >= 3:
            print('invalid entry')