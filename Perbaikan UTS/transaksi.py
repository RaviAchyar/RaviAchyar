from queue import Queue
from pelanggan import Pelanggan

antrian = Queue()
riwayat_transaksi = []

def input_pelanggan():
    nama = input("Masukkan nama pelanggan: ")
    daftar_belanja = []

    while True:
        barang = input("Masukkan nama barang: ").strip()
        try:
            harga = int(input(f"Masukkan harga untuk {barang}: "))
            daftar_belanja.append((barang, harga))
        except ValueError:
            print("Harga harus berupa angka!")
        break

    if daftar_belanja:
        antrian.put(Pelanggan(nama, daftar_belanja))
        print(f"\n{nama} telah selesai berbelanja. Menyimpan transaksi ke riwayat.")

def cek_transaksi():
    if riwayat_transaksi:
        print("\nRiwayat Transaksi:")
        for p in riwayat_transaksi:
            print(f"- {p.nama}: Rp{p.total_belanja():,}")
    else:
        print("  Belum ada transaksi yang dilakukan.")

def hapus_transaksi():
    if riwayat_transaksi:
        transaksi_hapus = riwayat_transaksi.pop(0)
        print(f"Transaksi untuk {transaksi_hapus.nama} telah dihapus.")
    else:
        print("Riwayat transaksi kosong.")