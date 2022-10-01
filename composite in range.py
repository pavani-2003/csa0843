a=int(input('Enter a: '))
b=int(input('Enter b: '))
for number in range(a,b+1):
    factor=0
    for i in range(1,number):
      if number%i==0:
        factor=i
    if factor>1:
      print (number)
