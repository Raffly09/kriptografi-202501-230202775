import string

def vigenere_encrypt(plaintext, key):
    """Enkripsi menggunakan Vigenere Cipher dengan key tertentu, termasuk angka."""
    alphabet = string.ascii_uppercase + string.digits  # A-Z dan 0-9
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = []
    key_index = 0
    for char in plaintext:
        if char in alphabet:
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isalpha() else ord('0')
            encrypted_char = chr((ord(char) - base + shift) % 36 + base)
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    """Dekripsi menggunakan Vigenere Cipher dengan key tertentu, termasuk angka."""
    alphabet = string.ascii_uppercase + string.digits  # A-Z dan 0-9
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = []
    key_index = 0
    for char in ciphertext:
        if char in alphabet:
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isalpha() else ord('0')
            decrypted_char = chr((ord(char) - base - shift) % 36 + base)
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)
    return ''.join(plaintext)

def main():
    print("Sistem Kriptografi Vigenere Cipher (dengan enkripsi angka)")
    plaintext = input("Masukkan plaintext: ").strip()
    key = input("Masukkan key (string huruf): ").strip()
    if not key.isalpha():
        print("Key harus berupa huruf saja.")
        return
    ciphertext = vigenere_encrypt(plaintext, key)
    print("\nOutput:")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Key: {key}")

if __name__ == "__main__":
    main()