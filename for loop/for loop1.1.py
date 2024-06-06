
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet.find(text[0])
#
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
#
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)
#
#.find() returns the index of the matching character inside the string. If the character is not found, it returns -1. As you can see, the first character in text, uppercase 'H', is not found, since alphabet contains only lowercase letters.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)
print(text.lower())
#
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
#
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index]
#
print(shifted)
#
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index + shift]
print(shifted)
#
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in text:

 text = 'Hello World'
 shift = 3
 alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
 for char in text:
     index = alphabet.find(char)
     print(char, index)
    
#
 text = 'Hello World'
 shift = 3
 alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
 for char in text.lower():
     index = alphabet.find(char)
    
     new_index = index + shift
     new_char = alphabet[new_index]
     print('char:', char, 'new char:', new_char)
     
#
 text = 'Hello World'
 shift = 3
 alphabet = 'abcdefghijklmnopqrstuvwxyz'
 encrypted_text = ''
 for char in text.lower():
     index = alphabet.find(char)
     new_index = index + shift
     new_char = alphabet[new_index]
     print('char:', char, 'new char:', new_char)
    
#


