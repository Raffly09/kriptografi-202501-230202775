# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik: [Digital Signature]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB] 

---

## 1. Tujuan
(
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.)

---

## 2. Dasar Teori
(Digital Signature adalah skema matematis berbasis kriptografi kunci asimetris (public-key cryptography) yang dirancang untuk memberikan jaminan keamanan informasi setara dengan tanda tangan fisik pada dokumen elektronik, mencakup tiga aspek krusial: otentikasi (memverifikasi identitas pengirim), integritas data (memastikan isi pesan tidak diubah sejak ditandatangani), dan nir-penyangkalan (non-repudiation). Proses ini bekerja dengan cara pengirim menghasilkan nilai hash (ringkasan unik) dari pesan asli dan mengenkripsinya menggunakan kunci privat miliknya untuk membentuk tanda tangan, yang kemudian disertakan bersama pesan tersebut; penerima selanjutnya memverifikasi validitas tanda tangan tersebut dengan mendekripsinya menggunakan kunci publik pengirim dan membandingkan hasil hash-nya, di mana kesesuaian kedua nilai tersebut membuktikan secara matematis bahwa pesan benar-benar berasal dari pemilik kunci privat dan belum dimanipulasi.  )

---

## 3. Alat dan Bahan
(- Python 3.13
- Visual Studio Code   
- Git dan akun GitHub  
- pycryptodome)

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `digital_siganure.py` di folder `praktikum/week9-digitalsiganture/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `digital_siganure.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

    # Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.") ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week9-digital-signature/Screenshot/Hasil%20Eksekusi.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Perbedaan Utama Enkripsi RSA vs. Digital siganture RSA Perbedaannya terletak pada penggunaan kunci dan tujuannya. Enkripsi RSA: Menggunakan Kunci Publik penerima untuk mengenkripsi pesan (tujuan: kerahasiaan). Digital siganture RSA: Menggunakan Kunci Privat pengirim untuk mengenkripsi hash pesan (tujuan: otentikasi dan non-repudiasi). 
- Pertanyaan 2: Integritas: Karena perubahan sekecil apa pun pada pesan asli akan menghasilkan nilai hash yang berbeda, sehingga verifikasi tanda tangan pasti gagal. Otentikasi: Karena tanda tangan yang valid secara matematis hanya bisa dibuat oleh pemilik Kunci Privat yang sah, membuktikan bahwa pesan benar-benar berasal dari pengirim tersebut.  
- Pertanyaan 3: CA berperan sebagai pihak ketiga tepercaya yang memverifikasi identitas pemilik kunci publik. CA menerbitkan sertifikat digital untuk menjamin bahwa kunci publik yang digunakan verifikator benar-benar milik entitas yang diklaim, guna mencegah pemalsuan identitas atau serangan Man-in-the-Middle.
)
---

## 8. Kesimpulan
(Berdasarkan praktikum implementasi Digital Signature menggunakan algoritma RSA dan fungsi hash SHA-256, dapat disimpulkan bahwa metode ini berhasil mendemonstrasikan jaminan otentikasi dan integritas data. Hasil pengujian kode program menunjukkan bahwa verifikasi tanda tangan hanya berhasil (valid) ketika pesan asli dipasangkan dengan tanda tangan yang dibuat oleh kunci privat yang sesuai, sedangkan percobaan modifikasi pada pesan menyebabkan kegagalan verifikasi. Hal ini membuktikan secara praktis bahwa mekanisme kriptografi kunci asimetris efektif dalam mendeteksi manipulasi data sekecil apa pun serta memastikan bahwa pesan benar-benar berasal dari pengirim yang sah (nir-penyangkalan).  )

---

## 9. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-12-10

    week7-digitalsiganture: RSA/DSA )
```
