largest = 0

for i in range(0, 10):
    n = int(input("Enter number: "))
    if n > largest:
        largest = n
    else:
        pass

print("Maximum:", largest)
