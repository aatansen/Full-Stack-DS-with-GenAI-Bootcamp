# Normal function
'''
def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operation."

result=calculator(3,5,'multiply')
print(result)
'''

# Command line utility
import argparse
import sys

def calculator(args):
    if args.o == 'add':
        return args.a + args.b
    elif args.o == 'sub':
        return args.a - args.b
    elif args.o == 'mul':
        return args.a * args.b
    elif args.o == 'div':
        if args.b != 0:
            return args.a / args.b
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operation."

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=float, default=1.0)
parser.add_argument("--b", type=float, default=2.0)
parser.add_argument("--o", type=str, default="add")

# args = parser.parse_args()
# sys.stdout.write(str(calculator(args)))

args = parser.parse_args()
result = calculator(args)
print(result)