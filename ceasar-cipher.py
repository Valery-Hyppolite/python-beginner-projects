
#A simple program that encode and decode your message.
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

willing_continue = True
while willing_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text_input,shift_amount,user_direction):
        plain_cypher_text = ''

        for letter in text_input:
            if letter in alphabet:
                position = alphabet.index(letter)
                if direction == 'encode':
                    letter_position = alphabet[position + shift_amount]
                    plain_cypher_text += letter_position
                if direction == 'decode':
                    letter_position = alphabet[position - shift_amount]
                    plain_cypher_text += letter_position
            else:
                plain_cypher_text += letter

        print(f"the {direction} text is {plain_cypher_text}")
    
    caesar(text_input = text, shift_amount = shift, user_direction = direction)

    user_choice = input("Yould you like to do this again? type yes/no\n")
    if user_choice == 'yes':
        willing_continue = True
    else:
        willing_continue = False
        print("goodbye, I'll see you again :)")
