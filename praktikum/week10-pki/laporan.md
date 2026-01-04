# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [PKI]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB] 


---

## 1. Tujuan
(
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).)

---

## 2. Dasar Teori
(Public Key Infrastructure (PKI) adalah seperangkat peran, kebijakan, perangkat keras, perangkat lunak, dan prosedur yang diperlukan untuk membuat, mengelola, mendistribusikan, menggunakan, menyimpan, dan mencabut sertifikat digital dan mengelola enkripsi kunci publik. Tujuan utama PKI adalah untuk memfasilitasi transfer informasi elektronik yang aman untuk berbagai aktivitas jaringan seperti e-commerce, perbankan internet, dan email rahasia.

Certificate Authority (CA) adalah entitas tepercaya yang menerbitkan sertifikat digital. CA bertindak sebagai pihak ketiga yang menjamin identitas pemegang sertifikat. Dalam model kepercayaan ini, jika pengguna mempercayai CA, maka pengguna juga dapat mempercayai sertifikat yang diterbitkan oleh CA tersebut. 

Self-Signed Certificate adalah sertifikat yang ditandatangani oleh entitas yang sama dengan yang identitasnya disertifikasi oleh sertifikat tersebut. Ini berbeda dengan sertifikat standar yang ditandatangani oleh CA tepercaya. Self-signed certificate berguna untuk lingkungan pengembangan (development) tetapi tidak disarankan untuk produksi publik karena browser tidak memiliki "root trust" terhadap pembuatnya.  )

---

## 3. Alat dan Bahan
(- Python 3.22  
- Sistem Operasi: Windows / Linux / macOS
- Code Editor: Visual Studio Code
- Library Python: (`cryptography`)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `pki.py` di folder `praktikum/week10-pki/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python pki.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi 1](/praktikum/week10-pki/Screenshot/Screenshot%20(251).png)
![Hasil Eksekusi 2](/praktikum/week10-pki/Screenshot/Screenshot%20(249).png)
![Hasil Eksekusi 3](/praktikum/week10-pki/Screenshot/Screenshot%20(250).png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul. 
- Pertanyaan 1: Fungsi utama CA adalah sebagai pihak ketiga yang tepercaya (Trusted Third Party) yang bertugas memverifikasi identitas entitas (seperti website, organisasi, atau individu) dan menerbitkan sertifikat digital yang mengikat kunci publik entitas tersebut dengan identitasnya. CA menjamin bahwa "kunci publik A benar-benar milik organisasi A".) 
- Pertanyaan 2: Self-signed certificate tidak memiliki "chain of trust" ke Root CA yang sudah dikenali oleh sistem operasi atau browser. Akibatnya, Pengguna akan menerima pesan peringatan keamanan ("Your connection is not private") yang menakutkan bagi pengunjung awam serta tidak ada jaminan validasi identitas yang dilakukan oleh pihak independen, sehingga siapa saja bisa membuat sertifikat self-signed yang mengklaim sebagai "https://www.google.com/search?q=google.com", memudahkan serangan phishing.
- Pertanyaan 3: PKI mencegah Man-in-the-Middle (MITM) melalui mekanisme validasi tanda tangan digital, Saat browser terhubung ke server HTTPS, server mengirimkan sertifikatnya. Browser mengecek tanda tangan digital pada sertifikat tersebut menggunakan Public Key dari CA yang menerbitkannya (yang sudah tertanam di browser Jika ada penyerang MITM mencoba mencegat dan memberikan sertifikat palsu, browser akan mendeteksi bahwa sertifikat tersebut tidak ditandatangani oleh CA tepercaya (atau tanda tangannya tidak valid), sehingga koneksi diputus atau diperingatkan.)
---

## 8. Kesimpulan
(Pada praktikum ini, telah berhasil disimulasikan pembuatan sertifikat digital standar X.509 menggunakan Python. Dapat disimpulkan bahwa PKI adalah fondasi keamanan internet modern yang mengandalkan kepercayaan terhadap CA. Tanpa CA yang memvalidasi keaslian pemilik kunci publik, enkripsi saja tidak cukup untuk menjamin keamanan karena rentan terhadap serangan penyamaran (impersonation).  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-12-10

    week10-PKI:Public Key Infrastructure (PKI & Certificate Authority) )
```
```
