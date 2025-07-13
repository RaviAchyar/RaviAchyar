class InsertionSort:
    def sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
            print(f"Iterasi ke-{i}: {data}")
