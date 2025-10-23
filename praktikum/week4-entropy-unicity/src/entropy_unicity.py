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

print("\n"+"="*50)