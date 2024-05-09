# Function: A function is block of code that is reusable

# def add_numbers(a, b, c):
#     sum = a + b + c
#     print("The sum of ",  a, " + ", b, " + ", c, " is: ", sum)
#     return sum

# result = add_numbers(5, 10, 15)
# print("The result is: ", result)

# result = add_numbers("5", '10', "15")
# print("The result is: ", result)

#error
# result = add_numbers(5, '10', "15")
# print("The result is: ", result)

##########################################

# def fun(num,num1,operator):
#     if operator=='+':
#         return num + num1
#     elif operator=='-':
#         return num - num1
#     elif operator=='/':
#         return num / num1
#     if operator=='*':
#         return num * num1
#     if operator=='%':
#         return num % num1


# num=int(input("enter number :"))
# num1=int(input("enter second number :"))
# operator=input("enter operator :")
# output=fun(num,num1,operator)
# print(output)

###########################################
# def accept():
#     n1=int(input("enter first number"))
#     n2=int(input("enter second number"))
#     n3=input("enter operator")
#     return n1,n2,n3

# def cal(num,num1,operator):
#     if operator=='+':
#         return num + num1
#     elif operator=='-':
#         return num - num1
#     elif operator=='/':
#         return num / num1
#     if operator=='*':
#         return num * num1
#     if operator=='%':
#         return num % num1


# n1,n2,n3=accept()
# result=cal(n1,n2,n3)
# print("The result :",result)

##############################################
# def cal(sal,bonus):
#     return sal+bonus


# salary=5000
# bonus=1000
# total_salary=cal(salary,bonus)
# print(total_salary)

#################################################
# def convert(string):
#     return string.upper()

# string =input("enter string")
# upper=convert(string)
# print("original string :",string)
# print("upper case string :",upper)

###################################################

# Write a Python program that creates an empty student dictionary
# The program should have a function add_student_record() to add a record to the student dictionary
# Call the function three times to add three student records

# student_record={}

# def add_student_record():
#     student_id=int(input("enter student id:"))
#     name=input("enter student name:")
#     grade=input("enter grade:")
#     student_record[student_id]={"Name":name,"Grade":grade}
#     print("student record added sucessfully\n")

# def display_record():
#     if student_record:
#         for student_id,record in student_record.items():
#             print(f"Student Id :{student_id}")
#             print(f"Name :{record['Name']}")
#             print(f"Grade :{record['Grade']}")
#             print("\n")

# add_student_record()
# add_student_record()
# display_record()
###########################################################
# Perform the following operations on a dictionary of student records:
# Accept and store a student record in the dictionary
# Edit an existing student record
# Delete a student record
# Display all student records

student_record={}

# Function to accept and store a student record
def add_record():
    student_id=int(input("enter student ID"))
    Name=input("enter student name")
    Grade=input("enter student grade")
    student_record[student_id]={"Name":Name,"Grade":Grade}
    print("student record succesfully")

#Function to edit an existing student record

def edit_student_record():
    student_id =int(input("enter student ID to edit:"))
    if student_id in student_record:
        print("current record")
        print(f"Student ID :{student_record[student_id]}")
        print(f"student name :{student_record[student_id]['Name']}")
        print(f"student grade :{student_record[student_id]['Grade']}")
        new_name=input("enter name(leave empty to keep current)")
        new_grade=input("enter new grade(leave empty to keep current)")
        if new_name:
            student_record[student_id]["Name"]=new_name
        if new_grade:
            student_record[student_id]["Grade"]=new_grade
        print("student record update succesfully")
    else:
        print("student id not found")

# Function to delete a student record
def delete_student_record():
    student_id=int(input("enter student id for delete"))
    if student_id in student_record:
        del student_record[student_id]
    else:
        print("student id not found in student record")

#Function to display all student records

def display_all_record():
    if student_record:
        print("student Records:")
        for student_id,record in student_record.items():
            print(f"student id :{student_id}")
            print(f"Name :{record['Name']}")
            print(f"student Grade :{record['Grade']}")
    else:
        print("record not found")

while True:
    print("\nStudent Record Menu:")
    print("1. Add Student Record")
    print("2. Edit Student Record")
    print("3. Delete Student Record")
    print("4. Display All Records")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice == '1':
        add_record()
    elif choice == '2':
        edit_student_record()
    elif choice == '3':
        delete_student_record()
    elif choice == '4':
        display_all_record()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
