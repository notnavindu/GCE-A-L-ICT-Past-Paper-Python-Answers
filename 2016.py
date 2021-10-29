"""
*Assumption: The program terminates when the user enters -1 as the food type (input) 

"""

# Initialize price list as a dictionary
priceList = {1: 10, 2: 12, 3: 15, 4: 10, 5: 25, 6: 45, 7: 50, 8: 25, 9: 10, 10: 12}

# Initialize Total
total = 0


while True:
    # input the file type
    foodType = int(input("Enter food type: "))

    # break out of the loop if ftype is -1
    if foodType == -1:
        break
    # get price from the price list
    price = priceList[foodType]

    # add price to the total
    total += priceList[foodType]

# Print total
print("Total: ", total)

