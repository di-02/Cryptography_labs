# Function to generate a permutation key from a given word
def generate_permutation_key(word):
    word = word.upper()  # Convert the word to uppercase
    unique_chars = []  # List to store unique characters

    # Iterate through the characters in the word, preserving order
    for char in word:
        if char not in unique_chars:
            unique_chars.append(char)

    # Create the permutation key by combining unique characters and the rest of the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    remaining_chars = [char for char in alphabet if char not in unique_chars]
    permutation_key = ''.join(unique_chars + remaining_chars)

    return permutation_key


# Function to create a Caesar Cipher mapping using a permutation key
def create_caesar_mapping_from_key(permutation_key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mapping = {}
    for i in range(26):
        mapping[alphabet[i]] = permutation_key[i]
    return mapping


def caesar_cipher_with_two_keys(text, skip_count, permutation_key):
    mapping = create_caesar_mapping_from_key(permutation_key)
    encrypted_text = ""

    for char in text:
        char = char.upper()  # Convert the character to uppercase
        if char.isalpha():
            if char.isupper():
                base = 'A'
            else:
                base = 'a'
            shifted_char = mapping[char]
            # Apply the second key (number of positions to skip)
            shifted_char = chr(((ord(shifted_char) - ord(base) + skip_count) % 26) + ord(base))
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text


# Function to decrypt text using a Caesar Cipher mapping with two keys
def caesar_decipher_with_two_keys(text, skip_count, permutation_key):
    # Undo the second key (number of positions to skip)
    decrypted_text = ""

    for char in text:
        char = char.upper()  # Convert the character to uppercase
        if char.isalpha():
            if char.isupper():
                base = 'A'
            else:
                base = 'a'
            shifted_char = chr(((ord(char) - ord(base) - skip_count) % 26) + ord(base))
            # Undo the first key (permutation)
            for original_char, permuted_char in create_caesar_mapping_from_key(permutation_key).items():
                if permuted_char == shifted_char:
                    decrypted_text += original_char
                    break
        else:
            decrypted_text += char

    return decrypted_text


