from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# AES-128 membutuhkan kunci sepanjang 16 bytes (128 bit)
key = get_random_bytes(16) 

print(f"AES Key (128-bit): {key.hex()}")
print("-" * 30)

# Enkripsi
data_to_encrypt = b"Ini adalah pesan rahasia dengan AES-128"

# Membuat object cipher AES dengan mode GCM 
cipher_encrypt = AES.new(key, AES.MODE_GCM)

# Melakukan enkripsi dan membuat tag autentikasi 
ciphertext, tag = cipher_encrypt.encrypt_and_digest(data_to_encrypt)

# Nonce (Number used once) diperlukan untuk dekripsi
nonce = cipher_encrypt.nonce

print(f"Ciphertext (Hex): {ciphertext.hex()}")
print(f"Nonce (Hex): {nonce.hex()}")
print(f"Tag (Hex): {tag.hex()}")
print("-" * 30)

# Dekripsi
try:
    # Membuat object cipher baru untuk dekripsi menggunakan key dan nonce yang sama
    cipher_decrypt = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    # Mendekripsi dan memverifikasi tag (memastikan data tidak diubah peretas)
    decrypted_data = cipher_decrypt.decrypt_and_verify(ciphertext, tag)
    
    print("Decrypted Result:", decrypted_data.decode('utf-8'))
    
except ValueError:
    print("Error: Kunci salah atau data telah dimanipulasi!")