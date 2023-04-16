from data_functions import csv_to_array

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

users = csv_to_array("save/user.csv", users)
candi = csv_to_array("save/candi.csv", candi)
bahan_bangunan = csv_to_array("save/bahan_bangunan.csv", bahan_bangunan)

#Indeks yang tidak dipakai (hanya berisi nama indeks) diubah menjadi Neff, menjadi [Neff, [data]]
users[0] = 2
candi[0] = 0
bahan_bangunan[0] = 0

#Tipe data untuk jin
#[Neff, [username_jin, password_jin, jenis_jin]]
#[0] disini adalah Neff
jin = [0]

nama_user = "" #string ini kosong bila keadaan logout dan jika login akan terisi username yang login
            #nama user juga bisa menjadi penanda askes yang dimiliki suatu akun
