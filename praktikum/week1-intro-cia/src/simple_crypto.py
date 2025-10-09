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
print("Hasil Dekripsi :", teks_didekripsi)