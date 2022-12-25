while True:
    n=int(input("enter the range:"))
    a=[]
    for i in range(1,n+1):
        b=input("enter email address=")
        a.append(b)
    for i in a:
        c=i.find("@")
        print("username:",i[:c],"and domain:",i[c+1:].upper())
    d=input("do you want to continue the program if yes the type 'Y' or 'y' and 'N','n' for exit=")
    if d=="Y" or d=="y":
        pass
    else:
        exit()
