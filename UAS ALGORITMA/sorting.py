class BubbleSort:
    def sort(self, data):
        n = len(data)
        for i in range(n-1):
            for j in range(n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
            print(f"Iterasi ke-{i+1}: {data}")

class SelectionSort:
    def sort(self, data):
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            print(f"Iterasi ke-{i+1}: {data}")

class InsertionSort:
    def sort(self, data):
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >=0 and data[j] > key:
                data[j+1] = data[j]
                j -=1
            data[j+1] = key
            print(f"Iterasi ke-{i}: {data}")

class ShellSort:
    def sort(self, data):
        n = len(data)
        gap = n // 2
        iterasi = 1
        while gap > 0:
            for i in range(gap, n):
                temp = data[i]
                j = i
                while j >= gap and data[j - gap] > temp:
                    data[j] = data[j - gap]
                    j -= gap
                data[j] = temp
            print(f"Iterasi ke-{iterasi}: {data} (gap={gap})")
            gap //= 2
            iterasi += 1