import string
import random

import numpy as np

from letter import Letter


class CipherMachine:
    def __init__(self):
        self.__seed: str = self.__seed_generator()

    # TODO:
    # - additional letters
    # - missing dot
    # - double space
    # - encode information about space
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
        sentences: list = self.__sentence_generator(encoded_text, letter)
        return " ".join(sentences)

    def decode(self, input_text: str) -> str:
        words: list = input_text.split(" ")
        decoded_text: list = self.__parse_code_words(words)
        return "".join(decoded_text)

    def __parse_code_words(self, words: list) -> list:
        code_words: list = []
        for word in words:
            if self.__has_code_letter(word):
                code_words.append(word[2])
        return code_words

    def __has_code_letter(self, word: str) -> bool:
        return True if len(word.replace(".", "")) >= 3 else False

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

    def __sentence_generator(self, encoded_text, letter) -> list:
        encoded_len: int = len(encoded_text)
        sentence_counter: int = self.__calculate_sentence_count(encoded_len, letter.number)
        output_text = []
        for sentence_array in np.array_split(encoded_text, sentence_counter):
            sentence_array[0] = np.char.capitalize(sentence_array[0])
            sentence_array[len(sentence_array) - 1] = sentence_array[len(sentence_array) - 1] + "."
            sentence: str = " ".join(sentence_array)
            output_text.append(sentence)
        return output_text

    def __calculate_sentence_count(self, encoded_len: int, letter_number: int) -> int:
        if encoded_len < letter_number:
            sentence_counter = round((encoded_len / 4))
        else:
            sentence_counter: int = encoded_len % letter_number
        return sentence_counter if sentence_counter != 0 else 1
