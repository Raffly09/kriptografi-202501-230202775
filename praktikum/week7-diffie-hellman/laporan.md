# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: [Diffie-Hellman Protocol]  
Nama: [Raffly Ardya Putra]  
NIM: [230202775]  
Kelas: [5IKRB] 

---

## 1. Tujuan
(
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).)

---

## 2. Dasar Teori
(Diffie-Hellman (DH) adalah salah satu protokol kriptografi kunci publik (asimetris) pertama yang dikembangkan. Protokol ini memungkinkan dua pihak yang tidak memiliki pengetahuan sebelumnya satu sama lain untuk secara aman menyepakati sebuah kunci rahasia bersama melalui saluran komunikasi yang tidak aman (yaitu, dapat disadap). Tujuan DH bukan untuk mengenkripsi data secara langsung, melainkan untuk mempertukarkan kunci simetris yang kemudian dapat digunakan untuk komunikasi yang lebih efisien (misalnya, menggunakan AES atau sejenisnya).  )

---

## 3. Alat dan Bahan
(- Python 3.13
- Visual Studio Code   
- Git dan akun GitHub  
- Library tambahan)

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `Diffie_Hellman.py` di folder `praktikum/week7-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `Diffie_Hellman.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import random

def generate_keys(p, g):
    """
    Menghasilkan kunci pribadi (secret) dan kunci publik (public) untuk satu pihak.
    """
    # Kunci pribadi harus antara 1 dan p-1
    secret_key = random.randint(1, p - 1)
    
    # Kunci publik dihitung sebagai g^secret_key mod p
    public_key = pow(g, secret_key, p)
    
    return secret_key, public_key

def calculate_shared_secret(secret_key, other_public_key, p):
    """
    Menghitung kunci rahasia bersama menggunakan kunci pribadi sendiri dan kunci publik pihak lain.
    """
    # Kunci bersama = (Kunci_publik_pihak_lain^secret_key) mod p
    shared_secret = pow(other_public_key, secret_key, p)
    
    return shared_secret

# --- Parameter Umum ---
p = 23  
g = 5   
print(f"Parameter Publik: p={p}, g={g}\n")
print("-" * 30)

# --- FASE 1: Pembuatan dan Pertukaran Kunci Publik ---

# Alice menghasilkan kunci
a_secret, A_public = generate_keys(p, g)
print(f"Alice Secret Key (a): {a_secret}")
print(f"Alice Public Key (A): {A_public}")

# Bob menghasilkan kunci
b_secret, B_public = generate_keys(p, g)
print(f"Bob Secret Key (b):   {b_secret}")
print(f"Bob Public Key (B):   {B_public}\n")

print("Pertukaran Kunci Publik (A dan B)...")
print("-" * 30)

# --- FASE 2: Perhitungan Kunci Rahasia Bersama ---

# Alice menghitung kunci rahasia bersama (B^a mod p)
shared_secret_A = calculate_shared_secret(a_secret, B_public, p)

# Bob menghitung kunci rahasia bersama (A^b mod p)
shared_secret_B = calculate_shared_secret(b_secret, A_public, p)

# --- Verifikasi Hasil ---
print(f"Kunci Bersama Alice (B^a mod p): {shared_secret_A}")
print(f"Kunci Bersama Bob (A^b mod p):   {shared_secret_B}")

if shared_secret_A == shared_secret_B:
    print("\n✅ Verifikasi Sukses! Kunci rahasia bersama berhasil dibuat.")
else:
    print("\n❌ Verifikasi Gagal! Ada kesalahan dalam perhitungan kunci.") ...
