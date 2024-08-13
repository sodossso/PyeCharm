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
person=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if person==0:
    print(rock)
elif person==1:
    print(paper)
elif person==2:
    print(scissors)
else:
    print("You typed an invalid number, you lose! ")
    exit()

print("Computer chose:")
import random
computer_choices=[rock,paper,scissors]
computer=random.choice(computer_choices)
print(computer)
index_computer=computer_choices.index(computer)

if  person==index_computer:
    print("It's a draw!")
elif person==0 and index_computer==1:
    print("You lose!")
elif person==1 and index_computer==2:
    print("You lose!")
elif person==2 and index_computer==0:
    print("You lose!")
elif person>=3 or person<0:
    print("You lose! ")
else:
    print("You win!")
