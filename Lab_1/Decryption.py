from Caeser_Cipher_With_Permutations import create_caesar_mapping_from_key

def caesar_decipher(text_to_decrypt, key):
    decrypted_text = ""

    for char in text_to_decrypt:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Apply the reverse Caesar Cipher shift to decrypt
            shifted_char = chr((ord(char) - base - key) % 26 + base)
            decrypted_text += shifted_char
        else:
            # If the character is not alphabetic, leave it unchanged
            decrypted_text += char

    return decrypted_text