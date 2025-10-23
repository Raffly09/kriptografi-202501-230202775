import math

# --- 1. Fungsi Entropi Kunci ---
def key_entropy_bits(size_of_keyspace):
    """Menghitung entropi (H) dalam bit dari ruang kunci."""
    return math.log2(size_of_keyspace)

# Pengujian Entropi
keyspace_caesar = 26
keyspace_aes128 = 2**128

entropy_caesar = key_entropy_bits(keyspace_caesar)
entropy_aes = key_entropy_bits(keyspace_aes128)

print(f"Entropi Ruang Kunci 26 (Caesar) = {entropy_caesar:.3f} bit")
print(f"Entropi Ruang Kunci 2^128 (AES-128) = {entropy_aes:.3f} bit")

# --- 2. Fungsi Jarak Unik (Unicity Distance) ---
def calculate_unicity_distance(H_key, redundancy_rate=0.75, alphabet_size=26):
    """Menghitung Jarak Unik (N0) berdasarkan entropi kunci (HK) dan redundansi bahasa (R)."""
    # H_per_char = R * log2(A)
    H_per_char = redundancy_rate * math.log2(alphabet_size)
    
    # N0 = HK / H_per_char
    return H_key / H_per_char

# Pengujian Unicity Distance (Caesar Cipher)
# Redundancy Rate (R) untuk bahasa Inggris sekitar 0.75
# Ukuran Alfabet (A) untuk bahasa Inggris = 26
N0_caesar = calculate_unicity_distance(H_key=entropy_caesar)

print(f"Jarak Unik (N0) untuk Caesar Cipher = {N0_caesar:.3f} karakter")

# --- 3. Fungsi Waktu Brute Force ---
def estimated_bruteforce_duration(keyspace_size, ops_per_second=1_000_000):
    """Mengestimasi waktu yang dibutuhkan untuk brute force (dalam hari)."""
    
    total_seconds = keyspace_size / ops_per_second
    seconds_in_day = 3600 * 24
    
    return total_seconds / seconds_in_day

# Pengujian Waktu Brute Force
BF_time_caesar = estimated_bruteforce_duration(keyspace_caesar)
BF_time_aes = estimated_bruteforce_duration(keyspace_aes128)

print(f"Waktu Brute Force Caesar Cipher (26 kunci) = {BF_time_caesar:.10f} hari")
print(f"Waktu Brute Force AES-128 = {BF_time_aes:.2f} hari")