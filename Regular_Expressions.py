# Specify a set of characters that we want to match
# Called pattern matching
# Example: Ensure emp ID is of type A-999, Validate email id, Ensure PRN number does not contain a non-digit

# [abc] - Matches any character that is either a, b, or c.
# [a-z] - Matches any lowercase alphabetic character from a to z.
# [A-Z] - Matches any uppercase alphabetic character from A to Z.
# [0-9] - Matches any digit from 0 to 9.
# [a-zA-Z0-9] - Matches any alphanumeric character.
# [^abc] - Matches any character that is not a, b, or c.
# [^a-z] - Matches any character that is not a lowercase alphabetic character from a to z.

##########################################################
# import re

# while True:
#     user_input=input("enter number:")
#     # ^ is start of the string, $ is the end of the string, + is one or more characters
#     if re.match('^\d+$',user_input):
#     #if re.match("^[0-9]+$",user_input):
#         break
#     else:
#         print("invalid input")

# print("you entered a valid numeric value:",user_input)

##########################################################
#A-999

# import re
# while True:
#     emp_id=input("enter employee id(A-999 pattern):")

#     if re.match('^[A-Z]-\d{3}+$',emp_id):
#         break
#     else:
#         print("invalid input")
# print("you enter valid employee id:",emp_id)

############################################################
#Accept amount from the user strictly in the 9,99,999 format.
# import re

# while True:
#     user_input=input("Accept amount from the user strictly in the 9,99,999 format:")
#     # if re.match('^\d{1},\d{2},\d{3}',user_input):
#     if re.match('^[0-9]{1},[0-9]{2},[0-9]{3}+$',user_input):
#         break
#     else:
#         print("invalid input")

# print("you entered input:",user_input)

###########################################################
#Accept bill amount only in 999.99 format

# import re

# while True:
#     amount=input("Enter a bill amount (999.99 format):")
#     if re.match('^\d+\.\d{2}',amount):
#         break
#     else:
#         print("invalid input")
# print('you entered:',amount)

##########################################################
# import re

# text = "12345 abc 6789 xyz 42"

# # Define a regex pattern to match numbers
# pattern = r'\d+'

# # Search for numbers in the text
# matches = re.findall(pattern, text)

# # Print the matches
# for match in matches:
#     print(match)



