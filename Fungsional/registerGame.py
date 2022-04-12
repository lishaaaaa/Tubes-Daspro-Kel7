# Program Fungsi Register

# Program dapat mendaftarkan pengguna baru dengan memasukkan nama, username, dan password.
# Username harus unik (tidak bisa ada username yang sama)

# Catatan : 
# Belum memahami cara menyimpan data ke dalam csv

def register (role, user) :
    if (user [3]== "admin") :
        nama = input("Masukkan nama : ")
        username = input("Masukkan username : ")
        # username harus unik
        # inisialisasi i
        i = 0
        while (user[i] != " ") :
            cek_username = user [i]
            if (username == cek_username [2]) :
                print ("Username " + username + " sudah terpakai, silakan menggunakan username lain.")
                i = 0
                username = input("Masukkan nama : ")
            else :
                i += 1
        password = input("Masukkan password pemain : ")
        user [i] = [nama, username, password, "pemain"]
        print ("Username" + username + " telah berhasil register kedalam Binomo")
