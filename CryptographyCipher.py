FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesershift(message, shift):
    result = ""

    for i in message.upper(): 

        if i.isalpha():
            convert =  ord(i)
            # Convert to ASCII Code
            converted = convert + shift
            # Currently a number

            if converted > LAST_CHAR_CODE: 
                converted -= CHAR_RANGE
            
            if converted < FIRST_CHAR_CODE:
                converted += CHAR_RANGE

            shifted = chr (converted)
            # Turned the ceasershifted into a string 
            result += shifted
            # Appends to the result with the shifted text
        else: 
            result += i

    print(result)

# Program to run CaeserCipher
program_run = True
Message = ""

while program_run:

    User_type = int(input("\nWelcome to Ceasercipher: Would you like to Encrypt (1), Decrypt? (2) or Quit (3) "))

    if User_type == 1:

        User_message = input("\nMessage To Encrypt: ")

        User_shift = int(input("\nKey Shift: "))
        print("\nEncrypted text: ")
        caesershift(User_message, User_shift)

    elif  User_type == 2: 

        User_message = input("\nMessage To Decrypt: ")

        User_shift = int(input("\nKey Shift: "))
        print("\nDecrypted text: ")
        caesershift(User_message, -User_shift)

    else:
        print("\nThank you, Come Again")
        program_run = False
