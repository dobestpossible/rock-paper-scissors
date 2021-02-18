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
import random

def game(choice):
  comp = random.randint(0, 3)
  if choice == comp and comp == 0:
    print(f"{rock}\nGame is a draw")
  elif choice == comp and comp == 1:
    print(f"{paper}\nGame is a draw")
  elif choice == comp and comp == 2:
    print(f"{scissors}\nGame is a draw")
  elif choice == 0 and comp == 1:
    print(f"{paper}\nYou lost")
  elif choice == 0 and comp == 2:
    print(f"{scissors}\nYou won")
  elif choice == 1 and comp == 0:
    print(f"{rock}\nYou won")
  elif choice == 1 and comp == 2:
    print(f"{scissors}\nYou lost")
  elif choice == 2 and comp == 0:
    print(f"{rock}\nYou lost")
  elif choice == 2 and comp == 1:
    print(f"{paper}\nYou won")


user = input("Let's play Rock, Paper, Scissors!\nWhat do you choose? Type:\n0 for Rock\n1 for Paper\n2 for Scissors\n")



try:
  use = int(user)
  if use in range(0, 3):
    game(use)
  else:
    print("Only 0, 1, or 2 are valid choices. Please try again.")
except ValueError:
   print("Only 0, 1, or 2 are valid choices. Please try again.")


