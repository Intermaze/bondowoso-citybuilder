def run(fungsi):
    if fungsi == "login":
        login()

#f01
def login():
    #masalahnya belum tau mau gimana ngecek setiap indeks tanpa out of range
    username = input("Username: ")
    password = input("Password: ")
    nama_user='' #string ini kosong bila keadaan logout dan jika login akan terisi username yang login
                    #nama user juga bisa menjadi penanda askes yang dimiliki suatu akun

#f02
def logout():
    if nama_user != '' :
        nama_user='' #ngosongin identitas login yang dibuat di login, agar aksesnya hilang dan harus login kembali
        print('Logout berhasil!')
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

#f03
def summonjin():
    while True:
        nomor_jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        if 0<nomor_jenis_jin<3:
            break
        print(f'Tidak ada jenis jin bernomor "{nomor_jenis_jin}"!')

    if nomor_jenis_jin == 1 :
        jenis_jin = 'pengumpul'
    else:
        jenis_jin = 'pembangun'

    while True:
        username_jin = input('Masukkan username jin: ')
        if #disini ngecek setiap indeks user apakah ada yang sama atau nggak
            break
        print(f'Username “{username_jin}” sudah diambil!')

    while True:
        password_jin = input('Masukkan password jin: ')
        if 4<password_jin<26 :
            break
        print('Password panjangnya harus 5-25 karakter!')
    
    arrTemp = [username_jin, password_jin, jenis_jin] #gw gatau ini formatnya gimana, apa mo tambahin langsung bebas
    # nambahin array temp ke array user tapi w gatau, pake yg combine array di data kah?

