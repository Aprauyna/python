###################################### if else ##############################

# height=int(input("enter height in cm?\n"))
# if(height>=120):
#     print('go on your rollercoster ride')
# else:
#     print("not eligible for rollercoster ride")

# num=int(input("enter number to check odd or even\n"))
# if(num%2==0):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


################################ nested if-else ################################################## 

# height=int(input("enter height in cm?\n"))
# age=int(input("enter age?\n"))
# if(height>=120):
#     if(age<=18):
#         print("go for ride and pay 7$")
#     else:
#         print("go for ride and pay 14$")
# else:
#     print("not eligible for rollercoster ride")

##############################################  if-elif     #################################################

# height=int(input("enter height in cm?\n"))
# age=int(input("enter age?\n"))
# if(height>=120):
#     if(age<12):
#         print("go for ride and pay 7$")
#     elif(age>=12 and age<=18):
#         print("go for ride and pay 14$")
#     else:
#         print("go for ride and pay 21$")
# else:
#     print("not eligible for rollercoster ride")

################################################## BMI calculator ##############################################################

# height = float(input("enter height in meters?\n"))
# weight = int(input("enter weight in kgs?\n"))
# bmi = (weight/(height**2))
# if(bmi<=18.5):
#     print(f"your bmi rate is {bmi} and your have under weight.")
# elif(bmi>18.5 and bmi<=25):
#     print(f"your bmi rate is {bmi} and your have normal weight.")
# elif(bmi>25 and bmi<=30):
#     print(f"your bmi rate is {bmi} and your have slightly over weight.")
# elif(bmi>30 and bmi<=35):
#     print(f"your bmi rate is {bmi} and you obsses.")
# else:
#     print(f"your bmi rate is {bmi} and you critically obsses.")

################################### leap year ##########################################################

# year = int(input("enter year to check leap or not\n"))
# if((year%4==0 and year%100!=0) or year%400==0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")


# def leap_year(year):
#     if((year%4==0 and year%100!=0) or year%400==0):
#         return True
#     else:
#         return False
# year = int(input("enter year to check leap or not\n"))

# if leap_year(year):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

################################### swapping two number without using third varible #################

# num1=int(input("enter number\n"))
# num2=int(input("enter number\n"))

# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
# print(f"num1 is {num1} and num2 is {num2}")

#######################################################################################################

# height = int(input("enter your height in cm?\n"))
# age =int(input("enter your age\n"))
# bill=0

# if(height>=140):
#     if(age<12):
#         bill=7
#         print("for child you paid 7$\n")
#     if(age>=12 and age<18):
#         bill=14
#         print("for young you pqid 14$\n")
#     if(age>=18):
#         bill=21
#         print("for adult you paid 21$\n")
#     photos=input("if you want photos enter 'y' and for not enter 'n' \n")
#     if(photos=="y"):
#         bill+=3
#         print(f"total bill is {bill}")

# else:
#     print("you are not eligible")

############################################################################################################
# print("thankyou for choosing python pizzas deliviries\n")
# quantity=int(input("enter no of pizzas you want\n"))
# size=input("enter size of pizza 's' for small 'm' for medium 'l' for large\n")


# price=0
# if(size=="s"):
#     price=15
#     print("for small pizza pay 15$")
# elif(size=="m"):
#     price=20
#     print("for small pizza pay 20$")
# elif(size=="l"):
#     price=25
#     print("for small pizza pay 25$")
# else:
#     print("try again please choose correct option\n")
#     exit(1)
# add_paporoni=input("do you want paporoni? y or n \n")
# if(add_paporoni=="y"):
#     if(size=="s"):
#         price+=2
#     if(size=="l" or size=="m"):
#         price+=3
# else:
#     print("please choose correct option")
#     exit(1)
# extra_cheese=input("do you want extra cheese? y or n \n")
# if(extra_cheese=="y"):
#     price+=1
# final_price=quantity*price
# print(f"now your final bill is {final_price} and your quantity of pizza is {quantity}")


######################################################################################################################

# name1=input("enter your name\n")
# name2=input("enter second name\n")
# combine_name=name1+name2
# lower_name=combine_name.lower()
# t=lower_name.count("t")
# r=lower_name.count("r")
# u=lower_name.count("u")
# e=lower_name.count("e")

# first_digit=t+r+u+e
# l=lower_name.count("l")
# o=lower_name.count("o")
# v=lower_name.count("v")
# e=lower_name.count("e")

# second_digit=l+o+v+e

# score=int(str(first_digit)+str(second_digit))
# if(score<10 and score>90):
#     print(f"your score is {score} you go together like coke and mentos")
# elif(score>40 and score<50):
#     print(f"your score is {score} you are alright together")
# else:
#     print(f"your score is {score}")

#########################################################################################################################

# print("welcome to the teasure island \n your mission to find the teasure\n")
# path=input("choose your path either left or right\n").lower()
# if(path=="left"):
#     cond=input("choose swim or wait\n").lower()
#     if(cond=="wait"):
#         door=input("choose door colour red,yellowand blue\n").lower()
#     else:
#         print("game over")
#         exit(1)
#     if(door=="yellow"):
#         print("you win\n")
#     else:
#         print("game over")
# else:
#     print("game over")


