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
            print(f"Iterasi ke-{iterasi} (gap={gap}): {data}")
            iterasi += 1
            gap //= 2
