org = 'fsfdfsod'
num1 = 3
alphabet = 'abcdefghijklmnopqstuvwxyz'
hidden_text = ''

print('find the:',hidden_text)
for main in org:
    inx = print(alphabet.find(org))
    inx2 = inx + num1
    hidden_text += alphabet[inx2]
    print(main,hidden_text )

