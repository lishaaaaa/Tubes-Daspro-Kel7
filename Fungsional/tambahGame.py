from validasiGame import *

nama_game = input("Masukka nama game: ")
kategori_game = input("Masukkan kategori game: ")
tahun_game = input("Masukkan tahun rilis game: ")
harga_game = input("Masukkan harga game: ")
stok_game = input("Masukkan stok awal: ")

validGame = False
while not validGame:    # Selama ada kolom yang tidak valid maka proses akan diulang sampai semuanya valid
    if isValidStok(stok_game) and isValidHarga(harga_game) and isValidKategori(kategori_game) and isValidName(nama_game) and isValidTahun(tahun_game):
        validGame = True
    else:
        print("Mohon isi data game dengan sesuai")
        nama_game = input("Masukka nama game: ")
        kategori_game = input("Masukkan kategori game: ")
        tahun_game = input("Masukkan tahun rilis game: ")
        harga_game = input("Masukkan harga game")
        stok_game = input("Masukkan stok awal: ")

# Bagian yang menambahkan game ke csv #TODO
# menambahkan ID GAMEXXX ke csv
print(f"Selamat! Berhasil menambahkan game {nama_game}")

