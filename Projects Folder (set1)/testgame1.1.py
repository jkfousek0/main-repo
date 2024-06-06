
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
p1 = "user"
p2 = "computer"
print("you must be 18 to play")
num = int(input("Age?:"))
print("Age:",num)
if num > 18:
    print("Acceptable") 
else:
    print("Access denided: Reason not over 18")
name = input("enter your name:")
print("Welcome to the world of game1",name)
class Goblin:
    species = 'goblin'
    str = 1
    speed = 3
    agility = 3
    special_skill = 'raiding'
    def discription(self, name):
      return f'{self.name} is cool'
options = "Goblin, plebeian, apperentice mage, merchant, apperentice knight, apperentice archer"
print("select your class:", options)
if input(Goblin):
    print("welcome to the goblin tribe", name)
