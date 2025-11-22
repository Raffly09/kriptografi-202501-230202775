# Laporan Praktikum Kriptografi
Minggu ke-: 6
Topik: [Cipher Modern]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB] 

---

## 1. Tujuan
(
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.
.)

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
RSA (Rivest-Shamir-Adleman) adalah algoritma kriptografi jenis asimetris yang mengandalkan dua kunci berbeda: kunci publik untuk mengunci pesan dan kunci privat untuk membukanya. Keamanan RSA berpusat pada konsep matematika bahwa sangat mudah untuk mengalikan dua angka prima besar, tetapi sangat sulit (hampir mustahil) untuk memecah hasil perkalian tersebut kembali ke angka asalnya. Karena proses matematikanya rumit dan berat, RSA dilengkapi dengan metode pengacakan tambahan (seperti OAEP) agar lebih aman, namun biasanya hanya digunakan untuk data kecil seperti pengiriman kunci rahasia, bukan untuk mengenkripsi file besar.

AES (Advanced Encryption Standard) adalah algoritma kriptografi jenis simetris yang hanya menggunakan satu kunci yang sama untuk proses enkripsi dan dekripsi. Berbeda dengan RSA yang berbasis hitungan matematika berat, AES bekerja dengan cara memotong data menjadi blok-blok kecil, lalu mengacaknya berulang kali melalui proses substitusi (penggantian) dan permutasi (penggeseran) yang sangat cepat. Karena kecepatannya yang tinggi dan strukturnya yang efisien, AES menjadi standar dunia untuk mengamankan data dalam jumlah besar, dan sering kali menggunakan mode modern (seperti GCM) yang tidak chỉ menyandikan data tetapi juga memastikan data tersebut tidak diubah oleh peretas.  )

---

## 3. Alat dan Bahan
(- Python 3.13
- Visual Studio Code   
- Git dan akun GitHub  
- Library tambahan (RSA), (PKCS1_OAEP), (get_random_bytes), (base64)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `AES_Cipher.py` dan `RSA_Cipher.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Membuat program berdasarkan panduan praktikum.
3. Menjalankan program dengan perintah `python Caesar_Cipher.py dan Vigenere_Cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
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
    ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi RSA Cipher](/praktikum/week6-cipher-modern/Screenshot/Hasil%20RSA.png)
![Hasil Eksekusi AES Cipher](/praktikum/week6-cipher-modern/Screenshot/Hasil%20AES.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: DES (Data Encryption Standard): Algoritma Simetris (1 kunci). Menggunakan kunci pendek (56-bit). Saat ini dianggap tidak aman karena mudah diretas dengan brute force sedangkan AES (Advanced Encryption Standard): Algoritma Simetris (1 kunci). Menggunakan kunci panjang (128, 192, atau 256-bit). Sangat aman dan menjadi standar enkripsi dunia saat ini dan RSA (Rivest-Shamir-Adleman): Algoritma Asimetris (2 kunci: Publik & Privat). Keamanan berbasis kesulitan matematika (faktorisasi bilangan prima). Sangat aman untuk pertukaran kunci, namun lambat untuk data besar.  
- Pertanyaan 2: Alasan utamanya adalah Keamanan dan Panjang Kunci. Kunci DES hanya 56-bit, yang dapat dibongkar oleh komputer modern dalam hitungan jam (rentan serangan brute force). Sebaliknya, AES memiliki kunci minimal 128-bit yang secara komputasi hampir mustahil ditembus dengan teknologi saat ini. Selain itu, arsitektur AES lebih efisien dan cepat pada perangkat keras modern.  
- Pertanyaan 3: Karena RSA menggunakan dua kunci yang berbeda namun berpasangan secara matematis: Kunci Publik (untuk mengenkripsi/mengunci) dan Kunci Privat (untuk mendekripsi/membuka). dengan proses sebagai berikut:
1. Pilih dua bilangan prima besar acak, $p$ dan $q$.
2. Hitung modulus $n = p \times q$ (ini menjadi bagian dari kunci publik).
3. Hitung fungsi Euler $\phi(n) = (p-1)(q-1)$.
4. Pilih angka $e$ (kunci publik) yang relatif prima terhadap $\phi(n)$.
5. Hitung angka $d$ (kunci privat) yang merupakan invers dari $e$ modulo $\phi(n)$. 
)
---

## 8. Kesimpulan
(Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa AES jauh lebih unggul dan aman dibandingkan DES sebagai standar enkripsi simetris karena ukuran kuncinya yang lebih panjang dan ketahanan terhadap serangan brute force. Selain itu, terdapat pembagian peran yang jelas di mana RSA (asimetris) lebih efektif untuk mekanisme pertukaran kunci, sementara AES lebih efisien untuk mengenkripsi data berukuran besar. Keberhasilan implementasi kriptografi modern ini juga sangat bergantung pada penggunaan mode operasi yang tepat, seperti AES-GCM dan padding OAEP, untuk menjamin kerahasiaan sekaligus integritas data.  )

---

## 9. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 4f31a26af40d4b54795d24483892af8f1760d9d3
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-11-22

    week5-cryptosystem: Cipher Modern )
```
