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

#Bahan awal
bahan_bangunan = [[0 for i in range(0,3)] for j in range(0,4)]
bahan_bangunan[0] = ["nama","deskripsi","jumlah"]
bahan_bangunan[1][0] = "pasir"
bahan_bangunan[1][1] = "pasir"
bahan_bangunan[2][0] = "batu"
bahan_bangunan[2][1] = "batu"
bahan_bangunan[3][0] = "air"
bahan_bangunan[3][1] = "air"

nama_user = "" #string ini kosong bila keadaan logout dan jika login akan terisi username yang login
            #nama user juga bisa menjadi penanda askes yang dimiliki suatu akun
