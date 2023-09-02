#!/usr/bin/env python3

def decrypt_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            alphabet = ord(char) - ascii_offset
            alphabet_shift_reversed = (alphabet - shift) % 26
            char = chr(alphabet_shift_reversed + ascii_offset)
        result += char
    return result

print("Enter the encrypted text.")
encrypted_text = input("> ")

print("Enter the key (0 to 25)")
key = int(input("> "))

decrypted = decrypt_caesar_cipher(encrypted_text, key)
print(f"Result: {decrypted}")
