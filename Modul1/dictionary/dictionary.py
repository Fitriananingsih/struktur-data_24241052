from datetime import date
from sqlite3 import Date


aku = {
    "nama": "Fitriana ningsih"
    "url:" "https://www.fsttundikma.id"
    }

#caracara membuat dicnitry

# contoh jika 1 item
nama_dict = {
    "key": "value"
}

# contoh jika lebih dari 1 item
nama_dict = {
    "key1": "value",
    "key2": "value",
    "key3": "value"
}

# membuat dictionary
dict = {
    "nama"      : "Fitriana ningsih",
    "NIM"      : 24241052,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : '_',
        "twiter"    : '_',
        "instagram" : "_"
    }
}

# mengakses dict menggunakan key
print("Nama Saya adalah %s" % dict['nama'])
print("Akun Github saya %s" % dict['sosmed']['Github'])

# cara lainnya dengan menggunakan .get
print("NIM Saya adalah %s" % dict.get('NIM'))

nama_dict['kunci'] = 'Nilai_baru'

# Definisi awal dictionary
date = {
    "status": True,
    "sosmed": {
        "instagram": "_"
    }
}

# Mengubah nilai item dictionary dengan key
date['status'] = False

# Cek hasil perubahan
print(date['status'])

# Mengubah nilai item dictionary dengan .update
date.update({"sosmed": {"instagram": "_"}})

# Cek hasil perubahan
print(date['sosmed']['instagram'])

# mengubah nilai item Dictionary

data = {
    "nama": "Fitriana",
    "status": True,
    "sosmed": {
        "instagram": "_"
    }
}

# Menghapus menggunakan perintah del
del data['status']
print(data)  # status hilang

# Menghapus item menggunakan pop()
data.pop("sosmed")
print(data)  # sosmed hilang

#Menambahkan item pada dictionary

# membuat dictionary
mahasiswa = {
    "name" : "Fitriana"
}

# menambahkan nim
mahasiswa.update({
    "nim" : "24241052"
})

# melihat hasilnya
print(mahasiswa)

# looping dictionary

# mencetak data pada dict secara berulang-ulang setiap key
for key in mahasiswa:
    print(key, mahasiswa[key])

# Atau:
for key, value in mahasiswa.items():
    print(f"{key}: {value}")