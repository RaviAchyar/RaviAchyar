class RecursiveBinarySearch:
    def search(self, data, target, left, right):
        if left > right:
            print("Data tidak ditemukan.")
            return -1
        mid = (left + right) // 2
        print(f"Memeriksa index ke-{mid} (nilai: {data[mid]})...")
        if data[mid] == target:
            print(f"==> Data ditemukan pada index ke-{mid}")
            return mid
        elif data[mid] < target:
            return self.search(data, target, mid+1, right)
        else:
            return self.search(data, target, left, mid-1)