```
)

---

## 6. Hasil dan Pembahasan
(Simulasi ini secara jelas menunjukkan kelemahan utama dari protokol Diffie-Hellman Key Exchange dasar, yaitu kurangnya otentikasi. Ketika Eve (penyerang) mencegat dan mengganti kunci publik ($A$ dan $B$) dengan kunci publiknya sendiri ($E$), Eve berhasil membangun dua saluran komunikasi rahasia terpisah: satu dengan Alice ($g^{ae} \bmod p$) dan satu lagi dengan Bob ($g^{be} \bmod p$). Akibatnya, Alice dan Bob, meskipun yakin mereka telah menyepakati satu kunci rahasia bersama ($g^{ab} \bmod p$), justru berakhir dengan kunci yang berbeda dan berkomunikasi secara tidak sengaja melalui Eve. Eve dapat mendekripsi pesan yang datang dari Alice menggunakan kunci $g^{ae} \bmod p$, membacanya, dan mengenkripsinya kembali dengan $g^{be} \bmod p$ sebelum meneruskannya ke Bob. Seluruh proses ini membuat komunikasi rentan, membuktikan bahwa Diffie-Hellman, dalam bentuknya yang murni, memerlukan mekanisme tambahan, seperti sertifikat digital atau tanda tangan, untuk memverifikasi identitas pihak yang bertukar kunci dan mencegah serangan MITM.

Hasil eksekusi program:

![Hasil Eksekusi](/praktikum/week7-diffie-hellman/Screenshot/Hasil_Diffie-Hellman.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Diffie-Hellman memungkinkan pertukaran kunci di saluran publik karena keamanannya didasarkan pada kesulitan komputasi dari Masalah Logaritma Diskrit (Discrete Logarithm Problem/DLP). Meskipun kunci publik ($A = g^a \bmod p$ dan $B = g^b \bmod p$) dibagikan secara terbuka, menemukan kunci rahasia pribadi ($a$ atau $b$) dari kunci publik yang diketahui, generator ($g$), dan modulus ($p$) adalah tidak praktis secara komputasi jika $p$ adalah bilangan prima yang sangat besar. Dengan demikian, penyadap pasif hanya dapat melihat nilai yang mudah dihitung, tetapi tidak dapat menghitung kembali kunci rahasia yang mendasarinya.
- Pertanyaan 2: Kelemahan utama protokol Diffie-Hellman murni adalah kurangnya otentikasi atau verifikasi identitas. Protokol ini tidak memiliki mekanisme untuk memastikan bahwa kunci publik yang diterima benar-benar berasal dari pihak yang diklaim. Kurangnya otentikasi ini membuat Diffie-Hellman sangat rentan terhadap serangan Man-in-the-Middle (MITM), di mana pihak ketiga (Eve) dapat mencegat dan mengganti kunci publik, sehingga berhasil menyepakati dua kunci rahasia yang berbeda—satu dengan Alice dan satu dengan Bob—tanpa disadari oleh kedua belah pihak.
- Pertanyaan 3: Untuk mencegah serangan MITM, Diffie-Hellman harus diperkuat dengan mekanisme otentikasi yang terpisah. Cara yang paling umum adalah menggunakan Sertifikat Digital (Digital Certificates) dan Tanda Tangan Digital (Digital Signatures). Sertifikat digital, yang dikeluarkan oleh Otoritas Sertifikasi (CA) tepercaya, mengikat kunci publik seseorang ke identitasnya yang sebenarnya, sehingga Alice dan Bob dapat memverifikasi kunci publik yang mereka terima benar-benar milik pihak yang mereka ajak berkomunikasi sebelum melanjutkan dengan pertukaran kunci Diffie-Hellman. Ini adalah praktik standar yang digunakan dalam protokol keamanan modern seperti TLS/SSL.
)

---

## 8. Kesimpulan
(Simulasi protokol Diffie-Hellman berhasil menunjukkan bahwa dua pihak dapat menyepakati kunci rahasia bersama melalui saluran yang tidak aman, memanfaatkan kesulitan komputasi dari Masalah Logaritma Diskrit. Namun, simulasi serangan Man-in-the-Middle (MITM) membuktikan bahwa protokol murni ini rentan karena tidak adanya otentikasi, memungkinkan penyerang untuk membuat dua kunci rahasia yang terpisah dan menguping seluruh komunikasi tanpa terdeteksi. Oleh karena itu, dalam aplikasi dunia nyata, Diffie-Hellman harus selalu diintegrasikan dengan mekanisme otentikasi, seperti Sertifikat Digital (misalnya, pada TLS/SSL), untuk memverifikasi identitas dan mencegah penyadapan aktif.  )

---

## 9. Commit Log
(
```
commit 1e087c81177854034381283388419c88391f74cf
Author: Raffly Ardya Putra <rafflyardya.09@gmail.com>
Date:   2025-11-22

    week7-diffie-hellman: Diffie-Hellman Key Exchange )
```
