import random
ROCK, PAPER, SCISSORS:

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#rock = 0
#paper = 1
#scissors = 2
#names=rock,paper,scissors
images = [rock,paper,scissors]

choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
print(f"you chose {choice}")
if choice >=3:
  print("you are out of range, you lose!")
else:
  print(images[choice])
import random
computer = random.randint(0,2)
print(f"computer chose {computer}")
#computer = random.choice(names)
print(images[computer])


if choice == 0 and computer == 2:
  print("you won!")
elif choice == 2 and computer == 1:
  print("you won!")
elif choice == 1 and computer == 0:
  print("you won")
elif choice == computer:
  print("its a draw ")
else:
    print("you lose!")
