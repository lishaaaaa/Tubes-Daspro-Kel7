def register (user):
    def panjang (obj):
        n = 0
        for elm in obj:
            n += 1
        return n

    name = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    data = ["" for i in range(6)]
    valid = True
    stop = False
    i = 0
    while (i < (panjang(user)-2)) and (valid == True) and (stop == False):
        if (user[i][1] == username):
            valid = False
        elif (user[i][1] == ""):
            stop = True
        i += 1
    
    if valid == False:
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
    else:
        if (i < 9):
            data[0] = f"ID00{i+1}"
        elif (i < 99):
            data[0] = f"ID0{i+1}"
        data[1] = username
        data[2] = name
        data[3] = password
        data[4] = "User"
        data[5] = "0"
        print(f'''Username {username} telah berhasil register ke dalam "Binomo".''')

user = [["" for i in range(6)] for j in range(5)]
register(user)