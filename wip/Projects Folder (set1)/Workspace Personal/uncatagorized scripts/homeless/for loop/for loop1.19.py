text = 'AmaM AmjY'
shift = 2
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
undefined = input('can you decifer my code?:',)
for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]
print('encrypted text:', encrypted_text)