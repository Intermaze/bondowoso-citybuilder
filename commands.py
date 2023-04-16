from data import *
import random

#Cara utama menambahkan array ke data
#Akan menambahkan Neff data (data[0]) dengan 1
def combine_arr_to_data(data, arr):

    data[0] += 1 
    n1 = data[0]
    
    #N1 adalah panjang array (Neff)
    matrix_out = [0 for i in range(n1+1)]

    for i in range(n1):
        matrix_out[i] = data[i]
    matrix_out[n1] = arr

    return matrix_out

def run(fungsi):
    if fungsi == "login":
        login()
    if fungsi == "logout":
        logout()
    if fungsi == "summonjin":
        summonjin()
    if fungsi == "bangun":
        bangun ()
    if fungsi == "kumpul":
        kumpul ()
    if fungsi == "ubahjin":
        ubahjin()
    if fungsi == "batchkumpul":
        batchkumpul ()
    if fungsi == "batchbangun":
        batchbangun ()        

#f01
def login():
    username = input("Username: ")
    password = input("Password: ")

    username_terdaftar = False
    password_benar = False
    for i in range(1, users[0]+1):
        if username == users[i][0]:
            username_terdaftar = True
            if password == users[i][1]:
                password_benar = True
    
    global nama_user #Akses nama_user sebagai variabel global; nama_user yang diubah pada fungsi ini dapat diakses oleh fungsi lain
    
    if nama_user != '':
        print("Login gagal!")
        print(f"Anda telah login dengan username {nama_user}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    elif username_terdaftar and password_benar:
        nama_user = username
        print(f"Selamat datang, {nama_user}!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
    elif not(username_terdaftar):
        print("Username tidak terdaftar!")
    else:
        print("Password salah!")


#f02
def logout():
    global nama_user #Akses nama_user sebagai variabel global
    if nama_user != '' :
        nama_user= '' #ngosongin identitas login yang dibuat di login, agar aksesnya hilang dan harus login kembali
        print('Logout berhasil!')
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

#f03
def summonjin():
    if nama_user == "Bondowoso":
        global jin #Akses jin sebagai variabel global

        while True:
            nomor_jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            if nomor_jenis_jin == 1 or nomor_jenis_jin == 2:
                break
            print(f'Tidak ada jenis jin bernomor "{nomor_jenis_jin}"!')

        if nomor_jenis_jin == 1 :
            jenis_jin = 'Pengumpul'
        else:
            jenis_jin = 'Pembangun'

        while True:
            username_jin = input('Masukkan username jin: ')
            if jin[0] == 0: #Jika belum ada jin, langsung lanjut ke tahap berikutnya
                break
            else:
                username_jin_sudah_diambil = False
                for i in range(1,jin[0]+1): #disini ngecek setiap indeks user apakah ada yang sama atau nggak
                    if username_jin == jin[i][0]:
                        username_jin_sudah_diambil = True
            
            if username_jin_sudah_diambil:
                print(f'Username “{username_jin}” sudah diambil!')
            else:
                break

        while True:
            password_jin = input('Masukkan password jin: ')
            if 4<=len(password_jin)<=25 :
                break
            print('Password panjangnya harus 5-25 karakter!')
        
        arrTemp = [username_jin, password_jin, jenis_jin]

        jin = combine_arr_to_data(jin, arrTemp)
        print(jin)

def tipe_lain_jin(tipejin):
    if tipejin == "Pembangun":
        return "Pengumpul"
    else:
        return "Pembangun"

#f05
def ubahjin():
    global jin
    user_jin = input("Masukkan username jin: ")
    jin_found = False

    for i in range(1, jin[0]+1):
        if jin[i][0] == user_jin:
            jin_found = True
            konfirmasi = input(f"Jin ini bertipe “{jin[i][2]}”. Yakin ingin mengubah ke tipe “{tipe_lain_jin(jin[i][2])}” (Y/N)? ")

            while True: #Mengulangi input sampai user memilih "Y" atau "N"
                if konfirmasi == "Y":
                    jin[i][2] == tipe_lain_jin(jin[i][2])
                    print("Jin telah berhasil diubah.")
                    break
                if konfirmasi == "N":
                    break
                konfirmasi = input(f"Jin ini bertipe “{jin[i][2]}”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
            break
    
    if jin_found == False:
        print("Tidak ada jin dengan username tersebut.")

#f06 
def bangun ():
    global jin
    global candi
    #Mencari apakah ada jin pembangun
    jin_pembangun = 0
    for i in range (1,jin[0]+1):
        if jin[i][2] == "Pembangun":
            jin_pembangun += 1

    #Jin kurang dari 1
    if jin_pembangun < 1 :
        print ("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

    else :
        perlu_pasir = random.randint(1, 5)
        perlu_batu = random.randint(1, 5)
        perlu_air = random.randint(1, 5)

        #Bahan memenuhi
        if int(bahan_bangunan[1][2]) >= perlu_pasir and int(bahan_bangunan[2][2]) >= perlu_batu and int(bahan_bangunan[3][2]) >= perlu_air :
            bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - perlu_pasir
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - perlu_batu
            bahan_bangunan[3][2] = int(bahan_bangunan[3][2]) - perlu_air
            
            #Cari indeks candi kosong
            if candi [0] == 0:
                id_terakhir = 1
            else:
                for i in range (candi[0], 0, -1):
                    if candi[i][0] != "":
                        id_terakhir = i+1
                        break
            
            arrTemp = [id_terakhir, nama_user, perlu_pasir, perlu_batu, perlu_air]

            candi = combine_arr_to_data(candi, arrTemp)

            print ("Candi berhasil dibangun.")
            print (f"Sisa candi yang perlu dibangun: {100-(id_terakhir)}.")
            print (candi)

        #Bahan tidak memenuhi
        else :
            print ("Bahan bangunan tidak mencukupi.")
            print ("Candi tidak bisa dibangun!")
               
#f07
def kumpul ():
    global jin
    #Mencari apakah ada jin pengumpul
    jin_pengumpul = 0
    for i in range (1,jin[0]+1):
        if jin[i][2] == "Pengumpul":
            jin_pengumpul += 1

    if jin_pengumpul < 1 :
        print ("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    
    else :
        dapet_pasir = random.randint(0, 5)
        dapet_batu = random.randint(0, 5)
        dapet_air = random.randint(0, 5)

        bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) + dapet_pasir
        bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) + dapet_batu
        bahan_bangunan[3][2] = int(bahan_bangunan[3][2]) + dapet_air

        print (f"Jin menemukan {dapet_pasir} pasir, {dapet_batu} batu, dan {dapet_air} air.")

#f08
def batchkumpul ():
    global jin
    #Mencari berapa banyak jin pengumpul
    jin_pengumpul = 0
    for i in range (1,jin[0]+1):
        if jin[i][2] == "Pengumpul":
            jin_pengumpul += 1

    if jin_pengumpul < 1 :
        print ("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

    else:
        #Declare bahan bangunan yang didapat
        total_pasir = 0
        total_batu = 0
        total_air = 0

        for i in range (jin_pengumpul):
            dapet_pasir = random.randint(0, 5)
            dapet_batu = random.randint(0, 5)
            dapet_air = random.randint(0, 5)
            total_pasir += dapet_pasir
            total_batu += dapet_batu
            total_air += dapet_air

        bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) + total_pasir
        bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) + total_batu
        bahan_bangunan[3][2] = int(bahan_bangunan[3][2]) + total_air

        print (f"Mengerahkan {jin_pengumpul} jin untuk mengumpulkan bahan.")
        print (f"Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")

def batchbangun ():
    global jin
    global candi
    #Mencari berapa banyak jin pembangun
    jin_pembangun = 0
    for i in range (1,jin[0]+1):
        if jin[i][2] == "Pembangun":
            jin_pembangun += 1

    #Jin kurang dari 1
    if jin_pembangun < 1 :
        print ("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

    else :
        total_pasir = 0
        total_batu = 0
        total_air = 0

        arrbahan_pasir = [0 for i in range (jin_pembangun)]
        arrbahan_batu = [0 for i in range (jin_pembangun)]
        arrbahan_air = [0 for i in range (jin_pembangun)]

        for i in range (jin_pembangun):
            arrbahan_pasir[i] = random.randint(1, 5)
            arrbahan_batu[i] = random.randint(1, 5)
            arrbahan_air[i] = random.randint(1, 5)
            total_pasir += arrbahan_pasir[i]
            total_batu += arrbahan_batu[i]
            total_air += arrbahan_air[i]

        #Bahan memenuhi
        if int(bahan_bangunan[1][2]) >= total_pasir and int(bahan_bangunan[2][2]) >= total_batu and int(bahan_bangunan[3][2]) >= total_air :
            bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - total_pasir
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - total_batu
            bahan_bangunan[3][2] = int(bahan_bangunan[3][2]) - total_air
            
            #Cari candi kosong
            for i in range (jin_pembangun):
                if candi [0] == 0:
                    id_terakhir = 1
                else:
                    for j in range (candi[0], 0, -1):
                        if candi[j][0] != "":
                            id_terakhir = i+1
                            break

                arrTemp = [id_terakhir, nama_user, arrbahan_pasir[i], arrbahan_batu[i], arrbahan_air[i]]

                candi = combine_arr_to_data(candi, arrTemp)

            print (f"Mengerahkan {jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
            print (f"Jin berhasil membangun total {jin_pembangun} candi.")
            print (candi)
    
        #Tidak cukup bahan
        else :
            #Mengubah jika salah satu bahan yang mencukupi agar tidak negatif
            if total_pasir-bahan_bangunan[1][2] < 0 :
                kurang_pasir = 0
            else :
                kurang_pasir = total_pasir-bahan_bangunan[1][2]
            if total_batu-bahan_bangunan[2][2] < 0 :
                kurang_batu = 0
            else :
                kurang_batu = total_batu-bahan_bangunan[2][2]         
            if total_air-bahan_bangunan[3][2] < 0 :
                kurang_air = 0
            else :
                kurang_air = total_air-bahan_bangunan[3][2]

            print (f"Mengerahkan {jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
            print (f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")