# Write a code in Python to create a Morse code translator.
# You can take a string with alphanumeric characters in lower or upper case.
# The string can also have any special characters as a part of the Morse code.
# Special characters can include commas, colons, apostrophes, exclamation marks, periods, and question marks.
# The code should return the Morse code that is equivalent to the string.

import re

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

MORSE_DECODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

NOT_FOUND_SYMBOL = "#"

INTER_WORDS_MORSE_SYMBOL = "       "
INTER_LETTERS_MORSE_SYMBOL = "   "


def encode_english_word(input_word: str, not_found_symbol=NOT_FOUND_SYMBOL) -> str:
    letters = input_word.upper()
    encoded_letters = [MORSE_CODE_DICT.get(
        letter, not_found_symbol) for letter in letters]
    return INTER_LETTERS_MORSE_SYMBOL.join(encoded_letters)


def encode_english_expression(input_expression: str) -> str:
    words = re.sub(' +', ' ', input_expression).strip().split(" ")
    encoded_words = [encode_english_word(word) for word in words]
    return INTER_WORDS_MORSE_SYMBOL.join(encoded_words)


def decode_morse_word_to_english(input_word: str, not_found_symbol=NOT_FOUND_SYMBOL) -> str:
    symbols = input_word.strip().split(INTER_LETTERS_MORSE_SYMBOL)
    decoded_letters = [MORSE_DECODE_DICT.get(
        symbol, not_found_symbol) for symbol in symbols]
    return "".join(decoded_letters)


def decode_morse_expression_to_english(input_expr: str):
    words = input_expr.split(INTER_WORDS_MORSE_SYMBOL)
    decoded_words = [decode_morse_word_to_english(word) for word in words]
    return " ".join(decoded_words)


if __name__ == '__main__':
    while True:
        conversion = input(
            "Decode from Morse or Encode to Morse? Type D or E. Type (exit) for exit.\n")
        if conversion == "E":
            input_expression = input("Enter expression in english\n")
            encoded = encode_english_expression(input_expression)
            print(f'Morse code:\n{encoded}')
            continue
        if conversion == "D":
            input_expression = input("Enter expression on MORSE code\n")
            decoded = decode_morse_expression_to_english(input_expression)
            print(f'English expression\n{decoded}')
            continue
        if conversion == "exit":
            break
