import string

def caesar_encrypt(plaintext, shift):
    """Enkripsi menggunakan Caesar Cipher dengan shift tertentu, termasuk angka."""
    alphabet = string.ascii_uppercase + string.digits  # A-Z dan 0-9
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.upper().translate(table)

def caesar_decrypt(ciphertext, shift):
    """Dekripsi menggunakan Caesar Cipher dengan shift tertentu, termasuk angka."""
    return caesar_encrypt(ciphertext, -shift)

def main():
    print("Sistem Kriptografi Caesar Cipher (dengan enkripsi angka)")
    plaintext = input("Masukkan plaintext: ").strip()
    try:
        shift = int(input("Masukkan shift (angka): ").strip())
        key = str(shift)  # Key adalah shift-nya
        ciphertext = caesar_encrypt(plaintext, shift)
        decrypted_plaintext = caesar_decrypt(ciphertext, shift)
        print("\nOutput:")
        print(f"Plaintext: {plaintext}")
        print(f"Ciphertext: {ciphertext}")
        print(f"Key: {key}")
        print(f"Hasil Dekripsi: {decrypted_plaintext}")
    except ValueError:
        print("Shift harus berupa angka.")

if __name__ == "__main__":
    main()