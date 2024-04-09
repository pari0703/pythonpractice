# Read input values
x, k = list(map(int, input().split()))

# Read the polynomial expression
expression = input()

# Evaluate the polynomial expression for the given value of x
result = eval(expression.replace('x', str(x)))

# Check if the result equals k
if result == k:
    print(True)
else:
    print(False)
