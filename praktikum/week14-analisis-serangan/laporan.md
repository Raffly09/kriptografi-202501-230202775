# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: [Analisis Serangan]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.)

---

## 2. Dasar Teori
(Kriptografi modern tidak hanya bergantung pada kerahasiaan algoritma, tetapi pada kekuatan kunci dan implementasi yang benar. Salah satu serangan paling umum pada sistem autentikasi adalah Dictionary Attack dan Rainbow Table Attack.

1. Dictionary Attack: Mencoba menebak password dengan menggunakan daftar kata-kata umum (kamus).

2. Rainbow Table: Menggunakan tabel raksasa berisi pasangan plaintext dan hash yang sudah dihitung sebelumnya untuk membalikkan fungsi hash dengan instan.

Serangan ini sangat efektif jika sistem menggunakan algoritma hashing yang cepat (seperti MD5 atau SHA-1) tanpa menambahkan Salt (data acak tambahan).  )

---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Mencari kasus serangan nyata.
2. Menganalisis bentuk dan dampak serangan.
3. Meminta Bantuan AI untuk rephrase dan menambahkan detail artikel.)

---

## 5. Hasil dan Pembahasan
(
## Langkah 1 — Identifikasi Serangan (Studi Kasus Nyata)
Kasus: Kebocoran Data LinkedIn (2012)
Pada tahun 2012, jejaring sosial profesional LinkedIn mengalami peretasan besar di mana sekitar 6,5 juta hash password pengguna dicuri dan dipublikasikan di forum peretas Rusia.

Vektor Serangan: Peretas berhasil melakukan SQL Injection untuk mengambil dump database pengguna.

Jenis Serangan Kriptografi: Setelah mendapatkan database, peretas menggunakan serangan Dictionary Attack dan Rainbow Table untuk memecahkan jutaan password dalam waktu singkat.

Sumber Berita:

BBC News: "LinkedIn confirms account passwords hacked" 🔗 Link: https://www.bbc.com/news/technology-18330566

New York Times: "LinkedIn Breached: Passwords Leaked" 🔗 Link: https://bits.blogs.nytimes.com/2012/06/06/linkedin-passwords-compromised/

## Langkah 2 — Evaluasi Kelemahan
Berdasarkan analisis insiden LinkedIn tersebut, berikut adalah evaluasi kelemahannya:

Penggunaan Algoritma Lemah (SHA-1): LinkedIn saat itu menggunakan algoritma SHA-1. SHA-1 adalah algoritma yang dirancang untuk kecepatan (fast hashing). Kecepatan ini justru menjadi kelemahan dalam penyimpanan password, karena peretas dapat mencoba jutaan kombinasi per detik menggunakan perangkat keras standar.

Tidak Menggunakan Salt (Unsalted): Kelemahan fatalnya adalah tidak adanya Salt.

Tanpa Salt: Jika User A dan User B memiliki password sama ("rahasia123"), hash mereka akan identik. Peretas cukup memecahkan satu hash untuk mengetahui password semua orang yang menggunakan kata sandi tersebut.

Dampak: Ini memungkinkan penggunaan Rainbow Table, sehingga proses cracking menjadi hampir instan untuk password yang umum.

Kesimpulan Evaluasi: Kelemahan bukan pada rusaknya algoritma SHA-1 secara matematis, melainkan pada implementasi konfigurasi sistem yang salah (memilih algoritma cepat tanpa salting untuk tujuan penyimpanan password).

## Langkah 3 — Rekomendasi Solusi
Jika Anda bertugas memperbaiki sistem tersebut, berikut adalah rekomendasi teknisnya:

1. Solusi Algoritma
Ganti SHA-1 dengan algoritma Hashing Lambat (Slow Hashing) yang dirancang khusus untuk password, yaitu:

bcrypt (standar industri saat ini).

Argon2 (pemenang Password Hashing Competition).

2. Alasan Pemilihan
Work Factor (Cost): Algoritma seperti bcrypt memiliki parameter work factor yang bisa diatur. Ini membuat proses hashing sengaja diperlambat (misalnya 0,5 detik per hash). Bagi pengguna asli, 0,5 detik tidak terasa. Bagi peretas yang ingin mencoba 1 miliar password, waktu yang dibutuhkan menjadi jutaan tahun.

Salting Otomatis: Algoritma modern ini secara otomatis menambahkan salt unik dan panjang pada setiap password, sehingga serangan Rainbow Table tidak berguna.
)

---

## 6. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Karena dulunya pengembang memprioritaskan performa (kecepatan login) dan kurangnya kesadaran bahwa kecepatan hardware hacking (GPU) akan meningkat drastis. Migrasi dari sistem lama ke baru juga sulit karena mengharuskan semua pengguna mereset password.  
- Pertanyaan 2: Kelemahan algoritma adalah cacat matematika pada rumusnya (contoh: MD5 collision). Kelemahan implementasi adalah cara pakainya yang salah (contoh: memakai SHA-1 yang 'sehat' tapi tanpa Salt). 
- Pertanyaan 3: Menerapkan Crypto-agility (kemampuan update algoritma tanpa rombak aplikasi) dan rutin melakukan audit keamanan (Penetration Testing).
)
---

## 7. Kesimpulan
(Kerentanan Algoritma Cepat: Algoritma hashing konvensional seperti MD5 dan SHA-1 sangat tidak aman untuk penyimpanan password karena kecepatan komputasinya yang tinggi. Hal ini memudahkan peretas melakukan Dictionary Attack atau Brute Force untuk memecahkan jutaan hash dalam waktu singkat. Kasus LinkedIn membuktikan bahwa ketiadaan Salt (bumbu/data acak) adalah kesalahan fatal. Tanpa salt, hash dari password yang sama akan selalu identik, memungkinkan penggunaan Rainbow Table untuk peretasan massal secara instan. Keamanan sistem autentikasi saat ini tidak lagi bergantung pada kerahasiaan algoritma, melainkan pada Work Factor (biaya komputasi). Penggunaan algoritma slow hashing seperti bcrypt atau Argon2 adalah standar wajib karena algoritma ini sengaja diperlambat untuk mempersulit serangan brute force tanpa mengganggu kenyamanan pengguna asli.  )

---

## 8. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-01-05

    week14-Analisis Serangan: Analisis serangan dan laporan )
```
