from queue import Queue

def QueueMenu():
    q = Queue()
    while True:
        print("\n| Menu Aplikasi Queue |")
        print("1. Input Object")
        print("2. Hapus Object")
        print("3. Cek Empty")
        print("4. Panjang Dari Queue")
        print("5. Kembali ke Menu Utama")
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
            break
        else:
            print("Pilihan tidak valid.")
