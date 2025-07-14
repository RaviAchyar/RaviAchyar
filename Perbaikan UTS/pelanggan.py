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