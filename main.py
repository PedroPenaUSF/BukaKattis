# Step 1 receive all inputs
a = int(input())
operand = input()
b = int(input())

# Step 2 Distinguish operand and perform operation
if operand == '+':
    solution = a + b
else:
    solution = a * b

# Step 3 print solution
print(solution)
