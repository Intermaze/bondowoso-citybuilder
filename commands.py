from data import *
from data_functions import csv_to_array #Digunakan dalam f13 load
from data_functions import array_to_csv #Digunakan dalam f14 save
import random
import os 
import argparse

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
    if fungsi == "debug":
        debug()
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
    if fungsi == "help":
        help ()
    if fungsi == "save":
        save ()
    if fungsi == "ayamberkokok":
        ayamberkokok ()
    if fungsi == "hapusjin":
        hapusjin ()         
    if fungsi == "hancurkancandi":
        hancurkancandi ()         
    if fungsi == "laporanjin":
        laporanjin ()
    if fungsi == "laporancandi":
        laporancandi ()
    if fungsi == "exit":
        exit ()

#f00 (Testing; lihat isi data)
def debug():
    print("nama_user:", nama_user)
    print("users:",users)
    print("candi:",candi)
    print("bahan_bangunan:",bahan_bangunan)

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
        global users #Akses users sebagai variabel global

        while True:
            nomor_jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil (1/2): "))
            if nomor_jenis_jin == 1 or nomor_jenis_jin == 2:
                break
            print(f'Tidak ada jenis jin bernomor "{nomor_jenis_jin}"!')

        if nomor_jenis_jin == 1 :
            jenis_jin = 'Pengumpul'
        else:
            jenis_jin = 'Pembangun'

        while True:
            username_jin = input('Masukkan username jin: ')
            if users[0] == 2: #Jika belum ada jin, langsung lanjut ke tahap berikutnya
                break

            username_jin_sudah_diambil = False
            for i in range(3,users[0]+1): #disini ngecek setiap indeks user jin apakah ada yang sama atau nggak
                if username_jin == users[i][0]:
                    username_jin_sudah_diambil = True            
            
            if username_jin_sudah_diambil == False:
                break

            print(f'Username “{username_jin}” sudah diambil!')

        while True:
            password_jin = input('Masukkan password jin: ')
            if 4<len(password_jin)<=25 :
                break
            print('Password panjangnya harus 5-25 karakter!')
        
        arrTemp = [username_jin, password_jin, jenis_jin]

        users = combine_arr_to_data(users, arrTemp)

def tipe_lain_jin(tipejin):
    if tipejin == "Pembangun":
        return "Pengumpul"
    else:
        return "Pembangun"

def hapusLineArray(nama_array, jumlah_kolom_array, index_line_array): #fungsi mengubah isi satu line pada array menjadi none
    global users
    global candi
    global bahan_bangunan
    for i in range (jumlah_kolom_array): #jumlah kolom pada array hitung mulai dari 1
        nama_array[index_line_array][i] = None

#f04
def hapusjin ():
    global users
    global candi

    #inisiasi awal dan input
    username_jin = str(input('Masukkan username jin : '))
    index_jin = -1 #-1 artinya tidak terdaftar

    #mengecek apakah username jin terdaftar
    for i in range(3,users[0]+1): #disini ngecek setiap indeks user jin apakah ada yang sama atau nggak
        if username_jin == users[i][0]:
            index_jin = i

    tipeJin_Temp = users[index_jin][2] #tipe jin yang ingin dihapus

    if index_jin != -1 : #apabila jin terdaftar
        while True : #memastikan input konfirmasi benar
            confirm = str(input(f'Apakah anda yakin ingin menghapus jin dengan username {username_jin} (Y/N)? '))
            if confirm == 'Y' or confirm == 'N':
                break

        if confirm == 'Y': #menghapus jin yang dipilih
            if tipeJin_Temp == 'Pembangun': 
                for i in range (1,candi[0]+1):
                    if username_jin == candi[i][1]:
                        hapusLineArray(candi, 5, i)
            hapusLineArray(users, 3, index_jin)
            return print('Jin telah berhasil dihapus dari alam gaib.')
        
        else: #tidak jadi menghapus jin yang terdaftar
            return print('Jin tidak jadi dihapus dari alam gaib')
        
    else: #jin tidak terdaftar
        return print('Tidak ada jin dengan username tersebut.')


