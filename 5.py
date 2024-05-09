# fruits=["apple","orange","grapes"]
# fruits.append("peach")
# fruits.insert(0,"papaya")

# for fruit in fruits:
#     print(fruit + " pie")


# print(fruits)

###########################################################################################

# heights=(input("enter heights of student\n").split())

# for n in range(0,len(heights)):
#     heights[n] = int(heights[n])

# total_height=0
# no_of_student=0
# for height in heights:
#     total_height+=height
#     no_of_student+=1

# avg_height=total_height/no_of_student
# print(avg_height)

##########################################################################################
# highest_score=input("enter student score\n").split()

# for n in range(0,len(highest_score)):
#     highest_score[n]=int(highest_score[n])

# max_score=0
# for score in highest_score:
#     if(score>max_score):
#         max_score=score

# print(max_score)

# print(max(highest_score))

########################################################################################
# total=0
# for num in range(1,10):
#     print(num)
#     total+=num
# print(total)

#############################################################################################
# target=int(input("enter number"))
# even=0
# odd=0
# for num in range(1,(target+1)):
#     if(num%2==0):
#         even+=num
#     else:
#         odd+=num
# print(even)
# print(odd)
# even_sum=0
# for num in range(2,(target+1),2):
#     even_sum+=num
# print(even_sum)

###############################################################################################

# target=int(input("enter target"))
# for num in range(1,(target+1)):
#     if(num%3==0 and num%5==0):
#         print("fizzbuzz")
#     elif(num%3==0):
#         print("fizz")
#     elif(num%5==0):
#         print("buzz")
#     else:
#         print(num)

##########################################################################################
#password genrator
import random

# num=input("enter numbers").split()
# num.append("gogo")
# print(num)

letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','&','*','(',')','+']

num_letter=int(input("how much character you want\n"))
num_digit=int(input("how much digit you want\n"))
num_symbol=int(input("how much symbol you want\n"))

# col_letter='' #empty string

# for char in range(1,num_letter+1):
#     col_letter+=random.choice(letter)

# for char in range(1,num_digit+1):
#     col_letter+=random.choice(digit)

# for char in range(0,num_symbol):
#     col_letter+=random.choice(symbol)

# print(col_letter)

coll_letter=[] #empty list
for char in range(1,num_letter+1):
    coll_letter.append(random.choice(letter))

for char in range(1,num_digit+1):
    coll_letter.append(random.choice(digit))

for char in range(0,num_symbol):
    coll_letter.append(random.choice(symbol))
# print(coll_letter)

password=''
random.shuffle(coll_letter)
for char in (coll_letter):
    password+=char
print("your generated password is :",password)

print("your passwors length is :",len(coll_letter))

