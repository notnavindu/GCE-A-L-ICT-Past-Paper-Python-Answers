K = int(input("Enter K : "))

N = int(input("Enter length of array 'L' : "))

# Allocate memory for array
L = [0] * N

for i in range(N):
    L[i] = int(input("Enter value for element number " + str(i+1) + " : "))

# Set M to a very large number : 'infinity'
M = float('inf')

X = M

for y in L:
    if (y > K) and (y < X):
        X = y

print("The smallest element in L that is greater than K is", X)
