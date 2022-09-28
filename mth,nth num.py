list=[14,16,87,36,25,89,34]
size=len(list)
print(size)
list.sort()
print(list)
m=int(input("Enter Mth maximum number which you want :"))
n=int(input("Enter Nth minumum number which you want : "))
if m<1 or m>size:
    greatest=0
else:
    greatest=list[size-m]
if n<=0 or n>size:
    smallest=0
else:
    smallest=list[n-1]
print(greatest)
print(smallest)
print("sum = ",greatest+smallest)
print("Dif = ",abs(greatest-smallest))
