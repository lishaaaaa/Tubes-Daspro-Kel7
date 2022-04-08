# Fungsi yang mengubah data sebuah game pada csv
from validasiGame import *

def ubahGame(listOfGames):   # menerima sebuah csv game dan mengganti kandungannya #TODO
    # untuk sementara menggunakan array
    ID = input("Masukkan ID game: ")
    found = False
    index = 0
    for i in range(lengthFinder(listOfGames)):
        if listOfGames[i][0] == ID:
            found = True
            validGame = False       # proses while untuk memvalidasi elemen game
            while not validGame:    # validasi elemen-elemen game benar atau tidak
                tempName = input("Masukkan nama game: ")
                if tempName != "":
                    tempVal1 = isValidName(tempName)
                else:
                    tempVal1 = True
                    tempName = listOfGames[i][1]

                tempKategori = input("Masukkan kategori game: ")
                if tempKategori != "":
                    tempVal2 = isValidKategori(tempKategori)
                else:
                    tempVal2 = True
                    tempKategori = listOfGames[i][2]

                tempTahun = input("Masukkan tahun rilis game: ")
                if tempTahun != "":
                    tempVal3 = isValidTahun(tempTahun)
                else:
                    tempVal3 = True
                    tempTahun = listOfGames[i][3]

                tempHarga = input("Masukkan harga game: ")
                if tempHarga != "":
                    tempVal4 = isValidHarga(tempHarga)
                else:
                    tempVal4 = True
                    tempHarga = listOfGames[i][4]

                if tempVal4 and tempVal3 and tempVal2 and tempVal1:
                    validGame = True    #bila semua elemen sudah sesuai program lanjut ke editing

            listOfGames[i][1] = tempName
            listOfGames[i][2] = tempKategori
            listOfGames[i][3] = tempTahun
            listOfGames[i][4] = tempHarga
            index = i
            break
    if not found:
        print("Maaf ID game tidak ditemukan")
    else:
        print("Game berhasil diperbarui, berikut info terbarunya:  ")
        print(listOfGames[index])




sample_games = [["X" for i in range(5)]for j in range(5)]     # array yg dipake untuk testing sblm punya csv file
sample_games[0][0] = "ID Game"
sample_games[0][1] = "Judul Game"
sample_games[0][2] = "Kategori"
sample_games[0][3] = "Tahun Rilis"
sample_games[0][4] = "Harga"


sample_games[1][0] = "GAME001"
sample_games[1][1] = "Valorant"
sample_games[1][2] = "FPS"
sample_games[1][3] = "2020"
sample_games[1][4] = "10000"


ubahGame(sample_games)
