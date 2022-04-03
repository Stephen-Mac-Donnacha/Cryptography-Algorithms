from vigenere_cipher import viginere_cipher
from lsfr import lsfr


def main():
    print("Enter which cryptography algorithm you would like to see")
    print("1: Vignere Cipher\n"
          "2:LSFR (Linear Feedback Shift Register\n"
          "3:Diffie Hellman Key exchange(coming soon!)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        viginere_cipher()
    else:
        lsfr()


if __name__ == "__main__":
    main()
