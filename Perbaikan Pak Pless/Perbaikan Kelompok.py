class BinaryRecursiveSearch:

    def __init__(self, data):
        self.data = sorted(data)

    def search(self, item, low=None, high=None):
        if low is None:
            low = 0
        if high is None:
            high = len(self.data) - 1

        print(f"Mencari {item} di antara index {low} dan {high}")

        if low <= high:
            middle = (low + high) // 2
            print(f"Nilai tengah index: {middle}, data: {self.data[middle]}")

            if self.data[middle] == item:
                print(f"Ditemukan! {item} ada di index {middle}")
                return middle
            elif item < self.data[middle]:
                return self.search(item, low, middle - 1)
            else:
                return self.search(item, middle + 1, high)
        else:
            print(f"{item} tidak ditemukan dalam rentang ini.")
            return -1

    def __repr__(self):
        return f"BinaryRecursiveSearch(data={self.data})"


# Data manual 1-20
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Buat objek BinaryRecursiveSearch
brs = BinaryRecursiveSearch(data)

# Item yang akan dicari
item_to_search = 17

# Jalankan pencarian
index = brs.search(item_to_search)

# Cetak hasil akhir
if index != -1:
    print(f"\nHasil: Angka {item_to_search} ditemukan pada index {index}")
else:
    print(f"\nHasil: Angka {item_to_search} tidak ditemukan")
