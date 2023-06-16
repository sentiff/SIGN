import string
import random

from letter import Letter


class CipherMachine:
    def __init__(self):
        self.__seed: str = self.__seed_generator()

    def encode(self, input_text: str) -> str:
        letter: Letter = self.__create_letter()
        encoded_text: list = []
        for x in range(len(input_text)):
            """3rd letter in each word that has over 3 letters"""
            current_word_len: int = random.randint(1, 10)
            current_word: list = []
            while True:
                # TODO: change to random.choices()
                for i in range(current_word_len):
                    current_word.append(random.choice(string.ascii_letters).lower())
                if len(current_word) > 2:
                    current_word[2] = input_text[x]
                    encoded_text.append("".join(current_word))
                    break
                encoded_text.append("".join(current_word))
        print(encoded_text)
        return " ".join(encoded_text)

    def __seed_generator(self) -> str:
        return "".join(random.choices(string.ascii_letters, k=10))

    def __create_letter(self) -> Letter:
        position: int = random.randrange(len(self.__seed))
        letter_from_seed: str = self.__seed[position].lower()
        number_of_letter: int = ord(letter_from_seed) - 96

        return Letter(
            letter_from_seed,
            number_of_letter
        )

    # TODO: fix
    def __sentence_generator(self, encoded_text, letter):
        encoded_len = len(encoded_text)
        if encoded_len < letter.number:
            sentence_counter = round((encoded_len / 4))
        else:
            sentence_counter: int = len(encoded_text) % letter.number
        encoded_text.insert(sentence_counter, ".")
        for x in range(len(encoded_text)):
            if x == 0 or encoded_text[x - 1] == ".":
                print("encoded_text[x]")
                print(encoded_text[x])
                new_one = (encoded_text[x]).replace(encoded_text[0], encoded_text[0].upper(), 1)
                print("new_one")
                print(new_one)
                encoded_text[x] = new_one
        encoded_text.append(".")
        return encoded_text
