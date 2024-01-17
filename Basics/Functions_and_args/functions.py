# Example for command line arguments
import sys

def add(num1, num2):
    a = num1 + num2
    return a

def mul(num1, num2):
    m = num1 * num2
    return m

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
operations = sys.argv[3]

if operations == "add":
    output = add(num1, num2)
    print(output)
    
if operations == "mul":
    output = mul(num1, num2)
    print(output)    