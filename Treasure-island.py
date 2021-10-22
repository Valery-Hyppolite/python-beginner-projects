Tresure island Game

print("Welcome to the treasure island!\nYour mission is to find the treasure.\nGood luck! ")

LR = input(" You\'re at a crossroad, where do you want to go 'left' or 'right'?\n").lower()

if LR == "right":
    print("fall into a hole, Game Over. :( ")
else:
    swim_or_wait = input(" You\'ve come to the lake. There is an island in the middle of the lacke, what do you wan to do?\n ")
    SW = swim_or_wait.lower()
    if SW == "swim":
        print(" Attacked by trought. Game over")
    else:
        door = input(" You arrived at the island safely. There are 3 doord, which door would you like to go through, red,yellow or blue?\n")
        D = door.lower()
        if D == 'Red':
            print("Burn by fire.Game Over.")
        elif D == 'blue':
            print("Eating by beasts. Game Over")
        elif D == 'yellow':
            print("You Win!!!")
        else:
            print("Game Over")
