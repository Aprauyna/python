#string
print("hello"[4])

print("123"+"345") #"" behave like a string

#integer

print(123_345)

#float

print(3.14569)

#boolean

True
False

#if we use len() with integer we got error,len fun not work with number example

# print(len(12345))

#use of type()

num_char=len(input("enter your name\n"))
print(type(num_char))
#we got error if we write code like this because here string concate with integer
# print("your name has "+num_char+" character")
#so we write through typecasting in string,here num_char object convert into string by str
new_num_char=str(num_char)
print("your name has "+new_num_char+" character")

a=123
print(type(a))

a=float(123)
print(type(a))

print(70 + float("123"))
print(str(70)+str(123))

############################################################################

two_digit_number=input("enter two digit number\n")
print(type(two_digit_number))
#we know,we use in string subscript
first_digit=int(two_digit_number[0])
second_digit=int(two_digit_number[1])
print(first_digit+second_digit)

##############################################################################

#priority PEMDAS

3+2
2-2
3*2
3/2 #behave default as float
3**2 #3 power 2
##############################################################################

height=float(input("enter height\n"))
weight=int(input('enter weight\n'))

# height1=height**2
# print(height1)

BMI=weight/(height**2)
print(type(BMI))
BMI1=int(BMI)
print(BMI1)

###############################################################################
print("\n")
print(8/3)
print(round(8/3))
print(round(8/3,2))
print(int(8/3))
print(type(8//3))

#use of f string,here bnifit is we dont want convert different datatype into string

score=0
height=1.65
iswinning=True
print(f"your score is {score} and your height is {height} is it {iswinning}")

#####################################################################################
age=input()
year=90-int(age)
weeks=year*52
print(f"you have {weeks} left.")

