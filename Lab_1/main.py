from Caeser_Cipher_With_Permutations import caesar_cipher_with_two_keys, caesar_decipher_with_two_keys,generate_permutation_key
from Decryption import caesar_decipher
from Encryption import encrypt_text


def main():
    while True:
        print("Menu:")
        print("1. Simple encryption")
        print("2. Encryption with permutation")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("For simple encryption the word to encrypt and the key to encrypt with required!")
            word_to_encrypt  = str(input("Enter the word to encrypt:"))
            key = int(input("Enter the key:"))
            encrypted = encrypt_text(word_to_encrypt, key)
            print("Encrypted text:", encrypted)
            word_to_decrypt = str(input("Enter the word to decrypt:"))
            key = int(input("Enter the key:"))
            decrypted = caesar_decipher(word_to_decrypt, key)
            print("Decrypted text:", decrypted)
        elif choice == "2":
            print("For encryption with permutation word, key and permutation pattern required!")
            word_to_encrypt = str(input("Enter the word to encrypt:"))
            key = int(input("Enter the key to encrypt:"))
            permutation_pattern = str(input("Enter the permutation keyword:"))
            encrypted = caesar_cipher_with_two_keys(word_to_encrypt, key, generate_permutation_key(permutation_pattern))
            print("Encrypted text:", encrypted)
            word_to_decrypt = str(input("Enter the word to decrypt:"))
            key = int(input("Enter the key:"))
            permutation_pattern = str(input("Enter the permutation keyword:"))
            decrypted = caesar_decipher_with_two_keys(word_to_decrypt, key, generate_permutation_key(permutation_pattern))
            print("Decrypted text:", decrypted)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

