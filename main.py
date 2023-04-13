# File: main.py
from data import csv_to_array
import commands

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

users = csv_to_array("save/user.csv", users)
candi = csv_to_array("save/candi.csv", candi)
bahan_bangunan = csv_to_array("save/bahan_bangunan.csv", bahan_bangunan)

print(users)

while True:
  masukan = input(">>> ")
  commands.run(masukan)