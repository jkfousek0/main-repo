#-- key:
rock = 'rock'
paper = 'paper'
scissors = 'scissor'
R = rock
P = paper
S = scissors
#-- end key:
#-- start
print("3...")
print("2...")
print("1...")
print("GO!")
player_1 = "player_1"
player_2 = "player_2"
import random
elements = ['rock', 'paper', 'scissors']
random_choice = random.choice(elements)
print("player_1", random_choice)
random_choice = random.choice(elements)
print("player_2", random_choice )
if random_choice is R and R:
    print('TIE!.')
if random_choice is R and S:
    print('player_1 wins!.')
if random_choice is R and P:
    print('player_1 losses!')
