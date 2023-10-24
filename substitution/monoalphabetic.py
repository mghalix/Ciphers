def cipher(plaintext: str, ckey: str) -> str:
    ciphertext = ""
    for c in plaintext:
        if c < "a" or c > "z":
            ciphertext += c
            continue

        index = ord(c) - ord("a")
        ciphertext += ckey[index]

    return ciphertext


def decipher(ciphertext: str, ckey: str) -> str:
    plaintext = ""

    for c in ciphertext:
        if c < "a" or c > "z":
            plaintext += c
            continue

        plaintext += chr(ckey.index(c) + ord("a"))

    return plaintext


def main():
    pass


if __name__ == "__main__":
    main()
