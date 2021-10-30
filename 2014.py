def fact():
    # Input required number
    n = int(input("Enter number: "))

    fact = n

    # calculate Factorial
    while (n > 1):
        n = n - 1
        fact = fact * n

print("Factorial of ", n, ": ", fact)
