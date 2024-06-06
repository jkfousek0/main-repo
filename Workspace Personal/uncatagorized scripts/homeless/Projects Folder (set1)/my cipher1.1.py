text = 'Yo!cjUoaModQfubhgp'
num = -12
if num != 12:
    num = 12
hidden_message = ''
def A_space_oddessy():
    alphabet = 'abcdefghijklmnopqrstuvwxyz !'
    hidden_message = ''
    for base in text.lower():
        if base == ' ':
            hidden_message += base
        else:
            subset = alphabet.find(base)
            subset2 = (subset + num)% len(alphabet)
            hidden_message += alphabet[subset2]
A_space_oddessy()