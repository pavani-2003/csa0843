m=int(input("enter the m value"))
if(m<0):
    print("invalid")
else:
    n=int(input("enter the n value"))
if(n<=0):
    print("invalid")
else:
    k=int(input("enter the k values"))
if(k<=0):
    print("invalid")
else:
    print("numbers are =")
    for i in range (m,n,k+i):
        print(" ",i)
