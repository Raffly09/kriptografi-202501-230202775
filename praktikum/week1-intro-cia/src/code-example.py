# simple_shift_cipher.py
# Shift Cipher sederhana
# Input: plaintext
# Output: hasil enkripsi otomatis dengan shift tetap (3)

def shift_cipher(text: str, shift: int = 3) -> str:
    """Melakukan enkripsi sederhana (Shift Cipher) dengan pergeseran tertentu."""
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif '0' <= ch <= '9':
            result.append(chr((ord(ch) - ord('0') + shift) % 10 + ord('0')))
        else:
            result.append(ch)
    return ''.join(result)

def main():
    print("=== SHIFT CIPHER SEDERHANA ===")
    plaintext = input("Masukkan plaintext: ")
    ciphertext = shift_cipher(plaintext, 3)
    print("\nHasil Enkripsi :", ciphertext)
    print("Hasil Dekripsi :", plaintext)

if __name__ == "__main__":
    main()