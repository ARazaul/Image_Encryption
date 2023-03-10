import os
import random


class ImageEncryptor:
    def __init__(self):
        self.system_path = os.getcwd().replace('\\', '\\\\')

    def menu(self):
        print("\nEncrypt Image\n1. Encrypt Image\n2. Decrypt Image\n3. Exit\n")

    def encrypt(self, pass_phrase, image_name):
        original_file = os.path.join(self.system_path, "Encrypt", image_name)
        duplicate_file = os.path.join(self.system_path, "Decrypt", image_name)
        with open(original_file, "rb") as original, open(duplicate_file, "wb") as duplicate:
            original_data = original.read()
            key = random.randint(2480786, 9153151)
            encrypted_data = original_data[:key][::-1] + original_data[key:][::-1]
            duplicate.write(encrypted_data)

    def decrypt(self, pass_phrase, image_name):
        original_file = os.path.join(self.system_path, "Decrypt", image_name)
        duplicate_file = os.path.join(self.system_path, "Encrypt", image_name)
        with open(original_file, "rb") as original, open(duplicate_file, "wb") as duplicate:
            original_data = original.read()
            key = random.randint(2480786, 9153151)
            decrypted_data = original_data[:key][::-1] + original_data[key:][::-1]
            duplicate.write(decrypted_data)

    def run(self):
        while True:
            self.menu()
            user_input = input("Enter: ").lower()
            if user_input == "1" or user_input == "encrypt":
                try:
                    image_name = input("Image Name: ")
                    self.encrypt(input("Pass Phrase: "), image_name)
                    os.remove(os.path.join(self.system_path, "Encrypt", image_name))
                    print("\nImage Encrypted Successfully\n")
                except FileNotFoundError:
                    print("File Not Found")
            elif user_input == "2" or user_input == "decrypt":
                try:
                    image_name = input("Image Name: ")
                    self.decrypt(input("Pass Phrase: "), image_name)
                    os.remove(os.path.join(self.system_path, "Decrypt", image_name))
                    print("\nImage Decrypted Successfully\n")
                except FileNotFoundError:
                    print("File Not Found")
            elif user_input == "3" or user_input == "exit":
                exit()
            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    image_encryptor = ImageEncryptor()
    image_encryptor.run()