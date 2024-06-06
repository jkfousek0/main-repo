# ---------------example promt (caesar cipher)------------------------------------
text = 'Hello Zaira'
shift = 3

#call function with no arguments
def caesar():
    # assign a string'with a set of symbols/num/letters'
    # And set the varible encrypted_text to a blank string value
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''


    #for loops define new var by a currentvar+method of choice(ex: .lower)
    for char in text.lower():

        #if loop passed due to the loop returning false 
        if char == ' ':
            encrypted_text += char


        # becuase the if loop failed else: block is called on
        # main code for cipher
        else:
            # char is = text.lower as expressed in the for loop above
            # index (7,4,11,11,14,25,0,8,17,0)
            index = alphabet.find(char)

            # index +3 to (7,4,11,11,14,25,0,8,17,0)%26
            new_index = (index + shift) % len(alphabet)
            # new index = (10,7,14,14,17,2,3,11,20,3)

            #encrpted txt var = '' + new_index in alphabet 
            encrypted_text += alphabet[new_index]
            # decrypted text = khoor cdlud
            # encrypted text = hello 

    print('plain text:', text)
    print('encrypted text:', encrypted_text)
caesar()
