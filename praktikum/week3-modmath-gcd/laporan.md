# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi..)

---

## 2. Dasar Teori
(Konsep Greatest Common Divisor (GCD) atau faktor persekutuan terbesar (FPB) merupakan salah satu prinsip dasar dalam teori bilangan. GCD dari dua bilangan bulat adalah bilangan bulat positif terbesar yang dapat membagi kedua bilangan tersebut tanpa menyisakan sisa. Algoritma yang umum digunakan untuk menghitung GCD adalah Algoritma Euclidean, yang didasarkan pada sifat bahwa gcd(a, b) = gcd(b, a mod b). Proses ini dilakukan secara berulang hingga nilai b menjadi nol, dan nilai a terakhir merupakan hasil GCD. Selain itu, versi perluasan dari algoritma ini, yaitu Extended Euclidean Algorithm, tidak hanya menghitung GCD, tetapi juga mencari pasangan bilangan (x, y) yang memenuhi persamaan linear a*x + b*y = gcd(a, b). Hasil ini sangat penting dalam berbagai bidang kriptografi dan teori modular, terutama dalam perhitungan invers modular.

Aritmetika modular (Modular Arithmetic) adalah sistem operasi aritmetika yang bekerja berdasarkan sisa hasil pembagian suatu bilangan dengan bilangan modulus tertentu. Dalam sistem ini, dua bilangan dikatakan kongruen jika memiliki sisa pembagian yang sama terhadap suatu modulus m, atau ditulis sebagai a ≡ b (mod m). Operasi dasar seperti penjumlahan, pengurangan, perkalian, dan perpangkatan dapat dilakukan dalam ruang modular dengan tetap menjaga hasil dalam rentang 0 ≤ hasil < m. Salah satu operasi penting dalam aritmetika modular adalah invers modular, yaitu bilangan x yang memenuhi (a * x) mod m = 1, yang dapat dihitung menggunakan algoritma Euclidean yang diperluas. Namun, invers modular hanya ada jika a dan m saling relatif prima (gcd(a, m) = 1).

Dalam implementasi komputasi, aritmetika modular dan GCD banyak diterapkan pada bidang kriptografi modern, terutama pada algoritma seperti RSA, Diffie-Hellman, dan Elliptic Curve Cryptography. Operasi modular memungkinkan sistem kriptografi bekerja dengan bilangan besar tanpa menyebabkan overflow, serta menjaga efisiensi dan keamanan. Melalui implementasi menggunakan bahasa Python, perhitungan seperti GCD, invers modular, dan operasi dasar aritmetika modular dapat disimulasikan dengan mudah untuk membantu memahami konsep matematis di balik sistem keamanan digital dan teori bilangan..  )

---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub.)

---

