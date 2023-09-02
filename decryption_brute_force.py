#!/usr/bin/env python3

print("Enter the encrypted text.")
encrypted_text = input("> ")

for shift in range(26):
    result = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            alphabet = ord(char) - ascii_offset
            alphabet_shift_reversed = (alphabet - shift) % 26
            char = chr(alphabet_shift_reversed + ascii_offset)
        result += char
    print(f"{shift} | {result}")
