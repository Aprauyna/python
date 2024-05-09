import random

name=["arun","kaka","nandan"]

choose=random.choice(name)
print(choose)

display=[]
for char in range(len(choose)):
    # display.append("_")
    display+=("_")
print(display)

end_of_game = False

while not end_of_game:
    guess=input("enter letter\n").lower()

    for position in range(len(choose)):
        letter=choose[position]
        if letter==guess:
            display[position]=letter
    print(display)

    if "_" not in display:  #in keyword particuraly check the element exits in list
        end_of_game=True
        print("you win")


