from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# Fungsi Pembuatan & Penyimpanan Kunci 
def generate_and_save_keys(key_size=2048):
    print(f"[*] Sedang men-generate pasangan kunci RSA {key_size}-bit...")
    key = RSA.generate(key_size)
    
    # Ekspor Private Key 
    private_key = key.export_key()
    with open("private.pem", "wb") as f:
        f.write(private_key)
    
    # Ekspor Public Key 
    public_key = key.publickey().export_key()
    with open("public.pem", "wb") as f:
        f.write(public_key)
        
    print("[*] Kunci berhasil disimpan ke 'private.pem' dan 'public.pem'")
    return key

# Fungsi Enkripsi Menggunakan Public Key
def encrypt_message(message, public_key_path="public.pem"):
    # Load Public Key dari file
    with open(public_key_path, "rb") as f:
        pub_key = RSA.import_key(f.read())
    
    # Inisialisasi Cipher 
    cipher = PKCS1_OAEP.new(pub_key)
    
    # Enkripsi
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    
    # Encode ke Base64 agar hasil terlihat rapi saat di-print
    return base64.b64encode(ciphertext).decode('utf-8')

# Fungsi Dekripsi Menggunakan Private Key
def decrypt_message(ciphertext_b64, private_key_path="private.pem"):
    # Load Private Key dari file
    with open(private_key_path, "rb") as f:
        priv_key = RSA.import_key(f.read())
    
    # Inisialisasi Cipher
    cipher = PKCS1_OAEP.new(priv_key)
    
    try:
        # Decode dari Base64 kembali ke bytes, lalu dekripsi
        ciphertext = base64.b64decode(ciphertext_b64)
        decrypted = cipher.decrypt(ciphertext)
        return decrypted.decode('utf-8')
    except ValueError:
        return "Error: Dekripsi gagal! Kunci salah atau data rusak."

# Implementasi Utama
if __name__ == "__main__":
    # Langkah 1: Generate Kunci 
    generate_and_save_keys()
    print("-" * 50)

    # Langkah 2: Simulasi Pengirim 
    pesan_rahasia = "Ini adalah pesan sangat rahasia dengan RSA Modern"
    print(f"Plaintext Asli : {pesan_rahasia}")
    
    encrypted_msg = encrypt_message(pesan_rahasia)
    print(f"Ciphertext (B64): {encrypted_msg}")
    print("-" * 50)

    # Langkah 3: Simulasi Penerima
    hasil_dekripsi = decrypt_message(encrypted_msg)
    print(f"Hasil Dekripsi : {hasil_dekripsi}")