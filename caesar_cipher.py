from caesar_cipher_resources import alphabet
from caesar_cipher_resources import characters
from caesar_cipher_resources import logo

encripted_letters_list = []
run_again = True

print(logo)

while run_again:

    function = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    # Encode letters
    def letter_encode(i):
        for j in range(len(alphabet)):
            if alphabet[j] == message[i]:
                if (j + shift_number) > 25:
                    encripted_letters_list.append(alphabet[j+shift_number-26])
                else:
                    encripted_letters_list.append(alphabet[j+shift_number])

    # Encode characters
    def character_encode(i):
        for k in range(len(characters)):
            if characters[k] == message[i]:
                if (k + shift_number) > 31:
                    encripted_letters_list.append(characters[k+shift_number-32])
                else:
                    encripted_letters_list.append(characters[k+shift_number])

    # Decode letters
    def letter_decode(i):
        for j in range(len(alphabet)):
            if alphabet[j] == message[i]:
                if (j - shift_number) < 0:
                    encripted_letters_list.append(alphabet[j-shift_number+26])
                else:
                    encripted_letters_list.append(alphabet[j-shift_number])

    # Decode characters
    def character_decode(i):
        for k in range(len(characters)):
            if characters[k] == message[i]:
                if (k - shift_number) < 0:
                    encripted_letters_list.append(characters[k-shift_number+32])
                else:
                    encripted_letters_list.append(characters[k-shift_number])

    # Encode function
    def encode(message, shift_number):
        for i in range(len(message)):
            if message[i] in alphabet:
                letter_encode(i)
            elif message[i] == " ":
                encripted_letters_list.append(" ")
            else:
                character_encode(i)
        
        encripted_letters_list_to_string = "".join(encripted_letters_list)
        print(f"Here's the encoded result: {encripted_letters_list_to_string}")

    # Decode function
    def decode(message, shift_number):
        for i in range(len(message)):
            if message[i] in alphabet:
                letter_decode(i)
            elif message[i] == " ":
                encripted_letters_list.append(" ")
            else:
                character_decode(i)
        
        encripted_letters_list_to_string = "".join(encripted_letters_list)
        print(f"Here's the decoded result: {encripted_letters_list_to_string}")

    if function.lower() == "encode":
        encode(message = message, shift_number = shift_number)
    elif function.lower() == "decode":
        decode(message = message, shift_number = shift_number)
    else:
        print("Please type correct answer")

    proceed = input("Type 'yes' if you want to go again., Otherwise typr 'no':\n").lower()

    # Check user want to continue or exit
    if proceed == "yes":
        run_again = True
        encripted_letters_list = []
    else:
        run_again = False
