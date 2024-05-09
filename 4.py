###########################################3 randomization ###################################
#generally we use in game to generate random entity
#python have own random  module

# import random

# num=random.randint(1,10)
# print(num)

# num2=random.random()
# #how to generate floatimg point numnber between 0 to 5
# num2*=5
# print(num2)

###############################################################################################

# import random
# num=random.randint(0,1)
# if(num==1):
#     print("Head")
# if(num==0):
#     print("Tails")
######################################python list ###############################################
#it is the way orgnizing the data in python.here we want to store group piece of data,data that have some sort of connection with eachother,
#here we can differnet data in single variable,we might to have order in data
#list use squre barcket to store data,and data can be any datatype or mixed datatype

# colour=["red","green","blue"]
# colour.append("white") #alter at the last position
# colour[0]="pink"
# colour.extend(["black","brown"])
# colour.insert(1,"nylon")
# print(colour)
# colour.remove("white")
# colour.pop(0)
# colour.pop()
# colour.sort()

# print(colour[0])
# print(colour[-1])
# print(colour)

# colour.reverse()
# print(colour)

# colour.clear()
# print(colour)

# fruit=["apple","orange","grapes"]
# vegetables=["spinach","kale"]
# dirty = [fruit,vegetables]
# print(dirty[1][1])

# line1=[" "," "," "]
# line2=[" "," "," "]
# line3=[" "," "," "]
# map=[line1,line2,line3]
# position=input()
# letter=position[0].lower()
# abc=["a","b","c"]
# letter_index=abc.index(letter)
# number_index=int(position[1])-1
# map[number_index][letter_index]="x"
# print(f"{line1}\n{line2}\n{line3}")
##############################################################################################

import random

rock='''()'''
paper='''[]'''
scissor='''x'''

list=[rock,paper,scissor]
user_choice=int(input("what do you choose ? type 0 for rock,1 for paper or 2 for scissor.\n"))
if user_choice>=3 and user_choice<0:
    print("invalid input.\n")
else:
    print(list[user_choice])

    computer_choice=random.randint(0,2)
    print(computer_choice)
    print(list[computer_choice])

    if(user_choice==0 and computer_choice==2):
        print("you win")
    elif(user_choice==2 and computer_choice==0):
        print("you loss")
    elif(computer_choice>user_choice):
        print("you loss")
    elif(computer_choice<user_choice):
        print("you win")
    elif(computer_choice==user_choice):
        print("it is draw")
    