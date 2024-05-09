# A lambda function in Python is a small, anonymous function that can have any number of arguments, but can only have one expression
# It is often used for short, simple operations 
# Lambda functions are defined using the lambda keyword, followed by the arguments and the expression
# General syntax: lambda arguments: expression

# add=lambda a,b :a+b

# num,num1=map(int,input("enter two in number").split())
# result=add(num,num1)
# print(result)

#########################################
# add=lambda a,b:a+b

# x=int(input("enter first number:"))
# y=int(input("Enter second number:"))
# result=add(x,y)
# print(result)

#########################################
# fun=lambda num: num%2==0


# num=int(input("enter number:"))
# result=fun(num)
# if result:
#     print("even")
# else:
#     print("odd")

###########################################
# Write code to accept a number from the user and to find its square using a function called calc_square()
# Now rewrite using a lambda function called called calc_square_lambda() and test it
# sqr=lambda num:num**2
# cube=lambda num:num**3

# num=int(input("enter number:"))
# result=sqr(num)
# final=cube(num)
# print(result)
# print(final)

##############################################

# def fact(num):
#     if num==0:
#         return 1
#     else:
#         return num*fact(num-1)

# fact=lambda num:1 if num==0 else num*fact(num-1)

# num=int(input("enter number:"))
# result=fact(num)
# print(result)