## 4. Langkah Percobaan
(
1. Membuat file `modular_math.py` di folder `praktikum/week3-modular_math/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python modular_math.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# --- Langkah 1: Aritmetika Modular ---
def mod_add(a, b, n):
    """Menghitung (a + b) % n"""
    return (a + b) % n

def mod_sub(a, b, n):
    """Menghitung (a - b) % n"""
    return (a - b) % n

def mod_mul(a, b, n):
    """Menghitung (a * b) % n"""
    return (a * b) % n

def mod_exp(base, exp, n):
    """Menghitung (base^exp) % n menggunakan pow bawaan"""
    return pow(base, exp, n)

# --- Langkah 2: GCD & Algoritma Euclidean ---
def gcd(a, b):
    """Menghitung Greatest Common Divisor (GCD) dari a dan b"""
    while b != 0:
        a, b = b, a % b
    return a

# --- Langkah 3: Extended Euclidean Algorithm & Invers Modular ---
def egcd(a, b):
    """
    Extended Euclidean Algorithm.
    Mengembalikan tuple (g, x, y) sedemikian rupa sehingga:
    a*x + b*y = g = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    # Update x dan y menggunakan hasil rekursif
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def modinv(a, n):
    """
    Mencari invers modular dari a mod n.
    Mengembalikan x sedemikian rupa sehingga (a * x) % n = 1.
    """
    g, x, _ = egcd(a, n)
    if g != 1:
        # Invers modular tidak ada jika a dan n tidak koprima
        return None
    else:
        return x % n

# --- Langkah 4: Logaritma Diskrit (Sederhana) ---
def discrete_log(a, b, n):
    """
    Mencari x dalam a^x ≡ b (mod n) menggunakan brute force.
    Ini hanya efisien untuk n yang kecil.
    """
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    # Tidak ditemukan
    return None

# --- Main Program & Eksekusi Contoh ---
if __name__ == "__main__":
    print("=== Praktikum Week 3: Modular Math, GCD, & Discrete Log ===")
    
    print("\n--- Langkah 1: Aritmetika Modular ---")
    print(f"7 + 5 mod 12 = {mod_add(7, 5, 12)}")
    print(f"7 - 5 mod 12 = {mod_sub(7, 5, 12)}")
    print(f"7 * 5 mod 12 = {mod_mul(7, 5, 12)}")
    print(f"7^128 mod 13 = {mod_exp(7, 128, 13)}")
    
    print("\n--- Langkah 2: GCD (Algoritma Euclidean) ---")
    print(f"gcd(54, 24) = {gcd(54, 24)}")
    print(f"gcd(111, 259) = {gcd(111, 259)}")
    
    print("\n--- Langkah 3: Invers Modular (Extended Euclidean) ---")
    inv_3_11 = modinv(3, 11)
    print(f"Invers 3 mod 11 = {inv_3_11}")
    if inv_3_11 is not None:
        print(f"   -> Pengecekan: (3 * {inv_3_11}) mod 11 = {mod_mul(3, inv_3_11, 11)}")
        
    inv_10_17 = modinv(10, 17)
    print(f"Invers 10 mod 17 = {inv_10_17}")
    if inv_10_17 is not None:
        print(f"   -> Pengecekan: (10 * {inv_10_17}) mod 17 = {mod_mul(10, inv_10_17, 17)}")

    print("\n--- Langkah 4: Logaritma Diskrit (Brute Force) ---")
    # Contoh 1: 3^x ≡ 4 (mod 7)
    x1 = discrete_log(3, 4, 7)
    print(f"Mencari x untuk 3^x ≡ 4 (mod 7)... x = {x1}")
    if x1 is not None:
        print(f"   -> Pengecekan: 3^{x1} mod 7 = {mod_exp(3, x1, 7)}")

    # Contoh 2: 2^x ≡ 3 (mod 13)
    x2 = discrete_log(2, 3, 13)
    print(f"Mencari x untuk 2^x ≡ 3 (mod 13)... x = {x2}")
    if x2 is not None:
        print(f"   -> Pengecekan: 2^{x2} mod 13 = {mod_exp(2, x2, 13)}")
        
    print("\n=== Eksekusi Selesai ===") ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program modmath:

![Hasil Eksekusi](/praktikum/week3-modmath-gcd/screenshot/Hasil.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Peran utamanya adalah untuk membuat operasi yang gampang dilakukan, tapi susah dibalik. Ini seperti mencampur dua warna cat : gampang mencampur biru dan kuning untuk mendapat warna hijau, tapi sangat sulit (mustahil) memisahkan cat hijau itu kembali menjadi biru dan kuning murni. Dalam kriptografi, gampang untuk mengunci (enkripsi) data menggunakan aritmetika modular, tapi sangat susah untuk membukanya (dekripsi) kecuali Anda tahu kunci rahasianya.  
- Pertanyaan 2: Sederhananya, invers modular adalah "kunci pembatal" atau "kunci lawannya".Bayangkan dalam RSA:
- Anda mengunci pesan pakai Kunci Publik (angka $e$).
- Anda hanya bisa membuka pesan itu pakai Kunci Privat (angka $d$).Invers modular adalah proses matematika (menggunakan egcd) untuk menciptakan si Kunci Privat ($d$) yang merupakan pasangan sempurna untuk Kunci Publik ($e$). Tanpa invers modular, kita tidak bisa membuat pasangan kunci yang bisa saling membuka dan mengunci. 
- Pertanyaan 3: Tantangan utamanya adalah jumlah tebakan yang terlalu banyak.Mencari $x$ dalam $a^x \equiv b \pmod{n}$ (logaritma diskrit) itu pada dasarnya adalah "menebak-nebak".
- Jika $n$ (modulus) kecil, misal 7, komputer bisa menebak $x$ dengan cepat (coba $x=1, 2, 3, 4...$).
- Tapi jika $n$ adalah angka yang super besar (terdiri dari ratusan digit), jumlah tebakan yang harus dicoba bisa mencapai triliunan triliun.  
)

---

## 8. Kesimpulan
(
1. Aritmetika Modular: Program ini berhasil menghitung operasi dasar modular, termasuk penjumlahan (mod_add), pengurangan (mod_sub), perkalian (mod_mul), dan eksponensiasi (mod_exp).

2. Greatest Common Divisor (GCD): Program ini dapat menemukan GCD dari dua bilangan menggunakan Algoritma Euclidean, seperti yang ditunjukkan oleh hasil gcd(54, 24) = 6.

3. Invers Modular: Program ini berhasil mengimplementasikan Extended Euclidean Algorithm (egcd) untuk menemukan invers modular (modinv). Hasilnya, seperti Invers 3 mod 11 = 4, telah diverifikasi dengan benar.

4. Logaritma Diskrit: Program ini mampu menyelesaikan masalah logaritma diskrit sederhana (mencari nilai x) menggunakan metode brute-force, seperti pada contoh 3^x ≡ 4 (mod 7) yang menghasilkan x = 4..  )

---

## 9. Commit Log
(
```
commit aaa2b6e9464d07a929892ac2c48a45c47e1146a2
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-10-18

    week3-modularmath: Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)
```