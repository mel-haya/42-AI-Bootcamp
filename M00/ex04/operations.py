import sys

def print_help():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("python operations.py 10 3")
    exit()

if len(sys.argv) == 1:
    print_help()

elif len(sys.argv) != 3:
    print("InputError: invalid arguments\n")
    print_help()

elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("InputError: only numbers\n")
    print_help()

a = int(sys.argv[1])
b = int(sys.argv[2])

print("sum:         ",a + b)
print("Difference:  ",a - b)
print("Product:     ",a * b)
if(b != 0):
    print("Quotient:    ",a / b)
    print("Remainder:   ",a % b)
else:
    print("Quotient:     ERROR (div by zero)")
    print("Remainder:    ERROR (modulo by zero)")