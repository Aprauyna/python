#set

#A set is an unordered collection of unique elements
# Sets are defined using curly braces {} or the set() function

my_prn_set={1,2,3,4,5}

#creating set
fruits={"Banana","Apple","Cherry"}
print(fruits)

#adding an element to the set
fruits.add("Orange")

#removing an element fro set
fruits.remove("Cherry")

#checking element is in set
is_mango_present="Apple" in fruits
print(is_mango_present)

## Iterating through the set
for fruit in fruits:
    print(fruit)


# Finding the length of the set
lenght=len(fruits)
print(lenght)

## Creating a new set with some common elements
vegetables = {"carrot", "potato", "Apple"}

# Finding the intersection of two sets
common_element=fruits.intersection(vegetables)
print(common_element)

# Combining two sets (union)
all_combine=fruits.union(vegetables)
print(all_combine)

# Creating an empty set
empty_set = set()

print("fruits :",fruits)
print("numbrr_of_fruits:",lenght)

###########################################################
account_types={"checking","saving","credit","investment"}

account=input("enter account type: checking,saving,credit,investment =")
for accounts in account_types:
    if account in account_types:
        print(account)
        break

#add new account type
account_types.add("money market")

print(account_types)

#print out update account type
print("updated account type:")
for type in account_types:
    print(type)
