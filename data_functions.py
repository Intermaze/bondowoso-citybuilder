def sliceString(string, index): #fungsi slice array/string array[:index]
    arrayTemp = [0 for i in range (index+1)]
    newString = ''
    for i in range (index+1):
        arrayTemp[i] = string[i]
        newString += arrayTemp[i]
    return newString

def rightStrip(string, chars=None):
    
    if chars is None:
        # bila karakter yang di strip tidak diberikan, strip string berikut
        chars = ' \t\n\r\f\v'
    
    # membaca string dari belakang
    i = len(string) - 1
    while i >= 0 and string[i] in chars:
        i -= 1
    
    newString = sliceString(string, i)
    # mengembalikan string yang telah di strip
    return newString

def jumlah_elemen(line_csv):
    #line merupakan string

    count = 0
    for i in range(len(line_csv)):
        if line_csv[i] == ";":
            count += 1

    #jumlah elemen dalam 1 line csv merupakan jumlah ";" ditambah 1
    return count+1

def combine_arr2_to_arr1(arr1, arr2, N1):
    #N1 adalah panjang array (Neff)
    arr3 = [0 for i in range(N1+1)]

    for i in range(N1):
        arr3[i] = arr1[i]
    arr3[N1] = arr2

    return arr3

def csv_to_array(lokasi_fisik, array_target):

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

        array_target = combine_arr2_to_arr1(array_target, arr_line, n1)
        n1 += 1

    file.close()
    array_target[0] = n1-1 #jumlah elemen data (Neff)
    
    return array_target

def array_to_csv(array_target, lokasi_fisik, jumlah_kolom, firstline):

    file = open (lokasi_fisik,'w',newline='')

    for baris in range(array_target[0]+1):
        if baris == 0:
            file.write(firstline)
            file.write("\n")
        elif array_target[baris][0] == None: #jika isi array None (terhapus), tidak di
            pass
        else:
            stringtemp = ""
            for i in range(jumlah_kolom):
                stringtemp += str(array_target[baris][i])
                if i != jumlah_kolom-1:
                    stringtemp += ";"
            file.write(stringtemp)
            file.write("\n")
    
    file.close()

    


