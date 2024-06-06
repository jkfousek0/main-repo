
import random

options =("rock","paper","scissors")
player = None
computer = random.choice(options)
if player not in options: 
  player = input("enter a choice (rock, paper, scissors): ")
                
print(f"player: {player}")
print(f"computer: {computer}")              

