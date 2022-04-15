# untuk melakukan read pada file .txt lalu memasukanya pada dictionary
def baca_data(filename):
        # membuka file
    file = open(filename,"r")
    
    # dict kosong
    pertandingan = {}
    data_tim = {}
    data_score = {}
    data_score2 = {}
    data_tim2 = {}
        # read txt
    for live in file.readlines():
            # memisahkan new line
        list_kata = live.split()

        # memasukan list kata kedalam dict pertandingan
        if "tanding" in pertandingan:
            pertandingan["tanding"].append(list_kata)
        else:
            pertandingan["tanding"] = [list_kata]
        # memasukan list kata[0] kedalam dict data tim
        if "tim" in data_tim:
            data_tim["tim"].append(list_kata[0])
        else:
            data_tim["tim"] = [list_kata[0]]
        # memasukan list kata[1] kedalam data score
        if "score" in data_score:
            data_score["score"].append(list_kata[1])
        else:
            data_score["score"] = [list_kata[1]]
        # memasukan list kata[2] kedalam data score 2
        if "score2" in data_score2:
            data_score2["score2"].append(list_kata[2])
        else:
            data_score2["score2"] = [list_kata[2]]
        # memasukan list kata[3] kedalam data tim 2
        if "tim2" in data_tim2:
            data_tim2["tim2"].append(list_kata[3])
        else:
            data_tim2["tim2"] = [list_kata[3]]


    
    return data_tim,data_score,data_score2,data_tim2,pertandingan




# memperhitungkan total gol tim dan rata rata gol pada tim dari input nama tim yang dilakukan user
def kalkulasi(data_tim,data_score,data_score2,data_tim2,input1):
   # mengubah score 1 menjadi integer 
    x = [int(j) for j in data_score["score"]]
        # menyatukan data tim 1 dan score 1 kedalam dict, dengan key data tim 1 dan value score 2
    tim1 = {}
    tim1 = dict(zip(data_tim["tim"],x))


    # mengubah score 2 menjadi integer
    x2 = x = [int(j) for j in data_score2["score2"]]
    # menyatukan data tim 2 dan score 2 kedalam dict, dengan key data tim 2 dan value score 2
    tim2 = {}
    tim2 = dict(zip(data_tim2["tim2"],x2))

        # dibuat 0 lebih dulu agar bisa di return
    jumlah = 0
    jumlah1 = 0

        
    # kalkulasi total gol
    jumlah1 = tim1[input1] + tim2[input1]
    # kalkulasi rata rata gol
    jumlah = jumlah1//2

    


    return jumlah, jumlah1
    

# membuat daftar pertandingan, dan daftar tim
def menu(pertandingan,datatim):
        # memasukan value dari dict pertandingan kedalam list tanding
    tanding = pertandingan["tanding"]
    # memasukan value dari dict data tim kedalam list list_tim
    list_tim = datatim["tim"] 




    
    return tanding, list_tim
# isi print yang menampilkan daftar tim, daftar pertandingan
def dashboard(tanding,list_tim):
    
                                                        # Menu #
