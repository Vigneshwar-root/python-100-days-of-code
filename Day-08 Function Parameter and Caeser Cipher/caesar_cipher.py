
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print(len(alphabet))




# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         if new_position >= 26:
#             new_position = new_position - 26
#             print(new_position)
#         cipher_text += alphabet[new_position] 
    
#     print(cipher_text)

def caesar(direction, text, shift_amount):
    result = ""
    val = 1
    if direction == 'decode':
        shift_amount *= -1
        val = -1
    for letter in text:
        position = alphabet.index(letter)
      
        new_position = position + shift_amount
        if new_position >= 26:
            new_position = new_position - 26 * val
        # elif direction == 'decode':
        #      new_position = position - shift_amount
        #      if new_position < 0:
        #         new_position = new_position + 26
        result += alphabet[new_position]      
    
    print(result)

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(direction, text, shift)

    user_input = input("Type 'Yes' if tyou want to go again. Otherwise type no. \n")
    if user_input == 'no':
        should_continue = False
        print("Good Bye")
    




