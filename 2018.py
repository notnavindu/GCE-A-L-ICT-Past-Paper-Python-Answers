# input comma seperated integer list L (without spaces)   i.e.: 23,12,34,67
L = input()

# Split string into a list of integers
L = list(map(int, L.split(",")))

# length of the list
n = len(L)

k = int(input("Enter value to search: "))

found = False
i = 0
# iterate over the list
while i < n:
    if L[i] == k:
        found = True
        break
    else:
        pass
    i += 1

if found:
    print("True")
else:
    print("False")
