from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta
import os

def generate_self_signed_cert():
    print("--- Memulai Pembuatan Key Pair RSA ---")
    # 1. Generate Private Key
    # Public exponent 65537 adalah standar industri
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    print("[OK] Private Key generated (2048-bit).")

    # 2. Membuat Identitas (Subject & Issuer sama karena Self-Signed)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Jawa Tengah"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Kebumen"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Universitas Putra Bangsa"),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, u"Lab Kriptografi"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"pki-demo.local"),
    ])
    print("[OK] Identitas Subject & Issuer dikonfigurasi.")

    # 3. Membangun Sertifikat
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow())
        .not_valid_after(datetime.utcnow() + timedelta(days=365)) # Berlaku 1 tahun
        .add_extension(
            x509.BasicConstraints(ca=True, path_length=None), critical=True,
        )
        .sign(key, hashes.SHA256())
    )
    print("[OK] Sertifikat berhasil ditandatangani (SHA256).")

    # 4. Menyimpan Sertifikat ke File
    cert_filename = "server_cert.pem"
    key_filename = "server_key.pem"

    # Simpan Sertifikat Publik
    with open(cert_filename, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    
    # Simpan Private Key (PENTING: Jangan disebar di produksi)
    with open(key_filename, "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    print(f"\n--- Hasil ---")
    print(f"Sertifikat disimpan di: {os.path.abspath(cert_filename)}")
    print(f"Private Key disimpan di: {os.path.abspath(key_filename)}")
    print(f"Serial Number: {cert.serial_number}")
    print("Selesai.")

if __name__ == "__main__":
    generate_self_signed_cert()