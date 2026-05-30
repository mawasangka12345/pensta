import datetime
import sys

# =========================================================
# 1. DATABASE AKSES (Isi Nama Teman & Password di Sini)
# =========================================================
DAFTAR_MEMBER = {
    "uton": "admin123",        # Nama: uton, Pass: admin123
    "teman1": "coba_doang",    # Nama: teman1, Pass: coba_doang
    "asep": "kunci88"          # Nama: asep, Pass: kunci88
}

# =========================================================
# 2. PENGATURAN MASA AKTIF (Tahun, Bulan, Tanggal)
# =========================================================
TANGGAL_EXPIRED = datetime.date(2026, 6, 10) 

def jalankan_keamanan():
    print("=== LOGIN SYSTEM NAGABUTON ===")
    
    # Input dari pengguna
    user = input("[?] Masukkan Username : ").strip().lower()
    pw   = input("[?] Masukkan Password : ").strip()

    # Cek Username dan Password
    if user in DAFTAR_MEMBER and DAFTAR_MEMBER[user] == pw:
        
        # Cek Masa Aktif
        hari_ini = datetime.date.today()
        sisa_hari = (TANGGAL_EXPIRED - hari_ini).days
        
        if sisa_hari < 0:
            print("\n[-] MAAF, MASA AKTIF SCRIPT SUDAH HABIS!")
            print(f"[-] Expired pada: {TANGGAL_EXPIRED}")
            sys.exit()
        else:
            print(f"\n[+] Akses Diterima! Halo {user}.")
            print(f"[+] Sisa Masa Aktif: {sisa_hari} hari lagi.\n")
            print("------------------------------------------")
    else:
        print("\n[!] USERNAME ATAU PASSWORD SALAH!")
        print("[!] Hubungi Nagabuton untuk beli lisensi.")
        sys.exit()

# Jalankan fungsi keamanan
jalankan_keamanan()

# =========================================================
# 3. TARUH SCRIPT ASLI KAMU (STABILIZER/UDP) DI BAWAH INI
# =========================================================
print(">>> SCRIPT UTAMA SEDANG BERJALAN...")
# Contoh: 
# os.system('python stabilizer.py') 
