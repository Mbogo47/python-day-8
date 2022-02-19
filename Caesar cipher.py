alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
    elif cipher_direction == "encode":
        shift_amount *= 1

        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char

    print(f"The {cipher_direction}d text is {end_text} ")


again = True
while again:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
    if direction == 'encode':
        text = input("Type your message to encode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    elif direction == 'decode':
        text = input("Type your message to decode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print("invalid direction")
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if result == "no":
        again = False
        print("Goodbye!")
