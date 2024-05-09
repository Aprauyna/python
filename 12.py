#namespace local vs global scope

#any  thing we given name is called namespace like local scope variable and globale scope variable

#block scope means variable defined in if ,while,for code block is the same as outside it

#modify global scope

# num=1

# def fun():
#     global num  #here we modify globle variable
#     num+=3
#     print(f"value of variable is {num}")

# fun()
# print(f"variable value {num}")

###############################################
# num=1

# def fun():
#     num=5
#     print(f"value of variable is {num}")

# fun()
# print(f"variable value {num}")

################################################
# EASY_LEVEL=5
# HARD_LEVEL=3

# def check_answer(guess,answer,turns):
#     if guess>answer:
#         print("too high")
#         return turns-1
#     elif guess<answer:
#         print("too low")
#         return turns-1
#     else:
#         print("you guess right")

# def set_difficulty():
#     level=input("enter difficulty type easy or hard\n")
#     if level=="easy":
#         return EASY_LEVEL
#     else:
#         return HARD_LEVEL

# import random
# print("welcome to the gusseing number game\n")
# print("i'm thinking number between 1 to 100\n")
# answer=random.randint(1,100)
# print(f"the correct answer is {answer}")

# turns=set_difficulty()


# guess=0
# while answer!=guess:
#     guess=int(input("enter number\n"))
#     print(f"you have {turns} attempts\n")
#     turns=check_answer(guess,answer,turns)
#     if turns==0:
#         print("you loose")
#         exit(1)

import random
EASY=5
HARD=3
def set_difficulty():
    level=input("enter level easy or hard\n")
    if level=="easy":
        return EASY
    else:
        return HARD

def fun(answer,guess,turn):
    if guess>answer:
        print("too high")
        return turn-1
    elif guess<answer:
        print("too low")
        return turn-1
    else:
        print("you got right guesss")
print("welcome to the guess number game\n")
print("numbers metween 1 to 100\n")
answer=random.randint(1,100)
print(f"you answer should be {answer}")

def call():
    turn=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turn} attempt\n")
        guess=int(input("enter number guess that number\n"))
        turn=fun(answer,guess,turn)
        if turn==0:
            print("you loose")
            return


call()
