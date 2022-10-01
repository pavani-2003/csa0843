c=input("enter the character  to be printed")
n=int(input("enter rows:"))
if(n<=0):
    print("enter a positive integer")

for i in range(0, n):
    for j in range(0, i+1):
        print(c,end="")
    print()
