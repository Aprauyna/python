a="Arun"
b="kumar"
print(a+" "+b)

# chr()=Convert an integer to a character print(chr(97)) will give ‘a’
# ord()=Convert a character to an integer print(ord(‘a’)) will give 97
# len()=Return the length of a string print(len(‘Hello’)) will give 5
# str()=Return the string representation of an object a = str(49.2) will give ‘49.2’

print(chr(97-32)) #output A
print(ord("a"))   #output 97

#####################################################
# string indexing

# In Python, strings are ordered sequences of character data, and thus can be indexed

string="Helo"
for char in string:
    print(char)

for i in range(len(string)):
    print(string[i])

print(string[3])
print(string[0])


#negative string indexing

letter=input('enter string :')
print(letter[-1])
print(letter[-3])
print("\n")


#################################################
#String Slicing

# Python also allows a form of indexing syntax that extracts substrings from a string, known as string slicing

string=input("enter character :")
length=len(string)
print(string[0:length])
print(string[2:length])
print(string[:1])
print(string[:2])
print(string[:3])
print(string[0:3])
print(string[1:])
print(string[2:])
print(string[3:])

s="hello"
print(s[0:5:2])
print(s[1:5:3])
############################################

#Modifying Strings
# Python Strings are immutable, which means we cannot modify them

s="Hello"
# s[1]="T" erroe 
#we can use following techniques
s=s.replace("e","T")
print(s)

s=s.replace("o","K")
print(s)
###############################################
#More String Methods

# Many other string functions exist, such as:
# Case conversion: capitalize(), lower(), upper(), title()
# Find and replace: count(), endswith(), startswith(), find(), replace()
# Character classification: isalnum(), isalpha(), isdigit(), islower(), isupper()

##########################################################



