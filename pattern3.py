for row in range (7):
    for cal in range (5):
        if (row==0 or row==6)or(cal==0):
            print("*",end="")
        else:
            print(end=" ")
    print()