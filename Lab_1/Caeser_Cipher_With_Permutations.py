# Function to generate a permutation key from a given word
def generate_permutation_key(word, key_to_shift):
    word = word.upper()  # Convert the word to uppercase
    unique_chars = []  # List to store unique characterspython

    # Iterate through the characters in the word, preserving order
    for char in word:
        if char not in unique_chars:
            unique_chars.append(char)

    # Create the permutation key by combining unique characters and the rest of the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    remaining_chars = [char for char in alphabet if char not in unique_chars]
    permutation_key = ''.join(unique_chars + remaining_chars)

    print(permutation_key)

    permutation_key = permutation_key[key_to_shift:] + permutation_key[:key_to_shift]

    print(permutation_key)
    return permutation_key


# Function to create a Caesar Cipher mapping using a permutation key
def create_caesar_mapping_from_key(permutation_key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mapping = {}
    for i in range(26):
        mapping[alphabet[i]] = permutation_key[i]
    print(mapping)
    return mapping


def caesar_cipher_with_two_keys(text, skip_count, permutation_key):
    #mapping = create_caesar_mapping_from_key(permutation_key)
    encrypted_text = ""
    pattern = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in range(len(text)):
        for i in range(len(pattern)):
            if text[char] == pattern[i].upper() or text[char] == pattern[i].lower():
                encrypted_text += permutation_key[i]
                break

    return encrypted_text


# Function to decrypt text using a Caesar Cipher mapping with two keys
def caesar_decipher_with_two_keys(text, skip_count, permutation_key):
    # Undo the second key (number of positions to skip)
    decrypted_text = ""

    pattern = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in range(len(text)):
        for i in range(len(pattern)):
            if text[char] == permutation_key[i].upper() or text[char] == permutation_key[i].lower():
                decrypted_text += pattern[i]
                break


    return decrypted_text


