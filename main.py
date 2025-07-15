data_belanja = {}
jumlah = int(input("Jumlah belanja: "))

for i in range(jumlah):
    print(f"\nNama customer ke-{i+1}:")
    nama_barang = input("NAMA BARANG: ")
    harga_satuan_barang = input("HARGA SATUAN BARANG: ")
    jumlah_QTY = input("JUMLAH QTY: ")
    
    daftar_belanja = []

    jumlah_barang = int(input("Masukkan jumlah barang: "))  
    for i in range(jumlah_barang):
        barang = input(f"  Nama barang ke-{i+1}: ")         
        jumlah = float(input(f"  harga untuk {barang}: "))        
        daftar_belanja.append((barang, jumlah))                     

    total_belanja = sum(jumlah for _, jumlah in daftar_belanja)
    jumlah_beli = jumlah_barang / jumlah_barang if jumlah_barang > 0 else 0

    data_belanja[jumlah] = {
        "nama barang": nama_barang,
        "harga satuan barang": harga_satuan_barang,
        "jumlah QTY": jumlah_QTY, 
        "jumlah beli": jumlah
    }

print("\nCari data mahasiswa")
cari = input("Masukkan")

if cari in data_belanja:
    mhs = data_belanja[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}, Rata rata nilai: {mhs['nilai rata rata']:.2f}")
    print("Daftar Nilai Mata Kuliah:")
    for barang, nilai in mhs['daftar_nilai']:
        print(f"  {barang}: {jumlah:.2f}")
else:
    print("Belanja tidak ditemukan.")

print("\nJumlah beli:")
for tanggal_belanja, info in data_belanja.items():
    print(f"nama barang: {tanggal_belanja} --> {info['harga satuan barang']} ({info['jumlah QTY']}), jumlah beli: {info['nilai barang']:.2f}")
    print("  Daftar Nilai Mata Kuliah:")
    for matkul, nilai in info['daftar_nilai']:
        print(f"    {matkul}: {nilai:.2f}")