#by using vernokm cipher convert plaintext to ciphertext and vice versa
def vernam_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        b = ord(plaintext[i]) ^ ord(key[i])
        ciphertext += chr((b >> 4) + 65) + chr((b & 0x0F) + 65)
    return ciphertext

def vernam_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        high = ord(ciphertext[i]) - 65
        low = ord(ciphertext[i+1]) - 65
        b = (high << 4) | low
        plaintext += chr(b ^ ord(key[i // 2]))
    return plaintext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key (must be same length as plaintext): ")

if len(key) != len(plaintext):
    print("Error: Key length must be equal to plaintext length!")
else:
    ciphertext = vernam_encrypt(plaintext, key)
    print("\nEncrypted Ciphertext (letters A-P):", ciphertext)

    cipher_input = input("\nEnter the ciphertext (letters A-P) to decrypt: ")
    key2 = input("Enter the same key used for encryption: ")

    if len(key2) * 2 != len(cipher_input):
        print("Error: Ciphertext length must be twice the key length!")
    else:
        decrypted_text = vernam_decrypt(cipher_input, key2)
        print("\nDecrypted Plaintext:", decrypted_text)