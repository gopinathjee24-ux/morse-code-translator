MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

def text_to_morse(text):
    text = text.upper()
    morse = " ".join(MORSE_CODE_DICT.get(char, "") for char in text)
    return morse

def morse_to_text(morse):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = morse.split(" ")
    decoded = "".join(reverse_dict.get(code, "") for code in words)
    return decoded

while True:
    print("\n--- MORSE CODE TRANSLATOR ---")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        user_text = input("Enter text: ")
        print("Morse Code:", text_to_morse(user_text))

    elif choice == "2":
        user_morse = input("Enter Morse Code (letters separated by space): ")
        print("Decoded Text:", morse_to_text(user_morse))

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Input! Try again.")