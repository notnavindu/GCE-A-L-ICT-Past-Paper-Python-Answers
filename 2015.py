# Open marks.txt
f = open("marks.txt", "a")

while True:
    # input index number
    idx = int(input("Index: "))

    # If index number is -1 break out of the loop
    if idx == -1:
        break

    # input marks
    m1 = int(input("Mark 1: "))
    m2 = int(input("Mark 2: "))
    m3 = int(input("Mark 3: "))

    # write index, m1, m2, m3 the  file
    print(idx, m1, m2, m3, sep=",", file=f)

# cloase the file
f.close()
