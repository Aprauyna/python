# A dictionary is a collection of key-value pairs, where each key is associated with a value
# Dictionaries are written with curly brackets {} and each key-value pair is separated by a colon, i.e. :

# my_dict = {"apple": 3, "banana": 5, "orange": 2}

# Here, apple, banana, and orange are keys with respective values as 3, 5, and 2


# student_data={
#     "arun":258,
#     "ankit":250,
#     "kaka":230,
#     "shivam":260
# }

# for student,marks in student_data.items():
#     print(f"{student.title()} : Total Marks :{marks}")

#Retrieving Values from a Dictionary
# 1) items()    Get keys and values
# 2) keys()     Get only keys
# 3) values()      Get only values

####################################################

# my_dict={'a':1,'b':2,'c':3}

# for key in my_dict:
#     value=my_dict[key]
#     print(f"key:{key} value:{value}")
#####################################################
# my_dict={'a':1,'b':2,'c':3}

# for key,value in my_dict.items():
#     print(f"key:{key} value:{value}")

#####################################################
# student_data={
#     "arun":258,
#     "ankit":250,
#     "kaka":230,
#     "shivam":260
# }

# for value in student_data.values():
#     print(f"total marks :{value}")
##########################################################
# student_data={
#     "arun":258,
#     "ankit":250,
#     "kaka":230,
#     "shivam":260
# }

# for key in student_data.keys():
#     print(f"student data :{key}")

########################################################

# Bank={"Arun":1000,"Ankit":2000}
# for key in Bank.keys():
#     print(f"Account holder name :{key}")

#######################################################

# stock_price={"Apple":148.99,"google":2701.11,"Tesla":791.10,"Amazon":3292.23}

# apple_price=stock_price["Apple"]
# print(apple_price)

# stock_price["google"]=800 #modify stock price

# stock_price["microsoft"]=6000 #add new stock

# del stock_price["Tesla"] #remove tesla from dictionary

# print("stock prices: ")
# for stock,price in stock_price.items():
#     print(f"{stock} : {price}")

########################################################
# bank_account={"1":500,"2":100}
# print("Account information")
# for key,money in bank_account.items():
#     print(f"account no :{key} And acconut balance :{money}")

# bank_account["1"]-=100
# bank_account["2"]+=200
# bank_account["1"]+=300

# for key,money in bank_account.items():
#     print(f"account no :{key} And acconut balance :{money}")

#########################################################

# bank_account={
#     "account_number":987654321,
#     "account_holder":"Arun kumar",
#     "balance":1000
# }

# print(f"Account number : {bank_account['account_number']}")
# print(f"Account holder :{bank_account['account_holder']}")
# print(f"balance :{bank_account['balance']}")

############################################################
#using the get() function

# bank_account={
#     "account_number":987654321,
#     "account_holder":"Arun",
#     "balance":1000.00
# }

# Act_number=bank_account.get("account_number","Not available")
# Act_holder=bank_account.get("account_holder","not avilable")
# balance=bank_account.get("balance",0.0)

# print(f"current Account number :{Act_number}")
# print(f"current Account holder :{Act_holder}")
# print(f"curent balance :{balance}")

##############################################################

# pizzas={
#     "crust":"thick",
#     "topping":["mushroom","extra cheese"]
# }

# print(f"you ordered {pizzas['crust']}-cust pizza with the following toppings:")
# for top in pizzas["topping"]:
#     print(f"\t{top}")

########################################################
# users ={
#     "Aeinstein":{"first":"albert","last":"einstein","location":"princeton"},
#     "mcurie":{"first":"marie","last":"curie","location":"paris"}
# }

# for user_name,user_info in users.items():
#     print("username :"+user_name)
#     full_name=user_info["first"]+" "+user_info["last"]
#     location=user_info["location"]

#     print("\tFull name :"+full_name)
#     print("\tLocation :"+location)

#########################################################

student_database = {}

# Add students to the database
student_database["Alice"] = {"age": 20, "subjects": ["Math", "Science", "History"]}
student_database["Bob"] = {"age": 21, "subjects": ["English", "Math", "Physics"]}
student_database["Charlie"] = {"age": 19, "subjects": ["Biology", "Chemistry", "Geography"]}

student_name=input("enter the student name of the student you want to view:")
if student_name in student_database:
    student_info=student_database[student_name]
    print(f"student name :{student_name}")
    print(f"Age :{student_info['age']}")
    print("Subjects :",",".join(student_info["subjects"]))
else:
    print("student not found")


#for update the age of student

student_name=input("enter the name of student you want to update:")
if student_name in student_database:
    new_age=int(input("enter age"))
    student_database[student_name]["age"]=new_age
    print(f"{student_name}'s age has been uodated to {new_age}")
else:
    print("student not found in database")

#add subjects to record student

student_name=input("enter the name of student to add subject to :")
if student_name in student_database:
    new_subject=input("enter new subject").split()
    student_database[student_name]["subjects"].extend(new_subject)
    print(f"Added {','.join(new_subject)} to {student_name}")

#remove student data from database

student_name=input("enter student name to remove from database")
if student_name in student_database:
    del student_database[student_name]
    print(f"{student_name} remove from database")
else:
    print("name not found")

#final output
for student_name,details in student_database.items():
    print(f"Student Name : {student_name}")
    print(f"Age : {details['age']}")
    print(f"Subjects : {','.join(details['subjects'])}")
