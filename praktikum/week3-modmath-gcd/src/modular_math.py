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
        
    print("\n=== Eksekusi Selesai ===")