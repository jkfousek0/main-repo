
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
    print('Access denided: Reason not over 18')
    
name = input("enter your name:")
print("Welcome to the world of DnD ripoff",name)
p1 = name
char1 = "goblin"
import random
random_6 = random.randint(1, 6)
race = input()
class char1:
    def __init__(self,name,vitality,health,strength,speed,stamina,luck,magic):
        self.name = char1
        self.vitality = 1
        self.health = 10
        self.strength = 1
        self.speed = 3
        self.stamina = 3
        self.luck = 0
        self.magic = 0
        self.inventory = ("wooden spear","knife")
    def attack(self, other):
        dice = dice(0)
        dice6 = dice(6)
        dice6.roll = random_6
        self.attack = self.strength + random_6
        damage = max(0, self.attack_strength - other.defense)
        
char2 = "human"
class char2:
    def __init__(self,name,vitality,health,strength,speed,stamina,luck,magic):
        self.name = char2
        self.vitality = 1
        self.health = 20
        self.strength = 1
        self.speed = 3
        self.stamina = 3
        self.luck = 0
        self.magic = 0
        self.inventory = ("pitch fork","knife")
    def attack(self, other):
        dice = dice(0)
        dice6 = dice(6)
        dice6.roll = random_6
        self.attack = self.strength + random_6
        damage = max(0, self.attack_strength - other.defense)
char3 = "mage"
class char3:
    def __init__(self,name,vitality,health,strength,speed,stamina,luck,magic):
        self.name = char3
        self.vitality = 1
        self.health = 20
        self.strength = 1
        self.speed = 3
        self.stamina = 3
        self.luck = 0
        self.magic = 0
        self.inventory = ("staff","bad book")
    def attack(self, other):
        dice = dice(0)
        dice6 = dice(6)
        dice6.roll = random_6
        self.attack = self.strength + random_6
        damage = max(0, self.attack_strength - other.defense)
char4 = "oger"
class char4:
    def __init__(self,name,vitality,health,strength,speed,stamina,luck,magic):
        self.name = char4
        self.vitality = 1
        self.health = 20
        self.strength = 1
        self.speed = 3
        self.stamina = 3
        self.luck = 0
        self.magic = 0
        self.inventory = ("large club","loin cloth")
    def attack(self, other):
        dice = dice(0)
        dice6 = dice(6)
        dice6.roll = random_6
        self.attack = self.strength + random_6
        damage = max(0, self.attack_strength - other.defense)
char5 = "elfs"
class char5:
    def __init__(self,name,vitality,health,strength,speed,stamina,luck,magic):
        elements = ['fire', 'strength', 'speed', 'heal']
        random_choice = random.choice(elements)
        self.name = char5
        self.vitality = 1
        self.health = 20
        self.strength = 1
        self.speed = 3
        self.stamina = 3
        self.luck = 0
        self.magic = 0
        self.inventory = random_choice; 'potion'
    def attack(self, other):
        dice = dice(0)
        dice6 = dice(6)
        dice6.roll = random_6
        self.attack = self.strength + random_6
        damage = max(0, self.attack_strength - other.defense)
options = ["goblin", "human", "mage", "oger", "elfs"]
weapons = ["knife","short_sword","bow&arrow","wooden staff","large club","wooden spear" ]
print("select your class:", options)
skills = ["knife_play", "archery", "fire ball"]
stats = ["strength", 'speed', 'stamina', 'luck', 'magic']


