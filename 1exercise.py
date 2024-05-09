# place=["india","Austria","Germany","Canada","Poland"]
# print(place)
# print(sorted(place))
# print(place)
# print(sorted(place,reverse=True))
# print(place)
# place.reverse()
# print(place)
# place.reverse()
# print(place)
# place.sort()
# print(place)
# place.sort(reverse=True)
# print(place)

# food=("sandwich","burger","fries","coke")
# for item in food:
#     print(item)

# food[1]="mutton"
# print(food)

# food=("sandwich","burger","fries","coke","chicken")
# for item in food:
#     print(item)

############################################
# student_marks=(("Arun",[44,55,66,77]),("Ankit",[11,22,33,44]),("Bob",[44,55,66,33]))
# for student,marks in student_marks:
#     total=sum(marks)
#     average=total/len(marks)
#     print(f"{student}: Average is {average}")
# print(("\n"))

# student_detail=[
#     ("Alice", [85, 90, 78, 92]),
#     ("Bob", [76, 88, 92, 80]),
#     ("Charlie", [90, 92, 89, 78]),
#     ("David", [70, 68, 72, 75])

# ]

# for student,marks in student_detail:
#     total=sum(marks)
#     average=total/len(marks)
#     percentage=(total*100)//500
#     print(f"{student} :Average is {average} and percentage is {percentage}")

##################################################

# temperature=[
#     ("Monday", [29, 27, 33, 24, 28]),
#     ("Tuesday", [31, 30, 24, 27, 29 ]),
#     ("Wednesday", [23, 27, 29, 30, 25]),
#     ("Thursday", [30, 28, 27, 29, 30]),
#     ("Friday", [32, 23, 29, 27])

# ]

# for day,temps in temperature:
#     print(f"{day}s: maximum temperature :",max(temps))

#######################################################
# python control structure
# Sequential logic – Just execute the next statement after the current statement
# Selection (Conditions) - if
# Repetition (Loop) – for, while

# number=int(input("enter number:"))
# if number>0:
#     print("number is +ve")
# if number<0:
#     print("number is -ve")
# if number==0:
#     print("number is zero")

#####################################################

# number=int(input("enter number"))
# if number%2==0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

############################################
#armstrong number

# def fun(number):
#     count=0
#     sum=0
#     numbers=number
#     num=number
#     while numbers>0:
#         numbers=numbers//10
#         count=count+1
#     while num>0:
#         rem=num%10
#         cube=rem**count
#         sum=sum+cube
#         num=num//10
#     if(number==sum):
#         print(f"{number} is armstrong")
#     else:
#         print(f"{number} is not armstrong")




# number=int(input("enter number to check armstrong or not "))
# fun(number)

#################################################
#palindrome
# def fun(palindrome):
#     length=len(palindrome)
#     print(length)
#     for i in range(length//2):
#         if palindrome[i]==palindrome[length-i-1]:
#             return True
#     return False
    




# palindrome=input("enter word to check palindrom or not")
# out=fun(palindrome)

# if out:
#     print("palindrome")
# else:
#     print("not palindrome")
#######################################################
#febonaic series

# def fun(terms):
#     num=0
#     num1=1
#     print(num)
#     print(num1)
#     while(terms>0):       
#         num2=num+num1
#         num=num1
#         num1=num2
#         print(num2)
#         terms=terms-1


# terms=int(input("enter number of terms"))
# fun(terms)

########################################################
# num1=float(input("enter first number :"))
# num2=float(input("enter second number :"))
# num3=float(input("enter third number :"))

# if num1>=num2 and num1>=num3:
#     print(f"{num1} is largest number")
# elif num2>=num1 and num2>=num3:
#     print(f"{num2} is largest number")
# else:
#     print(f"{num3} is largest number")

#########################################################
# banned_users = ['andrew', 'carolina', 'david']
# user="marie"

# if user not in banned_users:
#     print(f"{user.title()},you can post a response if you wise")
#########################################################
# required=input("mushrooms,green peeppers,extra cheese :")
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if required == "green peppers":
#        print("Sorry, we are out of green peppers right now.")
#        exit()
#     else:
#         print(f"Adding {required}.")
#         print("Finished making your pizza!")
#         exit()

##############################################################

# available_topping=["mushrooms","olives","green peppers","pepporoni","pineapple","extra cheese"]
# requested_topping=["mushrooms","french fries","extra cheese"]

# for request in requested_topping:
#     if request in available_topping:
#         print(f"Adding : {request}")
#     else:
#         print(f"sorry we dont have {request}")
# print("\nFinished making your pizza")

########################################################





