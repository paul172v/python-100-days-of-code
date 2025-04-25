def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Shifts the letters in `text` by `shift`. 
    If mode is 'encode', shifts forward; if 'decode', shifts backward.
    Non-letter characters are left unchanged.
    """
    result = []
    # Normalize mode
    mode = mode.lower()
    if mode not in ('encode', 'decode'):
        raise ValueError("Mode must be 'encode' or 'decode'")

    # Reverse shift for decoding
    if mode == 'decode':
        shift = -shift

    for ch in text:
        if 'a' <= ch <= 'z':
            # shift within lowercase
            offset = ord('a')
            new_code = (ord(ch) - offset + shift) % 26 + offset
            result.append(chr(new_code))
        elif 'A' <= ch <= 'Z':
            # shift within uppercase
            offset = ord('A')
            new_code = (ord(ch) - offset + shift) % 26 + offset
            result.append(chr(new_code))
        else:
            # leave non-letters unchanged
            result.append(ch)

    return ''.join(result)


def main():
    mode = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").strip().lower()
    text = input("Enter your message:\n")
    try:
        shift = int(input("Enter shift number (e.g. 2):\n"))
    except ValueError:
        print("Shift must be an integer.")
        return

    try:
        transformed = caesar_cipher(text, shift, mode)
    except ValueError as e:
        print(e)
        return

    print(f"\nThe {mode}d text is:\n{transformed}")


if __name__ == "__main__":
    main()
