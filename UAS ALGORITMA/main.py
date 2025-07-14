from dataarray import DataArray
from sorting import InsertionSort, SelectionSort, ShellSort, BubbleSort
from searching import LinearSearch, JumpSearch, RecursiveBinarySearch, ExponentialSearch

def main():
    while True:
        arr = DataArray()
        try:
            jumlah = int(input("Masukkan jumlah data array: "))
        except ValueError:
            print("Input harus angka! Dianggap 0.")
            jumlah = 0

        arr.generate_random_data(jumlah)
        print("\nData sebelum sorting:")
        arr.tampilkan()

        print("""\n| Menu Sorting |
1. Insertion Sort
2. Selection Sort
3. Shell Sort
4. Bubble Sort
=============================""")
        pilih_sort = input("Pilih algoritma sorting: ")
        data_copy = arr.data.copy()

        if pilih_sort == '1':
            print("\nProses Insertion Sort:")
            InsertionSort().sort(data_copy)
        elif pilih_sort == '2':
            print("\nProses Selection Sort:")
            SelectionSort().sort(data_copy)
        elif pilih_sort == '3':
            print("\nProses Shell Sort:")
            ShellSort().sort(data_copy)
        elif pilih_sort == '4':
            print("\nProses Bubble Sort:")
            BubbleSort().sort(data_copy)
        else:
            print("Pilihan tidak valid.")
            continue

        print("\nData setelah sorting:", data_copy)

        print("""\n| Menu Searching |
1. Linear Search
2. Jump Search
3. Recursive Binary Search
4. Exponential Search
=============================""")
        pilih_search = input("Pilih algoritma searching: ")
        try:
            target = int(input("Masukkan data yang ingin dicari: "))
        except ValueError:
            print("Input harus angka!")
            continue

        pos = -1
        if pilih_search == '1':
            pos = LinearSearch().search(data_copy, target)
        elif pilih_search == '2':
            pos = JumpSearch().search(data_copy, target)
        elif pilih_search == '3':
            pos = RecursiveBinarySearch().search(data_copy, target, 0, len(data_copy)-1)
        elif pilih_search == '4':
            pos = ExponentialSearch().search(data_copy, target)
        else:
            print("Pilihan tidak valid.")
            continue

        if pos != -1:
            print(f"Data ditemukan pada index ke-{pos}")
        else:
            print("Data tidak ditemukan.")

        ulang = input("\nKembali ke menu awal? (y/n): ").lower()
        if ulang != 'y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()
