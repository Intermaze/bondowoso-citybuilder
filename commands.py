from data import *

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