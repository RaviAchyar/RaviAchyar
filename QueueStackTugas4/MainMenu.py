from FuntionStack import MenuStack
from FuntionQueue import MenuQueue

def MainMenu():
    while True:
        print("1. Operasi Stack")
        print("2. Operasi Queue")
        print("3. Keluar Aplikasi")
        print("============================")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            MenuStack()
        elif pilihan == "2":
            MenuQueue()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    MainMenu()
