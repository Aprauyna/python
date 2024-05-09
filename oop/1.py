# Object-oriented programming (OOP) is based on the concept of objects, which can contain data and code to manipulate that data. In Python, everything is an object, including built-in data types like strings, integers, and lists.
# Main OOP principles:
# Encapsulation: This refers to the practice of hiding the implementation details of an object from the outside world, and only exposing a public interface that can be used to interact with the object.
# Inheritance: This refers to the ability to create new classes that are a modified version of an existing class, inheriting the attributes and methods of the parent class.
# Polymorphism: This refers to the ability of objects to take on multiple forms, based on their context or the methods that are being called on them.



# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def sayhello(self):
#         print("my name is ",self.name, "and my age is ",self.age)


# name=input("enter name:")
# age=int(input("enter age:"))
# person1=Person(name,age)
# person1.sayhello()

#####################################################
# Create a Student class that has name, age, student_id and list of subjects as its attributes
# Create two objects of this student class and display their information

# class Student:
#     def __init__(self,name,age,student_id):
#         self.name=name
#         self.age=age
#         self.student_id=student_id
#         self.subjects=["operating system","computer Architecure"]

#     def dis_info(self):
#         print(f"Name :{self.name}")
#         print(f"Age :{self.age}")
#         print(f"Student id :{self.student_id}")
#         print(f"subjects :{','.join(self.subjects)}")
# name=input("enter name :")
# age=int(input("enter age :"))
# id=int(input("enter student id :"))
# student1=Student(name,age,id)
# student2=Student("Bob",22,2)

# print(student1.name)
# print(student2.subjects)
# print("\n")
# student1.dis_info()
# print("\n")
# student2.dis_info()
####################################################
# class Student:
#     def __init__(self,name,age,student_id):
#         self.name=name
#         self.age=age
#         self.student_id=student_id
#         self.subjects=["Agricuture","operating system"]

#     def dis_info(self):
#         print("Name :",self.name)
#         print("Age :",self.age)
#         print("Student id :",self.student_id)
#         print("Subjects :",','.join(self.subjects))

# stu1=Student("Arun",22,1)
# stu2=Student("sam",33,2)
# print(stu1.name)
# print(stu2.age)
# print("\n")
# stu1.dis_info()
# stu2.dis_info()

#################################################

# Class Student: Student id, name and list of results; has methods to add and retrieve results
# Class Result: Represents a subject and the corresponding marks
# Create a Student object, add results to it, and then print the student information and results


