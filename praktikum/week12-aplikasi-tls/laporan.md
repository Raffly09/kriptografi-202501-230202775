# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: [Aolikasi TLS]  
Nama: [Nama Mahasiswa]  
NIM: [NIM Mahasiswa]  
Kelas: [Kelas]  

---

## 1. Tujuan
(
1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2. Menjelaskan enkripsi dalam transaksi e-commerce.
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.)

---

## 2. Dasar Teori
(Transport Layer Security (TLS) adalah protokol kriptografi yang dirancang untuk memberikan keamanan komunikasi melalui jaringan komputer. TLS merupakan penerus dari Secure Sockets Layer (SSL). Protokol ini menjamin privasi (kerahasiaan), integritas data, dan autentikasi antara aplikasi klien (seperti browser web) dan server.

Dalam implementasinya, TLS menggunakan Sertifikat Digital yang dikeluarkan oleh Certificate Authority (CA) terpercaya. Sertifikat ini memuat kunci publik server dan identitas pemilik situs. Saat koneksi terjadi (handshake), klien dan server menyepakati algoritma enkripsi (Cipher Suite) untuk mengamankan data yang dikirim.

E-commerce sangat bergantung pada TLS (ditandai dengan HTTPS) untuk melindungi data sensitif pengguna, seperti password saat login dan nomor kartu kredit saat transaksi. Tanpa enkripsi, data ini akan dikirim dalam bentuk teks biasa (plaintext) yang rentan terhadap penyadapan.  )

---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `TLS.py` di folder `praktikum/week12-secretsharing/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python TLS.py`.)

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
## 6.1 
(
![6.1](/praktikum/week12-aplikasi-tls/Screenshot/Screenshot%202026-01-04%20091051.png)
![Sertifikat Tokopedia](/praktikum/week12-aplikasi-tls/Screenshot/Tokopedia.png)
![Sertifikat Shopee](/praktikum/week12-aplikasi-tls/Screenshot/Shopee.png)

Dari hasil pengamatan, kedua situs menggunakan protokol HTTPS yang aman. Browser menunjukkan ikon gembok, menandakan sertifikat valid dan dikeluarkan oleh CA terpercaya (seperti Google Trust Services atau DigiCert). Algoritma yang digunakan umumnya adalah AES (Advanced Encryption Standard) untuk enkripsi data simetris dan RSA atau ECDHE untuk pertukaran kunci. Ini memastikan bahwa data yang lewat antara laptop saya dan server mereka tidak bisa dibaca oleh pihak ketiga.
)

## 6.2 
(
Dalam transaksi e-commerce, titik paling krusial adalah saat Login dan Checkout (Pembayaran).

1. Mekanisme Perlindungan: Saat saya memasukkan password atau PIN, data tersebut dienkripsi oleh browser menggunakan kunci publik server sebelum dikirim. Hanya server e-commerce yang memiliki kunci privat yang bisa mendekripsinya.

2. Ancaman Tanpa TLS: Jika website hanya menggunakan HTTP (tanpa SSL), maka terjadi ancaman Man-in-the-Middle (MitM). Penyerang yang berada dalam satu jaringan Wi-Fi (misalnya di kafe) dapat menggunakan alat sniffing (seperti Wireshark) untuk menangkap paket data. Tanpa enkripsi, password dan nomor kartu kredit akan terlihat jelas (plaintext), memungkinkan pencurian identitas dan kerugian finansial.
)

## 6.3
(
Isu 1: Audit Email Perusahaan Dilema: Apakah perusahaan boleh mendekripsi/membaca email karyawan? Analisis: Secara etika bisnis dan hukum, fasilitas email kantor adalah properti perusahaan. Perusahaan seringkali memiliki hak untuk mengaudit komunikasi demi mencegah kebocoran rahasia dagang atau aktivitas ilegal. Namun, karyawan harus diberitahu sejak awal (melalui kontrak kerja) bahwa komunikasi mereka tidak bersifat pribadi 100% pada perangkat kantor. Etika yang baik menuntut transparansi kebijakan, bukan pengawasan diam-diam.

Isu 2: Pengawasan Pemerintah (Surveillance) Dilema: Keseimbangan antara privasi warga vs keamanan negara. Analisis: Pemerintah sering meminta "backdoor" atau akses ke komunikasi terenkripsi (seperti kasus FBI vs Apple, atau regulasi di berbagai negara) dengan alasan mencegah terorisme. Evaluasi: Secara teknis, membuat backdoor untuk pemerintah akan melemahkan keamanan bagi semua orang, karena backdoor tersebut bisa ditemukan dan dieksploitasi oleh peretas jahat. Privasi adalah hak asasi, namun pengawasan mungkin dibenarkan jika ada surat perintah pengadilan yang spesifik (lawful interception), bukan pengawasan massal tanpa pandang bulu.
)
---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: (Hypertext Transfer Protocol) mengirimkan data dalam format teks biasa (plaintext) melalui port 80, sehingga tidak aman. HTTPS (Hypertext Transfer Protocol Secure) menambahkan lapisan enkripsi SSL/TLS melalui port 443, sehingga data yang dikirim teracak dan tidak bisa dibaca oleh penyadap. 
- Pertanyaan 2: Sertifikat digital berfungsi sebagai "KTP" atau identitas digital. Ia menjamin bahwa kunci publik yang kita terima benar-benar milik website yang kita tuju (autentikasi), bukan milik penyerang yang menyamar. Tanpa sertifikat yang valid dari CA, kita tidak bisa memastikan lawan bicara kita adalah server yang asli.
- Pertanyaan 3: Kriptografi (seperti End-to-End Encryption) memastikan hanya pengirim dan penerima yang bisa membaca pesan, melindungi privasi pengguna dari peretas maupun pengawasan massal. Namun, ini menjadi tantangan hukum ketika penegak hukum membutuhkan bukti dari percakapan kriminal (teroris/koruptor) tetapi tidak bisa mengaksesnya karena enkripsi yang kuat. Ini memicu perdebatan antara "Hak atas Privasi" melawan "Keamanan Nasional".
)
---

## 8. Kesimpulan
(Berdasarkan praktikum ini, dapat disimpulkan bahwa penerapan SSL/TLS (HTTPS) adalah syarat mutlak bagi keamanan e-commerce untuk menjamin kerahasiaan data transaksi dan kepercayaan pengguna. Sertifikat digital memegang peran vital dalam autentikasi server. Di sisi lain, kekuatan kriptografi memunculkan dilema etika yang kompleks antara hak privasi individu dan kebutuhan pengawasan untuk keamanan organisasi atau negara..  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- DigiCert. (n.d).. *What is an SSL Certificate?*.  
- Stallings, W. *Cryptography and Network Security*.
- Cloudflare. (n.d). *What is HTTPS?*  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 14379d34159137bb6a10c6c670afe31a76b8e981
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-01-04

    week7-aplikasi TLS )
````
