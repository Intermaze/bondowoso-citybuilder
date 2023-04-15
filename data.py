def rightStrip(string, chars=None):
    
    if chars is None:
        # bila karakter yang di strip tidak diberikan, strip string berikut
        chars = ' \t\n\r\f\v'
    
    # membaca string dari belakang
    i = len(string) - 1
    while i >= 0 and string[i] in chars:
        i -= 1

    # mengembalikan string yang telah di strip
    return string[:i+1]



def jumlah_elemen(line_csv):
    #line merupakan string

    count = 0
    for i in range(len(line_csv)):
        if line_csv[i] == ";":
            count += 1

    #jumlah elemen dalam 1 line csv merupakan jumlah ";" ditambah 1
    return count+1

#Fungsi append buatan
def append_arr2_to_arr1(arr1, arr2, N1, N2):
    #N1 dan N2 adalah panjang array
    arr3 = [0 for i in range(N1+N2)]

    for i in range(N1):
        arr3[i] = arr1[i]
    for i in range(N2):
        arr3[N1+i] = arr2[i]

    return arr3

def combine_arr2_to_arr1(arr1, arr2, N1):
    #N1 dan N2 adalah panjang array
    arr3 = [0 for i in range(N1+1)]

    for i in range(N1):
        arr3[i] = arr1[i]
    arr3[N1] = arr2

    return arr3

    

def csv_to_array(lokasi_fisik, variabel_target):

    #Inisialisasi
    file = open(lokasi_fisik, 'r')
    n1 = 0 #jumlah elemen variabel_target

    for line in file:
        line = rightStrip(line) #Menghilangkan "\n"

        arr_line = [0 for i in range(jumlah_elemen(line))]

        temp = ""
        element_count = 0
        for i in range(len(line)):
            if line[i] != ";":
                temp += line[i]
            else:
                arr_line[element_count] = temp
                element_count += 1
                temp = ""

        #Ada elemen lagi, karena tidak ada ";" di akhir line
        arr_line[element_count] = temp

        variabel_target = combine_arr2_to_arr1(variabel_target, arr_line, n1)
        n1 += 1
    
    return variabel_target


    


