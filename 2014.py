# Input required number
n = int(input())

fact = 1

# calculate Factorial
for i in range(n, 1, -1):
    fact = fact * i

print("Factorial of {} => {} ".format(n, fact))
