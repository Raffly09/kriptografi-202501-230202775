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
(- Python 3.13 
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

ALPHABET_SIZE = 26
ATTEMPTS_PER_SECOND = 1e6
REDUNDANCY_R = 0.75
AES_128_KEYSPACE = 2**128

def calculate_entropy(keyspace_size):
    """
    Menghitung entropi (H) dalam bit berdasarkan ukuran ruang kunci (keyspace).
    H = log2(keyspace_size)
    """
    if keyspace_size <= 0:
        return 0
    return math.log2(keyspace_size)

def calculate_unicity_distance(HK, R=REDUNDANCY_R, A=ALPHABET_SIZE):
    """
    Menghitung Jarak Unicity (N) dalam karakter.
    N = HK / (R * log2(A))
    HK: Entropi kunci (dalam bit)
    R: Redundansi bahasa
    A: Ukuran alfabet
    """
    denominator = R * math.log2(A)
    if denominator == 0:
        return float('inf') 
    return HK / denominator

def calculate_brute_force_time(keyspace_size, attempts_per_second=ATTEMPTS_PER_SECOND):
    """
    Menghitung waktu yang dibutuhkan untuk brute force dalam hari.
    """
 
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

print("="*50)
print("             ANALISIS KEAMANAN KRIPTOGRAFI")
print("="*50)

print("\n--- 1. ENTROPI KUNCI (HK) ---")
print(f"Konstanta Alphabet Size (A): {ALPHABET_SIZE}")

hk_caesar = calculate_entropy(ALPHABET_SIZE)
print(f"Entropy ruang kunci {ALPHABET_SIZE} (Caesar Cipher) = {hk_caesar:.4f} bit")

hk_aes128 = calculate_entropy(AES_128_KEYSPACE)
print(f"Entropy ruang kunci 2^128 (AES-128) = {hk_aes128:.4f} bit")

print("\n--- 2. JARAK UNICITY (N) ---")
print(f"Konstanta Redundansi (R): {REDUNDANCY_R}")

unicity_distance_caesar = calculate_unicity_distance(hk_caesar)
print(f"Jarak Unicity untuk Caesar Cipher (dengan HK={hk_caesar:.4f} bit) = {unicity_distance_caesar:.4f} karakter")

print("\n--- 3. WAKTU BRUTE FORCE ---")
print(f"Konstanta Percobaan/Detik: {ATTEMPTS_PER_SECOND:.0e} (asumsi)")

time_caesar = calculate_brute_force_time(ALPHABET_SIZE)
print(f"Waktu brute force Caesar Cipher ({ALPHABET_SIZE} kunci) = {time_caesar:.6f} hari")

time_aes128 = calculate_brute_force_time(AES_128_KEYSPACE)

print(f"Waktu brute force AES-128 (2^128 kunci) = {time_aes128:.2e} hari")

print("\n"+"="*50) ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week4-entropy-unicity/Screenshot/Hasil.png)

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
(
```
commit dd246f27db620dac62953781a03c9f4d7168ddb1
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-10-23

    week4-entropy_unicity: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force) )
```
