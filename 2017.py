# Function to write data to a text file
def writeToFile(hn, prev, post, amount):
    f = open("deb.txt", "a")
    print(hn, prev, post, amount, file=f)
    f.close()


# Input house number, prev,post meter readings
houseNumber = input("Enter house number:")
prev = int(input("Enter Previous meter reading:"))
post = int(input("Enter Post Meter reading:"))

# Calculate units
units = post - prev

# calculate amount
if units < 64:
    amount = units * 5
else:
    amount = (units - 64) * 10 + 64 * 5

print(houseNumber, prev, post, amount)

# Write data to a text using the function writeToFile()
writeToFile(houseNumber, prev, post, amount)
