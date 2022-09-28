a=float(input("fresh laoves:"))
b=float(input("old loaves:"))
a=a*185.00
b=b*0.6*185
n=185.00
t=a+b+n      
print("regular price:",n)
print("amt.new loaves",str(a))
formatted_float_value="{:.2f}".format(b)
print("amt.old loaves",formatted_float_value)
print("total amount:",t)
