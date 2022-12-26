import caesar_cipher_ascii_art

encripted_letters_list = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


print(caesar_cipher_ascii_art.ascii_art)

function = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message\n").lower()
shift_number = int(input("Type the shift number:\n"))

# Encode function
def encode(message, shift_number):
    for i in range(len(message)):
        for j in range(len(alphabet)):
            if alphabet[j] == message[i]:
                if (j + shift_number) > 25:
                    encripted_letters_list.append(alphabet[j+shift_number-26])
                else:
                    encripted_letters_list.append(alphabet[j+shift_number])
    
    print(encripted_letters_list)

if function.lower() == "encode":
    encode(message = message, shift_number = shift_number)
# else:
#     decode()
