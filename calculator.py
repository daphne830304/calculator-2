"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    userinput = input('Enter numbers:')
    token = userinput.split(' ')
    print(token)
    if token[0] == 'q':
        break
    elif token[0] == 'add':
        addition = add(int(token[1]),int(token[2]))
        print(addition)
        break
