# For Encryption using: (plaintext + key) mod 26
# For Decryption using : (ciphertext - key) mod 26


def encrypt(plaintext: str, key: int) -> str:
    ciphertext = ""
    for c in plaintext:
        if c < "a" or c > "z":
            ciphertext += c
            continue

        # range 97 -> 122 (a -> z)
        ascii = ord(c) + key
        if ascii > ord("z"):
            ascii -= 26

        ciphertext += chr(ascii)

    return ciphertext


def decrypt(ciphertext: str, key: int) -> str:
    plaintext = ""
    for c in ciphertext:
        if c < "a" or c > "z":
            plaintext += c
            continue

        ascii = ord(c) - key
        if ascii < ord("a"):
            ascii += 26

        plaintext += chr(ascii)

    return plaintext


def main():
    print(encrypt("a[", 1))


if __name__ == "__main__":
    main()
