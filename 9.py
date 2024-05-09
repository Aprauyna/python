#########################################dictionary#########################

# dictionary have key and value{"key":"value","loop":"pool"}

# programming_dictionary={
#     "key":"value",
#     "loop":"pool"
#     }

# print(programming_dictionary["key"])


# list=["key","loop"]
# print(list[0])
# list="pool"
# print(list[0])

#if we want to adding new item in dictionary

# programming_dictionary["kite"]="vivo"
# print(programming_dictionary)

#creat empty dictionary
# dic={}

#how can we wiped exiting dictionary
# programming_dictionary={}
# print(programming_dictionary)

#editing the dictionary

# programming_dictionary["kite"]="oppo"
# print(programming_dictionary)

#loop through dictionary and list

# list=["Arun","Kaka","nandan"]
# for name in list:
#     print(name)
# print(len(list))
# for int in range(len(list)):
#     print(list[int])

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#     print(len(programming_dictionary))

# for int in range(len(programming_dictionary)):#error
#     print(programming_dictionary[int])

##################################################################################################################

# student_score={
#     "Arun":95,
#     "kaka":100,
#     "nandan":99,
#     "shivam":100,
#     "ravan":17
#     }

# student_grade={}

# for student in student_score:
#     score=student_score[student]
#     if score > 90:
#         student_grade[student]="outstanding"
#     elif score > 80:
#         student_grade[student]="exceed exception"
#     else:
#         student_grade[student]="fail"

# print(student_grade)

######################################################################################################################

#nesting

capital={
    "INDIA":"new delhi",
    "France":"Paris",
    "Germany":"Berlin"
}

#nesting list in dictionary

country={
    "INDIA":["pune","mumbai","prayagraj",["banare","punchvati"]], #each key only one value,nesting list into list
    "Germany":["Berlin","hamburge"]
}

#nesting dictonary in dictionary
country={
    "INDIA":{
        "visited_place":["pune","mumbai","prayagraj",["banare","punchvati"]],
             "total_place_visited":15
             }, #each key only one value,nesting list into list
    "Germany":["Berlin","hamburge"]
}

#nesting dictionary in list

country=[
    {
        "India":{"visited_place":["pune","mumbai"],"total_visited":15},
    },
    {
        "Germany":["berlin","hamburge"]
    }
]  

############################################################################################################3
#travel vlog

# def new_city(country,visited,cities):
#     new_log={}
#     new_log["country"]=country
#     new_log["visit"]=visited
#     new_log["city"]=cities
#     travel_log.append(new_log)


# country=input("enter country\n")
# visited=int(input("how many time you visite\n"))
# cities=input("list which cities you tarveled\n").split()
# travel_log=[]
# # cities=eval(input())
# new_city(country,visited,cities)
# print(f"{travel_log[0]['country'],travel_log[0]['visit'],travel_log[0]['city'][1]}")

######################################################################################################
# auction game
# details={}
# def auction(name,bidding_price):
#     details[name]=bidding_price
#     print(details)

# not_end=False
# while not not_end:
#     name=input("entre name\n")
#     bidding_price=int(input("enter bidding amount\n"))
#     cond=input("enter you want bidding or not for yes and no\n")
#     if cond=="yes":
#         auction(name,bidding_price)
#     elif cond=="no":
#         list=[]
#         for bid in details:
#             list.append(details[bid])
#         max_bid=max(list)
#         print(list)
#         print(max_bid)
#         not_end=True


