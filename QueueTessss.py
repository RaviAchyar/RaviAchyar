# MRAVI ACHYAR TRISTA ZHAID
# 1124102193

import os

class Queue:
    def __init__(self): 
        self.items = []

    def IsEmpty(self):
        return len(self.items) == 0

    def Enqueue(self, item):
        self.items.append(item)

    def Dequeue(self):
        if not self.IsEmpty():
            return self.items.pop(0)
        return None

    def Size(self):
        return len(self.items)

def MainMenu():
    q = Queue()
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("| Menu Aplikasi Stack |")
        print("1. Input Object")
        print("2. Hapus Object")
        print("3. Cek Empty")
        print("4. Panjang Dari Queue")
        print("5. Keluar Aplikasi")
        print("========================")

        pilihan = input("Masukkan Pilihan: ")

        if pilihan == "1":
            obj = input("Objek yang ingin ditambahkan: ")
            q.Enqueue(obj)
            print(f"Objek '{obj}' telah ditambahkan ke Queue.")
        elif pilihan == "2":
            dequeued = q.Dequeue()
            if dequeued is not None:
                print(f"Objek '{dequeued}' dihapus dari Queue.")
            else:
                print("Queue kosong, tidak ada yang bisa dihapus.")
        elif pilihan == "3":
            print("Queue kosong." if q.IsEmpty() else "Queue tidak kosong.")
        elif pilihan == "4":
            print(f"Panjang dari Queue adalah: {q.Size()}")
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi Queue!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    MainMenu()
