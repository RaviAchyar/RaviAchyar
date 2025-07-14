import array

angka = array.array('i', [10, 20, 30, 40, 50])

for i in range(len(angka)):
    print("Isi array indeks", i, "adalah", angka[i])
