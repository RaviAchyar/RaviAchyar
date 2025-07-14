from transaksi import input_pelanggan, cek_transaksi, hapus_transaksi, antrian, riwayat_transaksi

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