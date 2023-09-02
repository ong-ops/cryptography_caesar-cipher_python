#!/usr/bin/env python3

def encrypt_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            alphabet = ord(char) - ascii_offset
            alphabet_shifted = (alphabet + shift) % 26
            char = chr(alphabet_shifted + ascii_offset)
        result += char
    return result

print("Enter the plain text.")
plain_text = input('> ')

print("Enter the key (0 to 25)")
key = int(input('> '))

encrypted = encrypt_caesar_cipher(plain_text, key)
print(f"Result: {encrypted}")
