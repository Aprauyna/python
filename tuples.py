#A tuple in Python is similar to a list, but it is immutable, meaning its values cannot be changed
#Tuples are written with parentheses () and each item is separated by a comma
#We can store data belonging to any data type in a tuple, including mixed data (i.e. some numbers, some text, etc)
#Declaring a tuple: my_tuple = (1, 2, 3, 4, 5)

bank_account=("Arun",50100303982474,1000)

print("Account Name :",bank_account[0])
print("Account number :",bank_account[1])
print("Account balance :",bank_account[2])

#we can't change the value of tuple,but tuple work like as list,so it can access through indexing
# bank_account[2]-=500
# print("Account balance :",bank_account[2])


shopping_cart=("shirt","pants","shoes","hat","socks")
print(shopping_cart)

for item in shopping_cart:
    print("-"+item)