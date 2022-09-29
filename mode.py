n=[1,1,2,3,4,5,6,2,1,3,3,3,3,1]
n.sort()
L1=[]
i=0
while i<len(n):
    L1.append(n.count(n[i]))
    i+=1
    d1=dict(zip(n,L1))
    d2={k for (k,v) in d1.items() if v==max(L1)}
    print("mode is :",d2)
