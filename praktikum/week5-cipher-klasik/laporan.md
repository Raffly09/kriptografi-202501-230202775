# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: [Cipher Klasik]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.
- Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
- Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
- Mengimplementasikan algoritma transposisi sederhana.
- Menjelaskan kelemahan algoritma kriptografi klasik..)

---

## 2. Dasar Teori
(Kriptografi Klasik adalah fondasi ilmu menyembuniykan pesan yang bekerja dengan mengubah plaintext (Pesan Asli) menjadi ciphertext (Pesan Enkripsi) menggunakan kunci. Metode ini terbagi menjadi dua kategori utama: Substitusi dan Transposisi. Dalam metode substitusi, huruf asli diganti dengan huruf lain. Contohnya adalah Caesar Cipher yang merupakan substitusi monoalfabetik sederhana (pergeseran huruf tetap) dan rentan terhadap serangan frekuensi. Untuk memperkuatnya, diciptakan Vigenère Cipher, yang menggunakan kata kunci untuk melakukan substitusi polialfabetik (pergeseran berubah-ubah), menjadikannya lebih aman namun masih rentan jika panjang kuncinya dapat dipecahkan.

Kategori kedua, Transposisi Cipher, tidak mengubah huruf itu sendiri tetapi memutarbalikkan atau mengubah posisi (permutasi) huruf-huruf dalam pesan. Contohnya adalah Transposisi Kolom, di mana plaintext disusun dalam barisan kolom, dan ciphertext dibaca berdasarkan urutan kolom yang ditentukan oleh kunci. Ciri khas Transposisi adalah frekuensi kemunculan huruf pada ciphertext akan tetap sama dengan plaintext. Secara keseluruhan, meskipun relatif sederhana, Cipher Klasik ini menjadi dasar konseptual penting yang membentuk pengembangan algoritma kriptografi modern yang jauh lebih kompleks.  )

---

## 3. Alat dan Bahan
(- Python 3.13
- Visual Studio Code   
- Git dan akun GitHub  
- Library tambahan (String)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `Caesar_Cipher.py` dan `Vigenere_Cipher.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Membuat program berdasarkan panduan praktikum.
3. Menjalankan program dengan perintah `python Caesar_Cipher.py dan Vigenere_Cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# Caesare Cipher
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
        key = str(shift)  
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

# Vigenere Cipher
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
    main()...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi Caesare Cipher](/praktikum/week5-cipher-klasik/Screenshot/Caesare%20Chipher.png)
![Hasil Eksekusi Vigenere Cipher](/praktikum/week5-cipher-klasik/Screenshot/Vigenere%20Cipher.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Kelemahan Utama Caesar dan Vigenère Cipher:
- Caesar Cipher: Hanya memiliki 25 kunci dan bersifat monoalfabetik, sehingga rentan terhadap Brute Force dan Analisis Frekuensi sederhana.
- Vigenère Cipher: Bersifat polialfabetik, namun kunci yang berulang membuatnya rentan terhadap serangan penentuan panjang kunci (Metode Kasiski atau IOC). 
- Pertanyaan 2: Cipher klasik gagal menyembunyikan pola statistik alami bahasa (seperti kemunculan huruf 'A' atau 'E' yang lebih sering). Substitusi monoalfabetik mempertahankan pola ini, sementara transposisi bahkan mempertahankan frekuensi persis setiap huruf.
- Pertanyaan 3: kelebihan dan kelemahan cipher substitusi vs transposisi:
    - Kelebihan subtitusi: Mengubah nilai karakter, dapat menyamarkan frekuensi, terutama Polialfabetik.
    - Kelemahan subtitusi: Rentan jika pola substitusi tetap (Monoalfabetik) atau jika panjang kunci diketahui (Vigenère).
    - Kelebihan Transposisi: Menjaga karakter asli, mudah diterapkan.
    - Kelemahan Transposisi: Gagal menyembunyikan statistik frekuensi karena hanya mengubah urutan huruf.
)
---

## 8. Kesimpulan
(Praktikum implementasi Kriptografi Klasik ini berhasil menunjukkan penerapan algoritma Caesar Cipher dan Vigenère Cipher sebagai contoh metode substitusi. Caesar Cipher terbukti paling sederhana dan rentan karena sifat monoalfabetiknya, sementara Vigenère memberikan keamanan yang lebih baik melalui substitusi polialfabetik. Meskipun demikian, semua algoritma klasik, baik substitusi maupun transposisi, memiliki kelemahan mendasar yaitu kerentanan terhadap Analisis Frekuensi, yang disebabkan oleh kegagalan menyembunyikan pola statistik bahasa asli atau penggunaan kunci yang berulang.  )

---

## 9. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 4f31a26af40d4b54795d24483892af8f1760d9d3
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-11-07

    week5-cryptosystem: Cipher Klasik )
```
