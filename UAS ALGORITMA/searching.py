import math

class LinearSearch:
    def search(self, data, target):
        for i, v in enumerate(data):
            print(f"Memeriksa index ke-{i} (nilai: {v})...")
            if v == target:
                print(f"==> Data ditemukan pada index ke-{i}")
                return i
        print("Data tidak ditemukan.")
        return -1

class JumpSearch:
    def search(self, data, target):
        n = len(data)
        step = int(math.sqrt(n))
        prev = 0
        print(f"Step size: {step}")
        while prev < n and data[min(step, n)-1] < target:
            print(f"Melompat ke index ke-{min(step, n)-1} (nilai: {data[min(step, n)-1]})")
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                print("Data tidak ditemukan.")
                return -1
        print(f"Linear search di blok dari index {prev} ke {min(step, n)-1}")
        for i in range(prev, min(step, n)):
            print(f"Memeriksa index ke-{i} (nilai: {data[i]})...")
            if data[i] == target:
                print(f"==> Data ditemukan pada index ke-{i}")
                return i
        print("Data tidak ditemukan.")
        return -1

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

class ExponentialSearch:
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
        return RecursiveBinarySearch().search(data, target, index//2, min(index, len(data)-1))