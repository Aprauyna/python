# with open("example.txt","r")as file:
#     print(file.read())

# r' (Read): Use this mode to open a file for reading. You can read data from the file but cannot modify it. If the file doesn't exist, it will raise an error.
# 'w' (Write): Use this mode to open a file for writing. If the file already exists, it will be truncated (emptied). If the file doesn't exist, a new file will be created. Be cautious, as it can overwrite the existing data.
# 'a' (Append): Use this mode to open a file for writing, but the data is added to the end of the file, rather than overwriting it. If the file doesn't exist, a new file will be created.

# 'r+' (Read and Write): Use this mode to open a file for both reading and writing. You can read and write data to the file. If the file doesn't exist, it will raise an error.

# 'w+' (Write and Read): Use this mode to open a file for both writing and reading. If the file already exists, it will be truncated (emptied). If the file doesn't exist, a new file will be created.

# 'a+' (Append and Read): Use this mode to open a file for both appending and reading. You can add data to the end of the file and read from it. If the file doesn't exist, a new file will be created.

# The 'r+', 'w+', and 'a+' modes are useful when you want to perform both reading and writing operations on the same file.

#########################################################
with open("1output.txt","w")as file:
    file.write("hello Arun")

# string=input("enter info to store in file")
# with open("output.txt","w")as file:
#     file.write(string)

# with open("example.txt","r")as file:
#     print(file.read())

#########################################################

# Accept a line of text from the user
# Compare it with the contents of example.txt
# If they are the same, write “Same!” in output.txt file, otherwise write “Different!” in output.txt file

# user_input=input("please enter some text :")

# with open("example.txt","r")as file:
#     content=file.read()
#     print(content)

# result="different"

# if user_input==content:
#     result="same!"

# with open("output.txt","w")as file:
#     file.write(result)
#     file.write(content)

###########################################################
# with open("account.txt","r")as file:
#     for line in file:
#         account=line.strip().split(",")
#         print("Account number :",account[0])
#         print("Account holder :",account[1])
#         print("Acccount balance :",account[2])

###########################################################
# import os

# def create_file(filename):
#     try:
#         with open(filename,"w")as f:
#             f.write("fig big\n")
#         print("file "+filename+" created succesfully")

#     except IOError:
#         print("Error:  could not create file"+filename)


# def read_file(filename):
#     try:
#         with open(filename,"r")as f:
#             content=f.read()
#             print("file content :",content)
#     except IOError:
#         print("error :could not read file "+filename)

# def append(filename,text):
#     try:
#         with open(filename,"a")as f:
#             f.write(text)
#         print("text append to file "+filename+" succesfully")
#     except IOError:
          
# 		   print("Error: could not append to file " + filename)

# def rename_file(filename,new_filename):
#     try:
#           os.rename(filename,new_filename)
#     except IOError:
#          print("error")  

# def delete_file(new_filename):
#      try:
#           os.remove(new_filename)
#           print("file"+new_filename+"delete succesfully")
#      except IOError:
#           print("Error")


# filename="kite.txt"
# new_filename="viko.txt"
# create_file(filename)
# read_file(filename)
# append(filename,"This is some additional text.\n")
# rename_file(filename,new_filename)
# read_file(new_filename)
# delete_file(new_filename)

# Exception handling allows you to gracefully handle errors or exceptional situations 
# This helps your program continue running instead of crashing when an error occurs
# We can handle exceptions using the try, except, else, and finally blocks

# The try block contains the code that might raise an exception
# The except block catches specific exception types and provides a response
# The else block is executed if no exceptions occurred in the try block
# The finally block is always executed, whether an exception occurred or not

# with open("abc.txt","r")as file:
#     # print(file.read())

#     for obio in file:
#         if "hello" in obio:
#             print(obio)
#             with open("giga.xls","a")as file1:
#                 file1.write(obio)
