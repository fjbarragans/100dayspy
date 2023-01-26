#Rock, paper and scissors
import random
election = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors? "))
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
options = [rock, paper, scissors]
computer = random.randint(0,2)

print(f"You choose {options[election]} \n Computer chose {options[computer]}")

if election == computer:
    print("Draw")
elif election - computer == 1:
    print("You win")
elif election == 0 and computer == 2:
    print("You win")
else:
    print("You lose")