'''Python program to implement symmetric encryption using python library'''
from cryptography.fernet import Fernet

def main():
    # Generate a key for encryption
    key = Fernet.generate_key()

    # Create a Fernet object with the generated key
    f = Fernet(key)

    # Take user input for the message to encrypt
    message = input("Enter the message to encrypt: ")

    # Convert the message to bytes and encrypt it
    token = f.encrypt(message.encode('utf-8'))

    # Print the encrypted token
    print("Encrypted Token:", token)

    # Decrypt the token and print the original message
    decrypted_message = f.decrypt(token).decode('utf-8')
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
