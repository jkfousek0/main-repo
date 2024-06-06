text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        #pass:
        if char == ' ':
            encrypted_text += char

         #main code:
        else:
            index = alphabet.find(char)
            print(index)
            new_index = (index + shift) % len(alphabet)
            print(new_index)
            encrypted_text += alphabet[new_index]
            print(encrypted_text)
            #output/call:
    print('plain text:', text)
    print('encrypted text:', encrypted_text)

caesar(text, shift)