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
    print("\n❌ Verifikasi Gagal! Ada kesalahan dalam perhitungan kunci.")