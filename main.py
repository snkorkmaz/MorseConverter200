import time
from logo import logo
import os

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

menu = """
MENU 

1. Text to Morse Converter
2. Morse to Text Converter 
3. Exit 
"""

guidelines = """
Please keep the following guidelines in mind:

- Morse code letters should be separated by exactly one space.
- Use a slash (/) to separate Morse code words. Each separator must be preceded and followed by one space."
"""


def text_is_valid(txt, morse_dict):
    """Returns True if all characters in the text (txt) are present in the Morse code dictionary (morse_dict),
    False otherwise."""
    for c in txt:
        if c not in morse_dict:
            return False
    return True


def code_is_valid(morse_code):
    """Returns True if all characters in the morse_code are valid characters, False otherwise."""
    for c in morse_code:
        if c not in [".", "-", "/", " "]:
            return False
    return True


while True:
    should_break = False

    # Clear Screen and Print HEADER (MENU)
    os.system('cls')
    print(logo)
    print("Welcome to the MorseConverter2000.")
    print(menu)

    # Ask for Input
    menu_choice = input("Enter the number of your choice: ")

    # User chooses TEXT TO MORSE CONVERTER
    if menu_choice == "1":

        # Clear Screen and Print HEADER
        os.system('cls')
        print(logo)
        print("You chose option 1: Text to Morse Code Converter\n")

        # Repeat to ask for TEXT INPUT
        while True:
            text = input("Please enter the text you want to convert to Morse code: ").upper()

            # Text is VALID
            if text_is_valid(text, morse_code_dict):
                morse_code = ""
                # Iterate over the input string and replace each character with its Morse code.
                for char in text:
                    if char == " ":
                        morse_code += "/ "
                    else:
                        morse_code += morse_code_dict[char] + " "  # letters are separated by spaces

                print("The Morse code representation of the input is:" + morse_code)

                # Repeat to ask if user wants to perform another conversion
                while True:
                    choice = input("Would you like to perform another conversion? y(yes)/n(no): ")
                    # User chooses to exit the program
                    if choice.lower() == "n":
                        print("Thank you for using the MorseConverter2000. Goodbye!")
                        exit()
                    # User chooses to perform another conversion
                    elif choice.lower() == "y":
                        should_break = True
                        break

                # Return to MENU
                if should_break:
                    break

            # Text is NOT VALID
            else:
                print(
                    'Text must contain only letters (A-Z, a-z), digits (0-9), and the following special characters: '
                    '., ,, ?, \', !, /, (, ), &, :, ;, =, +, -, _, ", $, @, (space)')
                time.sleep(5)

    # User chooses MORSE TO TEXT CONVERTER
    elif menu_choice == "2":

        # Clear Screen and Print HEADER
        os.system('cls')
        print(logo)
        print("You chose option2: Morse Code to Text Converter\n")
        print(guidelines)

        # Repeat to ask for CODE INPUT
        while True:
            code = input("Please enter the morse code you want to convert to text: ")
            converted_text = ""

            # Code is VALID
            if code_is_valid(code):

                # Split string at " " and store each morse letter in a list
                char_list = code.split(" ")
                for i in char_list:
                    # is space
                    if i == "/":
                        converted_text += " "
                    # is character
                    # get the text representation from the dictionary and store it in a list
                    else:
                        letter = [key for key, value in morse_code_dict.items() if value == i]
                        # The morse Letter is not in the dictionary, and thus not a valid morse code
                        if not letter:
                            print("Invalid input! Please enter a valid morse code.")
                        # Morse letter is valid and the text representation is stored in l[0]
                        else:
                            converted_text += letter[0]
                            letter = []
                print("The text representation of the input is: " + converted_text)

                # Repeat to ask if user wants to perform another conversion
                while True:
                    choice = input("Would you like to perform another conversion? y(yes)/n(no): ")
                    # User chooses to exit the program
                    if choice.lower() == "n":
                        print("Thank you for using the MorseConverter2000. Goodbye!")
                        exit()
                    # User chooses to perform another conversion
                    elif choice.lower() == "y":
                        break

                # Return to MENU
                if should_break:
                    break
            # Code is NOT VALID
            else:
                print('The code must contain only the characters: ".", "-", "/" and (space)')
                time.sleep(5)
                should_break = True
                break

