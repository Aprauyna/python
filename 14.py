import random
from data import data
from art import logo,VS
# from art import VS
score=0

def format_data(account):
    account_n=account["name"]
    account_d=account["description"]
    account_c=account["country"]

    return f"{account_n} {account_d} from {account_c}"

def compare(guess,a_account_follower_count,b_account_follower_count):
    if guess=="a":
        if a_account_follower_count>b_account_follower_count:
            return True
        else:
            return False
    elif guess=="b":
        if b_account_follower_count>a_account_follower_count:
            return True
        else:
            return False
        
#making game repeatable
account_b=random.choice(data)
end=False
while not end:
    #display art
    print(logo)
    #genrate a random account from the game data

    account_a=account_b
    account_b=random.choice(data)
    while account_a==account_b:
        account_b=random.choice(data)
    #format the account data into printable format
    print(f"compare A: {format_data(account_a)}\n")
    print(VS)
    print(f"Against B:{format_data(account_b)}")



    #ask user for a guess
    guess=input("who has more follower? A or B\n").lower()

    #check if user is correct
    #get follower count of each account
    a_account_follower_count=account_a['follower_count']
    b_account_follower_count=account_b['follower_count']
    #use if statement to check if user is correct
    answer=compare(guess,a_account_follower_count,b_account_follower_count)
    if answer:
    #score keeping
        score+=1
    #give user feedback on their guess
        print(f"your score is {score} keep going\n")
    else:
        print(f"sorry thats wrong,and your final score is {score}\n")
        end=True






    #making account at position B become the next account at position A

    #clear the screen between rounds
