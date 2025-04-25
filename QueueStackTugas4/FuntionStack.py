class Stack:
    def __init__(self):
        self.items = []
        
    def IsEmpty(self):
        return len(self.items) == 0
    
    def Push(self, item):
        self.items.append(item)
        
    def Pop(self):
        if not self.IsEmpty():
            return self.items.pop()
        return None
    
    def Peek(self):
        if not self.IsEmpty():
            return self.items[len(self.items) - 1]
        return None
    
    def Size(self):
        return len(self.items)

def MenuStack():
    s = Stack()
    pilih = "y"
    while (pilih == "y"):
        print("|Menu Aplikasi Stack|")
        print("1. Push Object")
        print("2. Pop Object")
        print("3. Cek Empty")
        print("4. Tampil Objek Terakhir")
        print("5. Panjang Dari Stack")
        print("=====================")
        
        pilihan = str(input("Masukkan pilihan: "))
        if pilihan == "1":
            obj = str(input("Objek yang ingin ditambahkan: "))
            s.Push(obj)
            print("Object " + obj + " telah ditambahkan")
        elif pilihan == "2":
            popped = s.Pop()
            if popped is not None:
                print("Object " + popped + " dihapus")
            else:
                print("Stack kosong, tidak ada yang bisa dihapus.")
        elif pilihan == "3":
            print(s.IsEmpty())
        elif pilihan == "4":
            last_item = s.Peek()
            if last_item is not None:
                print("Objek terakhir: " + last_item)
            else:
                print("Stack kosong, tidak ada objek terakhir.")
        else:
            print("Panjang dari Stack adalah: " + str(s.Size()))
