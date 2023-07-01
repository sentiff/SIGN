from cipher_machine import CipherMachine


def main() -> None:
    cypher_machine = CipherMachine()
    input_text: str = input("text to encode:\n ")
    output_text: tuple[str, str] = cypher_machine.encode(input_text)
    print(f"encoded text:\n {output_text}")
    decoded_text = cypher_machine.decode(output_text)
    print(f"decoded text:\n {decoded_text}")


if __name__ == "__main__":
    main()
