# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: [Cryptosystem]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
Menggambarkan proses enkripsi dan dekripsi sederhana.
Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).
---

## 2. Dasar Teori
Substitusi Acak (Random Substitution Cipher)

Substitusi acak adalah metode di mana setiap karakter dalam alfabet diganti dengan karakter lain secara acak. Tidak seperti Caesar Cipher yang menggunakan pergeseran tetap, metode ini membuat pasangan acak antara karakter asli dan karakter hasil enkripsi.

Langkah-langkah:

Membuat tabel substitusi acak
Semua huruf besar (A–Z), huruf kecil (a–z), dan angka (0–9) dikumpulkan. Kemudian urutan karakter diacak menggunakan fungsi random.shuffle().

Enkripsi
Setiap karakter pada plaintext diganti sesuai dengan tabel substitusi. Jika ada karakter non-alfabetik (misalnya spasi atau simbol), karakter tersebut dibiarkan tetap.

Dekripsi
Program membuat tabel kebalikan dari tabel substitusi. Setiap karakter pada ciphertext diganti kembali dengan karakter aslinya menggunakan tabel kebalikan ini.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub   )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:
 
```python
import string
import random

# --- Membuat tabel substitusi ---
def buat_tabel_substitusi():
    karakter_asli = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    karakter_acak = karakter_asli.copy()
    random.shuffle(karakter_acak)
    return dict(zip(karakter_asli, karakter_acak))

# --- Enkripsi ---
def enkripsi_substitusi(teks, tabel):
    hasil = ""
    for char in teks:
        if char in tabel:
            hasil += tabel[char]
        else:
            hasil += char  # karakter lain (spasi, simbol) tidak berubah
    return hasil

# --- Dekripsi ---
def dekripsi_substitusi(teks, tabel):
    tabel_kebalikan = {v: k for k, v in tabel.items()}
    hasil = ""
    for char in teks:
        if char in tabel_kebalikan:
            hasil += tabel_kebalikan[char]
        else:
            hasil += char
    return hasil

# --- Program utama ---
print("=== Program Enkripsi Substitusi Acak (Huruf + Angka) ===")

tabel_substitusi = buat_tabel_substitusi()

teks_asli = input("Masukkan teks asli: ")
teks_terenkripsi = enkripsi_substitusi(teks_asli, tabel_substitusi)
teks_didekripsi = dekripsi_substitusi(teks_terenkripsi, tabel_substitusi)

print("\nTabel Substitusi (Kunci):")
print(tabel_substitusi)
print("\nHasil Enkripsi :", teks_terenkripsi)
print("Hasil Dekripsi :", teks_didekripsi) ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program random substitution cipher:

![Hasil Eksekusi](/praktikum/week2-cryptosystem/Screenshot/hasil_eksekusi.png)
![Diagram Kriptosistem](/praktikum/week2-cryptosystem/Screenshot/diagram_kriptosistem.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Plaintext, yaitu pesan asli yang akan dienkripsi. Ciphertext, yaitu hasil dari proses enkripsi yang tidak dapat dibaca tanpa kunci. Algoritma enkripsi, yaitu aturan atau prosedur yang digunakan untuk mengubah plaintext menjadi ciphertext. Algoritma dekripsi, yaitu aturan yang digunakan untuk mengembalikan ciphertext menjadi plaintext. Kunci (key), yaitu parameter rahasia yang mengatur proses enkripsi dan dekripsi sehingga hanya pihak yang memiliki kunci yang dapat membaca pesan.  
- Pertanyaan 2: Kelebihan sistem simetris:

Proses enkripsi dan dekripsi lebih cepat dan efisien.

Algoritma lebih sederhana dan membutuhkan sumber daya komputasi yang lebih kecil.

Kelemahan sistem simetris:

Memiliki masalah pada distribusi kunci, karena pengirim dan penerima harus memiliki kunci yang sama secara rahasia.

Kurang cocok untuk sistem komunikasi skala besar karena setiap pasangan pengguna membutuhkan kunci unik.
- Pertanyaan 3: Distribusi kunci menjadi masalah utama karena pengirim dan penerima harus memiliki kunci rahasia yang sama sebelum proses komunikasi dapat dilakukan. Jika kunci tersebut dikirim melalui jaringan yang tidak aman, maka ada risiko pihak ketiga dapat menyadap dan mengetahui kunci tersebut. Tanpa mekanisme distribusi kunci yang aman, seluruh sistem enkripsi simetris dapat dengan mudah ditembus, karena keamanan data sepenuhnya bergantung pada kerahasiaan kunci.
)
---

## 8. Kesimpulan
(Algoritma substitusi acak (random substitution cipher) adalah salah satu bentuk enkripsi klasik yang bekerja dengan cara mengganti setiap karakter dalam pesan asli (plaintext) dengan karakter lain secara acak berdasarkan tabel substitusi yang berfungsi sebagai kunci. Proses enkripsi dilakukan dengan mencocokkan setiap huruf dan angka dengan pasangannya dalam tabel acak tersebut, sedangkan proses dekripsi dilakukan dengan menggunakan tabel kebalikan dari kunci yang sama. Metode ini lebih kuat dibandingkan dengan Caesar Cipher karena tidak menggunakan pola pergeseran tetap, melainkan penggantian acak yang menghasilkan kombinasi sangat banyak dan sulit ditebak tanpa mengetahui kuncinya. Dengan demikian, substitusi acak dapat dikatakan efektif untuk memahami konsep dasar keamanan data dan prinsip kerja kriptografi klasik berbasis substitusi..  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 8ac8d8bece7850acdb403f6a689b91d806827e22
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-10-12

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
