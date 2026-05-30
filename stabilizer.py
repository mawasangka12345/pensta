import socket
import time
import os
import urllib.request
from datetime import datetime

def ambil_waktu_internet():
    try:
        # Mengambil waktu akurat dari server Google (mencegah manipulasi jam HP)
        response = urllib.request.urlopen('https://www.google.com', timeout=3)
        waktu_server = response.headers['Date']
        # Mengubah format waktu server menjadi objek datetime
        waktu_lokal = datetime.strptime(waktu_server, '%a, %d %b %Y %H:%M:%S %Z')
        return waktu_lokal
    except Exception:
        # Jika tidak ada internet, kembalikan None
        return None

def UDP_Lifesaver():
    os.system('clear')
    print("==========================================")
    print("        HC UDP CUSTOM STABILIZER          ")
    print("         SALAM KENAL NAGABUTON            ")
    print("==========================================")
    print("[*] Memeriksa lisensi dan koneksi...")

    waktu_sekarang = ambil_waktu_internet()
    
    if waktu_sekarang is None:
        print("\n[!] Error: Butuh koneksi internet untuk cek lisensi!")
        print("KALAU ADA KESULITAN HUBUNGI NOMOR 085341608090")
        return

    # TENTUKAN TANGGAL EXPIRED DI SINI (Tahun, Bulan, Tanggal)
    expired_date = datetime(2026, 7, 31) 
    
    if waktu_sekarang > expired_date:
        print("\n==========================================")
        print("     MAAF, MASA AKTIF SCRIPT HABIS!       ")
        print("  KALAU ADA KESULITAN HUBUNGI NOMOR:      ")
        print("               085341608090               ")
        print("==========================================")
        return

    print("   Status: Pumping Real UDP Packets       ")
    print("   Masa Aktif: Terverifikasi (Aktif)      ")
    print("==========================================")

    # Target server DNS 
    target_ip = "1.1.1.1"
    target_port = 53
    data_packet = b"\x00\x00\x00\x00"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    counter = 1
    
    while True:
        try:
            sock.sendto(data_packet, (target_ip, target_port))
            print(f"[{counter}] Paket UDP berhasil dipompa ke {target_ip}:{target_port}")
            counter += 1
            time.sleep(1) 
        except KeyboardInterrupt:
            print("\n[!] Program dihentikan.")
            break
        except Exception as e:
            print(f"[!] Terjadi kesalahan: {e}")
            print("HUBUNGI NOMOR: 085341608090")
            break

if __name__ == "__main__":
    UDP_Lifesaver()
