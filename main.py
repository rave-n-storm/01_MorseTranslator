from replit import clear

# Replit's clear() function currently doesn't work in PyCharm.
# Those commands are still in the code, it doesn't affect the run in PyCharm, but it works on Replit.

# Morse code dictionary
morse_code = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
              "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
              "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
              "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
              "6": "-.....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": "/",
              "&": ".-...", "'": ".----.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-", ":": "---...",
              ",": "--..--", "=": "-...-", "!": "-.-.--", ".": ".-.-.-", "-": "-....-", "%": "------..-.-----",
              "+": ".-.-.", '"': ".-..-.", "?": "..--..", "/": "-..-."}


# function to choose functionality of the translator
def choose_functionality():
    """Asks user which functionality they want to use."""
    choice = input("Functionalities: \n"
                   "'text' - translate text to Morse code,\n"
                   "'morse' - translate Morse code to text.\n\n"
                   "Type your choice: ").lower()

    # choose functionality based on user's answer
    if choice == "text":
        clear()
        text_to_morse()
    elif choice == "morse":
        clear()
        morse_to_text()
    # ask user again if answer is invalid
    else:
        print("Invalid choice, please try again.\n")
        print("\033[2J\033[H", end="", flush=True)
        choose_functionality()


# text-to-Morse translator function
def text_to_morse():
    """Translates text to Morse code."""
    # input text to translate
    text_to_translate = input("Message to translate to Morse: \n").lower()

    try:
        # switch letters one-by-one into a list
        translated_morse_as_list = [morse_code[letter] for letter in text_to_translate]

    except KeyError:
        # catch KeyError on invalid character
        print("Invalid character in text, please try again.")
        text_to_morse()

    else:
        # join list into string
        translated_as_morse = " ".join(translated_morse_as_list)

        # print string then ask to continue
        print(f"Your message in Morse: \n{translated_as_morse}\n")
        ask_to_continue()


# Morse-to-text translator function
def morse_to_text():
    """Translates Morse code to text."""
    # input Morse code to translate
    morse_to_translate = input("Morse code to translate (use '-' and '.'): \n")

    # make a list of every Morse character of the input
    morse_list_to_translate = list(morse_to_translate.split(" "))

    try:
        # switch characters one-by-one into a list
        translated_text_as_list = []
        for char in morse_list_to_translate:
            for letter, morse in morse_code.items():
                if morse == char:
                    translated_text_as_list.append(letter)

    # catch KeyError on invalid character
    except KeyError:
        print("Invalid character in Morse code, please try again.")
        morse_to_text()

    else:
        # join list into string
        translated_as_text = "".join(translated_text_as_list)

        # print string then ask to continue
        print(f"Your code as text: \n{translated_as_text}\n")
        ask_to_continue()


def ask_to_continue():
    """Asks if user wants to translate something else."""
    # ask user if they want to continue
    to_continue = input("Would you like to translate something else? \n"
                        "Type 'Y' to choose functionality, \n"
                        "type 'N' to quit.\n").lower()

    # continue or quit based on user's answer
    if to_continue == "y":
        clear()
        choose_functionality()
    elif to_continue == "n":
        clear()
        exit()

    # ask user again if answer is invalid
    else:
        print("Invalid choice, please try again.")
        ask_to_continue()


### APP START  ###

print("MORSE TRANSLATOR \n"
      "by Németh Gáspár\n")
choose_functionality()
