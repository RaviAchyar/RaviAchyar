class LinearSearch:
    def search(self, data, target):
        for i, v in enumerate(data):
            print(f"Memeriksa index ke-{i} (nilai: {v})...")
            if v == target:
                print(f"==> Data ditemukan pada index ke-{i}")
                return i
        print("Data tidak ditemukan.")
        return -1
