import string
import random


def encode(input_text: str) -> str:
    encoded_text: list = []
    for x in range(len(input_text)):
        """3rd letter in each word that has over 3 letters"""
        current_word_len: int = random.randint(1, 10)
        current_word: list = []
        while True:
            for i in range(current_word_len):
                current_word.append(random.choice(string.ascii_letters))
            if len(current_word) > 2:
                current_word[2] = input_text[x]
                encoded_text.append("".join(current_word))
                break
            encoded_text.append("".join(current_word))
    return " ".join(encoded_text)


def main() -> None:
    input_text: str = input("text to encode:\n ")
    output_text: str = encode(input_text)
    print(f"encoded text:\n {output_text}")


if __name__ == "__main__":
    main()
