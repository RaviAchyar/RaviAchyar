class BubbleSort:
    def sort(self, data):
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
            print(f"Iterasi ke-{i+1}: {data}")
