import random
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
# player = random.choice([1,2,3])
player = int(input("What do you choose?, Type 1 for Rock, 2 for paper and 3 for Scissors "))
if player == 1:
    print(f"You Chose \n {rock}")
elif player == 2:
    print(f"You Chose \n {paper}")
else:
    print(f"You Chose \n {scissors}")

machine = random.choice([1,2,3])
if machine == 1:
    print(f"Machine Chose \n {rock}")
elif machine == 2:
    print(f"Machine Chose \n {paper}")
else:
    print(f"Machine Chose \n {scissors}")

if (player == 1 and machine == 1) or (player == 2 and machine == 2) or (player == 3 and machine == 3):
    print("Game Draw")
elif (player == 1 and machine == 2) or (player == 2 and machine == 3) or (player == 3 and machine == 1):
    print("You Lost")
elif (player == 1 and machine == 3) or (player == 2 and machine == 1) or (player == 3 and machine == 2):
    print("You Win!")

