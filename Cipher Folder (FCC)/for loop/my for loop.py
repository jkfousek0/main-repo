game = 'cd'
s = 5
alphabet = 'abcdefghijklmnpqrstuvwxyz'
hidden_test = ''
for hidden in game.lower():
    prefab = alphabet.find(hidden)
    print (prefab)
    print (hidden)
    print(game)