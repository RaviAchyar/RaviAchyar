import os

class Stack:
    def _init_(self):
        self.items = [];
        
    def IsEmpty(self):
        return len(self.items) == 0;
    
    def Push(self, item):
        self.items.append(item);
        
    def Pop(self):
        return self.items.pop();
    
    def Peek(self):
        return self.items[len(self.items)-1];
    
    def Size(self):
        return len(self.items);
    
def MainMenu():
    s = Stack();
    pilih = "y";
    while (pilih == "y"):
        print("|Menu Aplikasi Strak|");
        print("1. Push Object");
        print("2. Pop Object");
        print("3. Cek Empty");
        print("4. Tampil Objek Terakhir");
        print("5. Panjang Dari Stack");
        print("=====================");
        
        pilihan = str(input("Masukkan pilihan: "));
        if pilihan == "1":
            print("Hallo");
            obj = str(input("Objek yang ingin ditambahkan: "));
            s.Push(obj);
            print("Object " + obj + " telah ditambahkan");
        elif pilihan =="2":
            print("Object " + s.Pop() + " dihapus");
        elif pilihan == "3":
            print(s.IsEmpty());
        elif pilihan == "4":
            print("Objek terakhir: " + s.Peek());
        else:
            print("Panjang dari Stack adalah: "+ str(s.Size()));
            
if __name__ == "__main__":
    MainMenu();