import random

class DataArray:
    def __init__(self):
        self.data = []

    def generate_random_data(self, jumlah, min_val=1, max_val=20):
        self.data = [random.randint(min_val, max_val) for _ in range(jumlah)]

    def tampilkan(self):
        print("Data array:", self.data)
