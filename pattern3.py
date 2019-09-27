for row in range (7):
    for cal in range (5):
        if ((cal==0 or cal==4)and row !=0) or (row==0 or row ==3)and (cal>0 and cal<4):
            print("*",end="")
        else:
            print(end=" ")
    print()