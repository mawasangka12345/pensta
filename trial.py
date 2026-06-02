import sys

# =========================================================
# 1. DATABASE AKSES (Edit/Hapus Nama di Sini)
# =========================================================
DAFTAR_MEMBER = {
    "uton": "admin123",        # Masih aktif
    "teman1": "coba_doang",    # Masih aktif
    "asep": "kunci88",         # Masih aktif
    "nagabuton": "premium2026" # Akun owner
}

def jalankan_keamanan():
    print("================================")
    print("   LOGIN SYSTEM NAGABUTON       ")
    print("   (MANUAL ACCESS CONTROL)      ")
    print("================================")
    
    # Input dari pengguna
    user = input("[?] Username : ").strip().lower()
    pw   = input("[?] Password : ").strip()

    # Cek apakah Username ada di daftar dan Passwordnya cocok
    if user in DAFTAR_MEMBER and DAFTAR_MEMBER[user] == pw:
        print(f"\n[+] Akses Diterima! Selamat datang, {user.upper()}.")
        print("[+] Script Aktif (Tanpa Batas Waktu).")
        print("==========================================\n")
    else:
        print("\n[!] USERNAME ATAU PASSWORD SALAH / DIBLOKIR!")
        print("[!] Hubungi Nagabuton untuk akses.")
        sys.exit()

# Jalankan sistem keamanan
jalankan_keamanan()

# =========================================================
# 2. SCRIPT UTAMA (UDP STABILIZER)
# =========================================================
print(">>> SCRIPT STABILIZER UDP SEDANG AKTIF...")

import socket
import time

target_ip = "1.1.1.1"
target_port = 53
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = b"\x00\x00\x00\x00"

while True:
    try:
        sock.sendto(packet, (target_ip, target_port))
        print(f"[*] Mengirim paket stabil ke {target_ip}...")
        time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Berhenti.")
        break
