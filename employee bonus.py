sal=int(input("enter the salary of employee"))
grade=chr(input("enter the grade of employee"))
if(grade==A):
    bonus=sal*0.5
    print("the bonus of employee is:",bonus)
elif(grade==B):
    bonus=sal*0.10
    print("the bonus of employee is:",bonus)
else:
    print("invalid input")
if(sal<10000):
    bonus=bonus+(0.2*sal)
    print("the bonus of employee is:",bonus)
