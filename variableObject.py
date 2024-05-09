# #floor division

# a=11
# b=2
# c=a//b
# print(c)

# #Exponenttation

# a=2
# b=3
# c=b**2
# print(c)

# #modulus

# a=11
# b=2
# c=a%b
# print(c)

###############################################
#  Dynamically Typed
# Python is dynamically typed, meaning that we do not need to explicitly declare the data type of a variable
# The interpreter determines the data type based on the value assigned to the variable
# Memory allocation to variables has the following aspects (although they are hidden from the programmer):
# Object creation
# Reference counting
# Garbage collection
# Memory pools

###################################################
# Object Creation

# When we create a new object (e.g., by assigning a value to a variable), Python dynamically allocates memory to store that object's data
# The size of the allocated memory depends on the type and structure of the object (e.g., an integer, a string, a list)

##################################################
#Reference Counting

# Python uses reference counting to keep track of how many references (variables or data structures) point to a particular object
# Every object has an associated reference count that is incremented when a reference to the object is created and decremented when a reference is deleted

################################################
# Garbage Collection

# Python's garbage collector periodically identifies and reclaims memory occupied by objects that are no longer reachable (i.e., their reference count drops to zero)
# Circular references (objects referencing each other in a loop) are also managed by the garbage collector, as reference counting alone cannot handle these cases

####################################################
# Memory pools

# Python uses memory pools to efficiently manage memory allocation for small objects
# Memory pools help reduce the overhead of frequently allocating and deallocating small chunks of memory
# Objects of similar sizes are grouped into memory blocks within these pools

##########################################################
# Variables

# No need to declare data type
# The interpreter determines the data type based on the value assigned to the variable
# Variable naming: Must start with A-Z or a-z or underscore, then we can have alphanumeric characters or underscores
# Variables are case-sensitive and should not be the same as Python keywords
# Because of dynamic typing, this is allowed:
# x = 10
# x = “Hello”

#########################################################
# Naming Conventions

# Snake Case should be used for functions and variable names
# Words are separated by underscores.
# Example: number_of_college_graduates

# Pascal Case should be used for class names
# Identical to Camel Case, except the first word is also capitalized.
# Example: GraduateStudent

######################################################
# variable refrences

n=300 #This assignment creates an integer object with the value 300 and assigns the variable n to point to that object

m=n #Python does not create another object. It simply creates a new symbolic name or reference, m, which points to the same object that n points to.

m=400 #Now Python creates a new integer object with the value 400, and m becomes a reference to it

n="test" #now 300 is orphand object

# When the number of references to an object drops to zero, it is no longer accessible
# At that point, its lifetime is over – it becomes orphan
# Python will eventually notice that it is inaccessible and reclaim the allocated memory so it can be used for something else
# This process is referred to as garbage collection

#####################################################

# A literal is a notation for representing a fixed value in code
# Does not require any computation or evaluation
# Examples:
# Numeric literals: integers, floating-point numbers, and complex numbers, such as 123, 3.14	
# String literals: sequences of characters enclosed in quotes, such as "Hello, World!" or 'Python'
# Boolean literals: the values True and False
# None: a special value that represents the absence of a value.
# List literals: a sequence of comma-separated values enclosed in square brackets, such as [1, 2, 3].
# Dictionary literals: a sequence of key-value pairs enclosed in curly braces, such as {'a': 1, 'b': 2, 'c': 3}

#####################################################

# my_string="hello\"world\""
# print(my_string)

######################################################
#operators

# Arithmetic(+,-,*,/,//,%,**)
# Assignment(=,+=,-=,*=,/=,%=,//=,**=)
# Comparison(==,!=,<,>,<=,>=)
# Logical
# Membership(is in)
# Bitwise


# Identity is a comparison between two objects to see if they refer to the same memory location
# Determined using the "is" operator

a=[1,2,3]
b=a
# If we create a new object that has the same value as a, but is a different object in memory, the is operator will return False:
c=[1,2,3]
print(a is b)
print(b is a)
print(b is c)

# If we want to compare the values in the two lists, we should use the == operator
print(a==c)
print(c==b)

#using in operator
flag=0
list1=[1,2,3,4]
list2=[5,6,3,8]
for item in list1:
    if item in list2:
        flag=0
        break
    else:
        flag=1
        

if flag==0:
    print("overlapping")
else:
    print("not overlapping")

#########################################
#bitwise operator

# Bitwise AND (&)
a = 10     # 1010 in binary
b = 6      # 0110 in binary
c = a & b  # 0010 in binary
print(c)   # Output: 2

# Bitwise OR (|)
a = 10     # 1010 in binary
b = 6      # 0110 in binary
c = a | b  # 1110 in binary
print(c)   # Output: 14

# Bitwise XOR (^)
a = 10     # 1010 in binary
b = 6      # 0110 in binary
c = a ^ b  # 1100 in binary
print(c)   # Output: 12

# Bitwise NOT (~)
a = 10      # 1010 in binary
b = ~a      # -11 in decimal (11110101 in binary)
print(b)    # Output: -11

# left shift(<<)

a=10
b=(a<<1)
print(b)

#right shift(>>)

a=10
b=(a>>1)
print(b)
################################################
#logical operator(and,or,not)

x=5
y=10
if x > 3 and y < 15:
    print("Both conditions are True")
if x > 3 or y > 15:
    print("At least one condition is True")
if not(x > 3):
    print("The condition is False")

#################################################





