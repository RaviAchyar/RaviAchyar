from queue import Queue

class Pelanggan:
    def __init__(self, nama, daftar_belanja):
        self.nama = nama
        self.daftar_belanja = daftar_belanja

    def total_belanja(self):
        return sum(harga for _, harga in self.daftar_belanja)

    def tampilkan_belanja(self):
        print(f"\nDaftar belanja {self.nama}:")
        for barang, harga in self.daftar_belanja:
            print(f"  - {barang}: Rp{harga:,}")
        print(f"Total: Rp{self.total_belanja():,}")

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

def menu():
    while True:
        print("\nMenu:")
        print("1. Input Pelanggan")
        print("2. Cek Riwayat Transaksi")
        print("3. Hapus Transaksi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ").strip()

        if pilihan == "1":
            input_pelanggan()
            while not antrian.empty():
                pelanggan = antrian.get()
                riwayat_transaksi.append(pelanggan)
        elif pilihan == "2":
            cek_transaksi()
        elif pilihan == "3":
            hapus_transaksi()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan 1, 2, 3, atau 4.")

menu()
