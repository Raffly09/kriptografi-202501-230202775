# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: [Entropy & Unicity Distance]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.)

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
1. Entropy (Entropi)
Entropy dalam kriptografi adalah ukuran dari ketidakpastian (randomness) atau keacakan dari sebuah kunci atau masukan, yang secara langsung berkaitan dengan kekuatan kunci terhadap serangan brute force. Secara matematis, entropi $H$ (biasanya diukur dalam bit) dihitung sebagai $H = \log_2(N)$, di mana $N$ adalah jumlah total kemungkinan kunci dalam ruang kunci (keyspace). Kunci yang kuat harus memiliki entropi tinggi, artinya ruang pencariannya (jumlah kombinasi unik) harus sangat besar, sehingga mustahil untuk dicoba seluruhnya dalam waktu yang realistis. Entropi yang tinggi memastikan bahwa penyerang yang mencoba menemukan kunci melalui serangan brute force akan memerlukan waktu komputasi yang sangat lama. Misalnya, sebuah kunci dengan 128 bit entropi memiliki $2^{128}$ kemungkinan nilai.

2. Serangan Brute Force 
adalah metode serangan di mana penyerang mencoba setiap kemungkinan kunci secara sistematis hingga menemukan kunci yang benar. Kekuatan sebuah sistem kriptografi terhadap serangan ini ditentukan oleh ukuran ruang kunci (keyspace) dan entropi kuncinya. Jika entropi kunci cukup tinggi (misalnya 128 bit atau lebih), jumlah operasi yang diperlukan untuk mencoba semua kunci menjadi tidak mungkin dilakukan dengan teknologi komputasi saat ini dan di masa depan yang dapat diperkirakan. Sebaliknya, kunci dengan entropi rendah (misalnya kunci 40 bit) dapat dengan mudah diretas dalam hitungan detik. Oleh karena itu, evaluasi kekuatan kunci selalu dimulai dengan menghitung dan memastikan bahwa entropi kunci telah memenuhi standar keamanan minimum.

3. Unicity Distance 
adalah konsep dalam kriptanalisis (khususnya untuk stream cipher dan block cipher yang digunakan sebagai stream cipher mode) yang mendefinisikan panjang minimum ciphertext yang diperlukan agar penyerang, dengan menggunakan metode kriptanalisis, dapat secara unik menentukan kunci yang benar. Jarak ini diukur dalam unit karakter atau bit. Secara konseptual, ini adalah titik di mana redundansi yang melekat pada bahasa alami (plaintext) yang dienkripsi telah dieliminasi oleh panjang ciphertext yang cukup. Jika panjang ciphertext yang tersedia melebihi Unicity Distance, kunci yang benar (yang menghasilkan plaintext yang memiliki arti) akan menjadi satu-satunya yang masuk akal, sementara kunci lain akan menghasilkan plaintext yang tidak koheren. Ini adalah metrik penting yang mengukur kerentanan skema enkripsi tertentu terhadap kriptanalisis yang didasarkan pada statistik bahasa, bukan hanya serangan brute force.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub    )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `entropy_unicity.py` di folder `praktikum/week3-entropy_unicity/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python entropy_unicity.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari") ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)

)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Entropy (Entropi) adalah ukuran keacakan (randomness) dan ketidakpastian suatu kunci, yang diukur dalam bit. Semakin tinggi nilai entropi (misalnya, 128 bit atau lebih), semakin besar ruang kunci (keyspace), dan semakin kuat kunci tersebut terhadap serangan brute force.  
- Pertanyaan 2: Unicity Distance adalah panjang minimum ciphertext (teks tersandi) yang diperlukan agar kunci yang benar dapat secara unik ditentukan oleh kriptanalis. Hal ini penting karena menentukan titik di mana penyerang dapat memanfaatkan redundansi statistik bahasa alami (plaintext) untuk memecahkan kunci tanpa harus mencoba setiap kombinasi kunci.
- Pertanyaan 3: Brute force tetap menjadi ancaman karena dua alasan utama:

1. Kunci yang Lemah: Jika pengguna memilih kunci dengan entropi rendah (mudah ditebak), algoritma sekuat apa pun akan mudah ditembus.

2. Peningkatan Komputasi: Daya komputasi penyerang (GPU, komputasi awan) terus meningkat, membuat serangan yang tadinya tidak mungkin menjadi layak secara waktu. 
)
---

## 8. Kesimpulan
(Praktikum ini berhasil menunjukkan bahwa Entropy adalah metrik kritis dalam menentukan kekuatan kunci, di mana kunci dengan entropi tinggi (seperti $2^{128}$ bit) secara efektif menggagalkan serangan brute force karena waktu yang tidak realistis. Perhitungan Unicity Distance mengkonfirmasi bahwa cipher sederhana, seperti Caesar Cipher, rentan terhadap kriptanalisis berbasis statistik setelah hanya sedikit ciphertext tersedia. Dengan demikian, keamanan kriptosistem bergantung pada penggunaan kunci dengan entropi tinggi dan bukan hanya pada kekuatan algoritmanya semata..  )

---

## 9. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-10-23

    week4-entropy_unicity: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force) )
```
