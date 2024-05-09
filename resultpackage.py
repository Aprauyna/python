from pakages import greet

name=input("enter name :")
greet.sayHello(name)


from pakages import functions

num=int(input("enter number"))
num1=int(input("enter second number"))
out=functions.sum(num,num1)
print(out)
avg=functions.average(num,num1)
print(avg)
power=functions.power(num,num1)
print(power)