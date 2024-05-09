#function and output

def string(name,location):
    return f"{name} {location}" #return means end of the program

output=string("arun","pune")
print(output)

#########################################################################################
# def format_name(fname,lname):
#     if fname=="" or lname=="":
#         return "invalid input"
#     formated_fname=fname.title()
#     formated_lname=lname.title()
#     return f"return :{formated_fname} {formated_lname}"


# f_name=input("enter your first name\n")
# l_name=input("enter your last name\n")
# output=format_name(f_name,l_name)
# print(output)

###########################################################################################
# def is_leap(year):
#     if (year%4==0 and year%100!=0) or year%400==0:
#         return True
#     else:
#         return False

# def days_of_month(year,month):
#     """here we check no of days in month""" #this is docstring:here we documenting our program or function and we added multiple line comment also
#     months=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if month==2 and is_leap(year):
#         return 29
#     else:
#         return months[month-1]

# year=int(input("enter year"))
# month=int(input("enter month"))
# days=days_of_month(year,month)
# print(days)
##########################################################################################
# def outer_fun(a,b):
#     def inner_fun(c,d):
#         return c+d
#     return inner_fun(a,b)

# output=outer_fun(5,10)
# print(output)

######################################################################################
# def fun(num):
#     if num<80:
#         return
#         print("fdgwew")
#     if num<80:
#         return "pass"
#     if num<80:
#         return 'great'
    

# print(fun(20))

#####################################################################################
#pallindrom


# def isPalindrome(s):

# 	# Using predefined function to
# 	# reverse to string print(s)
# 	rev = ''.join(reversed(s))#this is predefined fun to reverse the string

# 	# Checking if both string are
# 	# equal or not
# 	if (s == rev):
# 		return True
# 	return False

# # main function
# s = "malayalam"
# ans = isPalindrome(s)

# if (ans):
# 	print("Yes")
# else:
# 	print("No")
#######################################################################################
# def pallin(name):
    
#     for i in range((len(name))//2):
#         if name[i]!=name[(len(name))-i-1]:
#             return False
        
#     return True


# name=input("enter name")
# out=pallin(name)
# if out:
#     print("yes")
# else:
#     print("no")



	
#############################################

# def add(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1-num2
# def mul(num1,num2):
#     return num1*num2
# def div(num1,num2):
#     return num1/num2

# operations={
#     "+":add,
#     "-":sub,
#     "*":mul,
#     "/":div
# }
# num1=int(input("enter number\n"))
# num2=int(input("enter number\n"))
# for symbol in operations:
#     print(symbol)
# operator=input("chosse operation\n")
# function=operations[operator]
# out=function(num1,num2)
# print(f"{num1} {operator} {num2} = {out}")

# end=False
# while not end:
#     num=int(input('enter anothr number\n'))
#     for symbol in operations:
#         print(symbol)
#     operator=input("chosse operation\n")
#     function=operations[operator]
#     output=function(out,num)
#     out=output
#     print(output)
#     kite=input("for exit enter x for continune enter any charcter\n")
#     if kite=="x":
#         end=True

#################################################################################
#with recursion for fresh use not want complete exit
# def cal():

#     def add(num1,num2):
#         return num1+num2
#     def sub(num1,num2):
#         return num1-num2
#     def mul(num1,num2):
#         return num1*num2
#     def div(num1,num2):
#         return num1/num2

#     operations={
#         "+":add,
#         "-":sub,
#         "*":mul,
#         "/":div
#     }
#     num1=int(input("enter number\n"))
#     end=False
#     while not end:
#         num=int(input('enter anothr number\n'))
#         for symbol in operations:
#             print(symbol)
#         operator=input("chosse operation\n")
#         function=operations[operator]
#         output=function(num1,num)
#         num1=output
#         print(output)
#         kite=input("enter x fresh start otherwise for continue enter any key\n")
#         if kite=="x":
#             end=True
#             cal()
# cal()





