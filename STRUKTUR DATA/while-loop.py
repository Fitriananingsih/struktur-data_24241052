angka = 0
while angka < 3: # kondisi
    angka += 1 # aksi 1
    print("*" * angka) # aksi 2

    angka = 0 
while angka < 3: 
    print ("*" * angka)
    angka += 1

angka = 0 
while angka < 3:
    angka += 1
    print ("*" * angka)

rows = 3
for i in range(rows):
    space = rows - i - 1
    stars = 2 * i + 1
    print(" " * space + "*" * stars)