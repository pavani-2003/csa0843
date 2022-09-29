def comb(L):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])
n1=int(input("enter the first digit:"))
n2=int(input("enter the second digit:"))
n3=int(input("enter the third digit:"))
comb([n1,n2,n3])