#f05
def ubahjin():
    global users
    user_jin = input("Masukkan username jin: ")
    jin_found = False

    for i in range(3, users[0]+1):
        if users[i][0] == user_jin:
            jin_found = True
            konfirmasi = input(f"Jin ini bertipe “{users[i][2]}”. Yakin ingin mengubah ke tipe “{tipe_lain_jin(users[i][2])}” (Y/N)? ")

            while True: #Mengulangi input sampai user memilih "Y" atau "N"
                if konfirmasi == "Y":
                    users[i][2] = tipe_lain_jin(users[i][2])
                    print("Jin telah berhasil diubah.")
                    break
                if konfirmasi == "N":
                    break
                konfirmasi = input(f"Jin ini bertipe “{users[i][2]}”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
            break
    
    if jin_found == False:
        print("Tidak ada jin dengan username tersebut.")

#f06 
def bangun ():
    global users
    global candi
    #Mencari apakah yang login jin adalah jin pembangun
    for i in range (3,users[0]+1):
        if users[i][0] == nama_user :
            if users[i][2] == "Pembangun" :
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

            else :
                print ("bangun hanya bisa diakses oleh jin pembangun")
               
#f07
def kumpul ():
    global users
    #Mencari apakah yang login jin pembangun jin pengumpul
    for i in range (3,users[0]+1):
        if users[i][0] == nama_user :
            if users[i][2] == "Pengumpul" :
                dapet_pasir = random.randint(0, 5)
                dapet_batu = random.randint(0, 5)
                dapet_air = random.randint(0, 5)

                bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) + dapet_pasir
                bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) + dapet_batu
                bahan_bangunan[3][2] = int(bahan_bangunan[3][2]) + dapet_air

                print (f"Jin menemukan {dapet_pasir} pasir, {dapet_batu} batu, dan {dapet_air} air.")
            
            else:
                print ("kumpul hanya bisa diakses oleh jin pengumpul")

