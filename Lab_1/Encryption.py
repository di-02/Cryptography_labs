def encrypt_text(text_to_encrypt,key):

    encrypted_text = ""

    for char in text_to_encrypt:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Apply the Caesar Cipher shift
            shifted_char = chr((ord(char) - base + key) % 26 + base)
            encrypted_text += shifted_char
        else:
            # If the character is not alphabetic, leave it unchanged
            encrypted_text += char

    return encrypted_text