#--------------------------------------------------------------------------------------------------------------------------------
        # berisikan daftar pertandingan
        # membuat garis untuk merapihkan
        print(130*"_")
        # membuat garis dan judul agar terlihat rapih
        print(50*"-","Match",66*"-")
        # print(str(list).replace("'", "").replace(",", "") gunanya untuk mengubah tanda ' jadi space kosong dan tanda , jadi space kosong, sehingga mudah dibaca
        [print(str(tanding[0]).replace("'", "").replace(",", "")) ,print(str(tanding[1]).replace("'", "").replace(",", "")),print(str(tanding[2]).replace("'", "").replace(",", ""))
        ,print(str(tanding[3]).replace("'", "").replace(",", "")),print(str(tanding[4]).replace("'", "").replace(",", "")),print(str(tanding[5]).replace("'", "").replace(",", ""))
        ,print(str(tanding[6]).replace("'", "").replace(",", "")),print(str(tanding[7]).replace("'", "").replace(",", "")),print(str(tanding[8]).replace("'", "").replace(",", ""))
        ,print(str(tanding[9]).replace("'", "").replace(",", "")),print(str(tanding[10]).replace("'", "").replace(",", "")),print(str(tanding[11]).replace("'", "").replace(",", ""))
        ,print(str(tanding[12]).replace("'", "").replace(",", "")),print(str(tanding[13]).replace("'", "").replace(",", "")),print(str(tanding[14]).replace("'", "").replace(",", ""))
        ,print(str(tanding[15]).replace("'", "").replace(",", "")),print(str(tanding[16]).replace("'", "").replace(",", "")),print(str(tanding[17]).replace("'", "").replace(",", ""))
        ,print(str(tanding[18]).replace("'", "").replace(",", "")),print(str(tanding[19]).replace("'", "").replace(",", ""))]
        print(130*"_")

        #-------------------------------------------------Daftar Tim-------------------------------------------------------------------
        # berisikan daftar tim
        print(50*"-","Daftar Tim",66*"-")
        # print(str(list).replace("'", "").replace(",", "") gunanya untuk mengubah tanda ' jadi space kosong dan tanda , jadi space kosong, sehingga mudah dibaca
        print(str(list_tim[0]).replace("'", "").replace(",", ""))
        print(str(list_tim[1]).replace("'", "").replace(",", ""))
        print(str(list_tim[2]).replace("'", "").replace(",", ""))
        print(str(list_tim[3]).replace("'", "").replace(",", ""))
        print(str(list_tim[4]).replace("'", "").replace(",", ""))
        print(str(list_tim[5]).replace("'", "").replace(",", ""))
        print(str(list_tim[6]).replace("'", "").replace(",", ""))
        print(str(list_tim[7]).replace("'", "").replace(",", ""))
        print(str(list_tim[8]).replace("'", "").replace(",", ""))
        print(str(list_tim[9]).replace("'", "").replace(",", ""))
        print(str(list_tim[10]).replace("'", "").replace(",", ""))
        print(str(list_tim[11]).replace("'", "").replace(",", ""))
        print(str(list_tim[12]).replace("'", "").replace(",", ""))
        print(str(list_tim[13]).replace("'", "").replace(",", ""))
        print(str(list_tim[14]).replace("'", "").replace(",", ""))
        print(str(list_tim[15]).replace("'", "").replace(",", ""))
        print(str(list_tim[16]).replace("'", "").replace(",", ""))
        print(str(list_tim[17]).replace("'", "").replace(",", ""))
        print(str(list_tim[18]).replace("'", "").replace(",", ""))
        print(str(list_tim[19]).replace("'", "").replace(",", ""))
        print(130*"_")
        



# Main Program
file_name = "file teks.txt"
data_tim,data_score,data_score2,data_tim2,pertandingan = baca_data(file_name)
tanding, list_tim = menu(pertandingan,data_tim)
dashboard(tanding,list_tim)

    
# Main program #2 ------------------------------------------------------------------------------------------------------------------------------
# input untuk user
inputan = input("\nMasukan nama tim: ")
# input untuk kalkulasi
input_ = inputan 
jumlah, jumlah1 = kalkulasi(data_tim,data_score,data_score2,data_tim2,input_)
# untuk membuat garis agar rapih
print(130*"_")

# bagian ini untuk input, jadi ketika input nama tim dimasukan maka akan keluar salah satu dari statement ini, sehingga ketika user memasukan nama tim maka yang keluar adalah pertandinganya, total gol, dan rata rata gol
if inputan == "brentford":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[0]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[12]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "arsenal":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[0]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[18]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "man_utd":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[1]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[16]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "leeds":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[1]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[13]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "burnley":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[2]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[10]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "brighton":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[2]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[15]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "chelsea":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[3]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[18]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "crystal_palace":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[3]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[12]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "everton":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[4]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[13]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "southampton":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[4]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[16]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "leicester":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[5]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[19]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "wolves":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[5]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[17]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "watford":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[6]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[15]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "aston_villa":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[6]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[11]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "norwich":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[7]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[14]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "liverpool":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[7]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[10]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "new_castle":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[8]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[11]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "west_ham":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[8]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[19]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "spurs":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[9]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[17]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
elif inputan == "man_city":
        print("I",50*" ", "Data List", 66*" ","I")
        print(50*"-", inputan , 70*"-")
        print("Pertandingan 1: ",str(tanding[9]).replace("'", "").replace(",", ""), "\nPertandingan 2: ",str(tanding[14]).replace("'", "").replace(",", ""), "\nTotal gol: ",jumlah1, "\nRata-rata gol tiap pertandingan: ", jumlah )
else:
    pass