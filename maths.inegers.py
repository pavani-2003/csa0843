a=int(input("enter the number"))
b=int(input("enter the number"))
c=0
for i in range(1,max(a,b)+1):
    if(a%i==0)and(b%i==0):
        c+=1
        print("integers =",c)