#f08
def batchkumpul ():
    global users
    #Apakah Bandung Bondowoso yang login
    if nama_user != "Bondowoso" :
        print ("batchkumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
    
    else :
        #Mencari berapa banyak jin pengumpul
        jin_pengumpul = 0
        for i in range (3,users[0]+1):
            if users[i][2] == "Pengumpul":
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
    global users
    global candi
    #Apakah Bandung Bondowoso yang login
    if nama_user != "Bondowoso" :
        print ("batchbangun hanya dapat diakses oleh akun Bandung Bondowoso.")

    else :
        #Mencari berapa banyak jin pembangun
        jin_pembangun = 0
        for i in range (3,users[0]+1):
            if users[i][2] == "Pembangun":
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
                indeks_jin_pembangun = 3 #Untuk mengecek setiap jin pembangun yang akan dicatat, mulai dari indeks jin(3)
                for i in range (jin_pembangun):
                    if candi [0] == 0:
                        id_terakhir = 1
                    else:
                        for j in range (candi[0], 0, -1):
                            if candi[j][0] != "":
                                id_terakhir = j+1
                                break
                    
                    #Mengecek jin pembangun agar bisa dimasukkan ke data candi
                    while users[indeks_jin_pembangun][2] != "Pembangun": 
                        indeks_jin_pembangun = indeks_jin_pembangun+1
                    
                    jin_yang_bangun = users[indeks_jin_pembangun][0]

                    #Setelah mendapat jin, akan melanjutkan ke indeks berikutnya agar tidak mengulang ke jin yang sama
                    indeks_jin_pembangun = indeks_jin_pembangun+1

                    arrTemp = [id_terakhir, jin_yang_bangun, arrbahan_pasir[i], arrbahan_batu[i], arrbahan_air[i]]

                    candi = combine_arr_to_data(candi, arrTemp)

                print (f"Mengerahkan {jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
                print (f"Jin berhasil membangun total {jin_pembangun} candi.")
        
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

#f09
def laporanjin ():
    global users
    if nama_user != "Bondowoso" :
        print ("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")

    else :
        total_jin = 0
        jin_pengumpul = 0
        jin_pembangun = 0
        candijin_terajin = -1
        candijin_termalas = 1000
        jin_terajin = "-"
        jin_termalas = "-"

        for i in range (3,users[0]+1):
            #Mengantisipasi indeks kosong
            if users[i][0] != None:
                total_jin += 1
                if users[i][2] == "Pengumpul":
                    jin_pengumpul += 1
                else :
                    jin_pembangun += 1
                
                total_candibuat = 0
                for j in range (1,candi[0]+1):
                    if users[i][2] == "Pembangun":
                        if users[i][0] == candi[j][1]:
                            total_candibuat += 1

                #Termalas/Terajin
                if users[i][2] == "Pembangun": #Jin pengumpul tidak ikut dalam perhitungan
                    if (candijin_terajin <= total_candibuat):
                        if (candijin_terajin == total_candibuat):
                            if ((jin_terajin > users[i][0]) == True):
                                jin_terajin = users[i][0]
                            else:
                                jin_terajin = jin_terajin
                        else :
                            candijin_terajin = total_candibuat
                            jin_terajin = users[i][0]
                    if (candijin_termalas >= total_candibuat):
                        if (candijin_termalas == total_candibuat):
                            if ((jin_termalas < users[i][0]) == True):
                                jin_termalas = users[i][0]
                            else:
                                jin_termalas = jin_termalas
                        else :
                            candijin_termalas = total_candibuat
                            jin_termalas = users[i][0]

        print (f"Total Jin: {total_jin}")
        print (f"Total Jin Pengumpul: {jin_pengumpul}")
        print (f"Total Jin Pembangun: {jin_pembangun}")   
        print (f"Jin Terajin: {jin_terajin}")
        print (f"Jin Termalas: {jin_termalas}")
        print (f"Jumlah Pasir: {bahan_bangunan[1][2]} unit")     
        print (f"Jumlah Batu: {bahan_bangunan[2][2]} unit")     
        print (f"Jumlah Air: {bahan_bangunan[3][2]} unit")     

#f10
def laporancandi():
    if nama_user != "Bondowoso" :
        print ("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")

    else :  
        total_candi = 0  
        total_pasir = 0
        total_batu = 0
        total_air = 0
        candi_termahal = 0
        candi_termurah = 162500

        for i in range (1, candi[0]+1):
            if candi[i][0] != None:
                total_candi += 1
                total_pasir += int(candi[i][2])
                total_batu += int(candi[i][3])
                total_air += int(candi[i][4])    

                harga_candi = 10000*candi[i][2]+15000*candi[i][3]+7500*candi[i][4]
                if (candi_termahal < harga_candi):
                    idcandi_termahal = candi[i][0]
                    candi_termahal = harga_candi
                if (candi_termurah > harga_candi):
                    idcandi_termurah = candi[i][0]
                    candi_termurah = harga_candi

        print (f"Total Candi: {total_candi}")
        print (f"Total Pasir yang digunakan: {total_pasir}")
        print (f"Total Batu yang digunakan: {total_batu}")
        print (f"Total Air yang digunakan: {total_air}")
        print (f"ID Candi Termahal: {idcandi_termahal} (Rp {candi_termahal})")
        print (f"ID Candi Termurah: {idcandi_termurah} (Rp {candi_termurah})")

#f11
def hancurkancandi():
    global candi
    if nama_user == 'Roro':#kondisi user roro
        id_candi = int(input('Masukkan ID candi: '))

        if id_candi > candi[0] or id_candi<0:#candi tidak terdaftar
            return print('Tidak ada candi dengan ID tersebut.')
        
        else:#candi terdaftar
            while True : #memastikan input konfirmasi benar
                confirm = str(input(f'Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)?'))
                if confirm == 'Y' or confirm == 'N':
                    break
                
            if confirm == 'Y':
                hapusLineArray(candi, 5, id_candi)
                return print('Candi telah berhasil dihancurkan.')
            else:
                return print('Candi tidak jadi dihancurkan.')
            
    elif nama_user == '':#kondisi user tidak login
        return print('Silahkan login terlebih dahulu.')
    
    else :#kondisi user bukan roro
        return print('User tidak memiliki wewenang untuk menghancurkan candi.')


#f12
def ayamberkokok ():
    if nama_user != "Roro" :
        print ("Ayam berkokok hanya dapat diakses oleh akun Roro Jonggrang.")

    else :
        global candi
        count_candi = 0
        for i in range (candi[0], 0, -1):
            if candi[i][0] != "":
                count_candi += 1
        print("Kukuruyuk.. Kukuruyuk..")
        print("")
        print("Jumlah Candi : ",count_candi)
        print("")
        if count_candi >= 100 :
            print("Yah,Bandung Bondowoso memenangkan permainan!")
        else :
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print("")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        quit()

#f13
working_dir = os.getcwd() #untuk f13 dan f14; directory folder semua fungsi dan "save"

def load(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    args = parser.parse_args()

    if args.path == None:
        print("Tidak ada nama folder yang diberikan!")
        print()
        print("Usage: python main.py <nama_folder>")
        exit()
    else:
        save_dir = os.path.join(working_dir, "save") #Asumsi folder save sudah ada
        current_save_dir = os.path.join(save_dir, args.path)

        if not os.path.exists(current_save_dir):
            print(f"Folder “{args.path}” tidak ditemukan.")
            exit()
        else:
            print("Loading...")
            global users
            global candi
            global bahan_bangunan

            users = csv_to_array(os.path.join(current_save_dir, "user.csv"),users)
            candi = csv_to_array(os.path.join(current_save_dir, "candi.csv"),candi)
            bahan_bangunan = csv_to_array(os.path.join(current_save_dir, "bahan_bangunan.csv"),bahan_bangunan) 

            print("Selamat datang di program “Manajerial Candi”")
            print("Silahkan masukkan username Anda")

#f14
def save():
    nama_folder = input("Masukkan nama folder: ")
    print("Saving... ")
    
    save_dir = os.path.join(working_dir, "save")

    if "save" not in os.listdir(working_dir):
        print("Membuat folder save...")
        os.mkdir(save_dir)

    save_list = os.listdir(save_dir)
    new_save = os.path.join(save_dir, nama_folder)

    if nama_folder not in save_list:
        print(f"Membuat folder save/{nama_folder}...")
        os.mkdir(new_save)
    
    users_dir = os.path.join(new_save, "user.csv")
    candi_dir = os.path.join(new_save, "candi.csv")
    bahan_bangunan_dir = os.path.join(new_save, "bahan_bangunan.csv")

    array_to_csv(users, users_dir, 3, "username;password;role")
    array_to_csv(candi, candi_dir, 5, "id;pembuat;pasir;batu;air")
    array_to_csv(bahan_bangunan, bahan_bangunan_dir, 3, "nama;deskripsi;jumlah")

    #Todo: buat fungsi data_functions baru: array_to_csv dan pakai disini

    print(f"Berhasil menyimpan data di folder {nama_folder}!")
    

#f15
def print_help (command):
    if command == 'login':
        print('. login')
        print('   Untuk masuk menggunakan akun')
    if command == 'logout':
        print('. logout')
        print('   Untuk keluar dari akun')
    if command == 'summonjin':
        print('. summonjin')
        print('   Untuk membuat jin dengan akun baru')
    if command == 'hapusjin':
        print('. hapusjin')
        print('   Untuk menghapus akun jin')
    if command == 'ubahjin':
        print('. ubahjin')
        print('   Untuk mengubah tipe jin')
    if command == 'bangun':
        print('. bangun')
        print('   Untuk membangun candi')
    if command == 'kumpul':
        print('. kumpul')
        print('   Untuk mengumpulkan bahan-bahan untuk bangun candi')
    if command == 'batchkumpul':
        print('. batchkumpul')
        print('   Untuk memerintah semua jin mengumpulkan bahan-bahan')
    if command == 'batchbangun':
        print('. batchbangun')
        print('   Untuk mengerahkan semua jin membangun candi')
    if command == 'laporanjin':
        print('. laporanjin')
        print('   Untuk mengambil laporan kinerja para jin')
    if command == 'laporancandi':
        print('. laporancandi')
        print('   Untuk mengambil laporan progres pembangunan candi')
    if command == 'hancurkancandi':
        print('. hancurkancandi')
        print('   Untuk menghancurkan candi')
    if command == 'ayamberkokok':
        print('. ayamberkokok')
        print('   Untuk menyelesaikan permainan')
    if command == 'save':
        print('. save')
        print('   Untuk menyimpan progres permainan')
    if command == 'exit':
        print('. exit')
        print('   Untuk keluar dari program')

def help():
    help_belum_login =['login', 'exit', 'save']
    help_bondowoso = ['logout', 'summonjin', 'hapusjin', 'ubahjin', 'batchkumpul', 'batchbangun', 'laporanjin', 'laporancandi', 'save', 'exit']
    help_roro = ['logout','hancurkancandi', 'ayamberkokok', 'save', 'exit']
    help_jin_pengumpul = ['logout','kumpul','save','exit']
    help_jin_pembangun = ['logout','bangun','save','exit']
    global users
    print('=========== HELP ===========')
    if nama_user == '':
        for i in range (3):
            print((i+1), end="")
            print_help(help_belum_login[i])
    elif nama_user == 'Bondowoso':
        for i in range (10):
            print((i+1), end="")
            print_help(help_bondowoso[i])
    elif nama_user == 'Roro':
        for i in range (5):
            print((i+1), end="")
            print_help(help_roro[i])
    else:
        for i in range (3,users[0]+1):
            if users[i][0] == nama_user :
                if users[i][2] == "Pengumpul" :
                    for i in range (4):
                        print((i+1), end="")
                        print_help(help_jin_pengumpul[i])
                if users[i][2] == "Pembangun" :
                    for i in range (4):
                        print((i+1), end="")
                        print_help(help_jin_pembangun[i])

    #f16
def exit ():
    exit_command = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if exit_command == "y":
        save()
        quit()
    elif exit_command == "n":
        quit()
    else:
        exit()