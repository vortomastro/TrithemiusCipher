import sys
import re

def decrypt_trithemius(ciphertext, keyword):
    """Decrypts text using the Trithemius cipher with a given keyword."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper()
    plaintext = ""

    for i, char in enumerate(ciphertext.upper()):
        if char in alphabet:
            key_index = alphabet.index(keyword[i % len(keyword)])
            shift = alphabet.index(char) - key_index
            plaintext += alphabet[shift % 26]
        else:
            plaintext += char
    return plaintext

def analyze_text(filename, keyword):
    """Reads a text file, cleans each line, decrypts, and shows character count."""
    with open(filename, "r") as file:
        for line in file:
            # Remove punctuation, accents, and special characters
            cleaned_line = re.sub(r'[^\w\s]', '', line.strip())
            cleaned_line = re.sub(r'[áéíóúÁÉÍÓÚ]', '', cleaned_line)  # Remove accents

            decrypted_line = decrypt_trithemius(cleaned_line, keyword)

            words = re.findall(r"\b[A-Za-z]+\b", decrypted_line)
            highlighted_line = decrypted_line
            for word in words:
                highlighted_line = highlighted_line.replace(word, f"\033[91m{word}\033[0m")

            print(highlighted_line, f"  (Caracteres: {len(cleaned_line)})")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py filename keyword")
        sys.exit(1) 

    filename = sys.argv[1]
    keyword = sys.argv[2]
    analyze_text(filename, keyword)
