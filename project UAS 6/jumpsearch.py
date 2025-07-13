import math
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
