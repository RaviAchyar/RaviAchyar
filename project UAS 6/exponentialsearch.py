class ExponentialSearch:
    def recursive_binary_search(self, data, target, left, right):
        if left > right:
            print("Data tidak ditemukan.")
            return -1
        mid = (left + right) // 2
        print(f"Memeriksa index ke-{mid} (nilai: {data[mid]})...")
        if data[mid] == target:
            print(f"==> Data ditemukan pada index ke-{mid}")
            return mid
        elif data[mid] < target:
            return self.recursive_binary_search(data, target, mid+1, right)
        else:
            return self.recursive_binary_search(data, target, left, mid-1)

    def search(self, data, target):
        if len(data) == 0:
            print("Data tidak ditemukan (data kosong).")
            return -1
        if data[0] == target:
            print(f"==> Data ditemukan pada index ke-0")
            return 0
        index = 1
        while index < len(data) and data[index] <= target:
            print(f"Melompat ke index ke-{index} (nilai: {data[index]})")
            index *= 2
        print(f"Binary search di blok dari index {index//2} ke {min(index, len(data)-1)}")
        return self.recursive_binary_search(data, target, index//2, min(index, len(data)-1))
