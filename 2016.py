"""
*Assumption: The program terminates when the user enters -1 as the food type (input) 

"""

# Initialize price list as a dictionary
priceList = {1: 10, 2: 12, 3: 15, 4: 10, 5: 25, 6: 45, 7: 50, 8: 25, 9: 10, 10: 12}

# Initialize Total
tot = 0


while True:
    # input the file type
    ftype = int(input())

    # break out of the loop if ftype is -1
    if ftype == -1:
        break
    # get price from the price list
    price = priceList[ftype]

    # add price to the total
    tot += priceList[ftype]

# Print total
print("Total: ", tot)

