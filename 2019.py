#input the total number of inputs
n = int(input("Number of inputs: ")) 

#a: total number of positive even numbers
a=0

while not n<=0:
    x = int(input("Enter Number: "))
    if x%2 == 0 :
        a = a+1
    n=n-1

print("Positive even numbers:",a)