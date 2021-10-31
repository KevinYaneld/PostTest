hargamakan = []
qtymakan = []
hargaminum = []
qtyminum = []
pilih = "y"

print("""
Hari :
1. Weekdays
2. Weekend""")
hari = input("Pilih Hari : ")

while pilih != "n" :
    print("""

    ========================================================    
    |                                                      |
    |             ===========================              |
    |             |      RESTORAN KVC       |              |
    |             ===========================              |
    |                                                      |
    |           Pilih Menu Yang Anda Inginkan              |
    |                 MAKANAN                              |
    |     1. Nasi Goreng      Rp 12000                     |
    |     2. Ayam Goreng      Rp  8000                     | 
    |     3. Nasi Kuning      Rp 15000                     |
    |     4. Nasi Pecel       Rp 12000                     |
    |     5. Soto Ayam        Rp 13000                     | 
    |                 MINUMAN                              |
    |     6. Teh              Rp  4000                     |
    |     7. Es Jeruk         Rp  6000                     | 
    |     8. Jus Alpukat      Rp 10000                     |
    |     9. Jus Mangga       Rp  9000                     |
    |     10. Es Cincau       Rp  8000                     |
    |                                                      |
    | Diskon setiap Pembelian 3 Minuman sebesar 10%        |
    | Diskon setiap Pembelian 2 Makanan sebesar 5%         |
    | Diskon setiap pembayaran melalui E-money sebesar 5%  |
    | Diskon saat weekend sebesar 5%                       |
    | Mendapat Diskon saat weekdays sebesar 10%            |
    ======================================================== 
        """)

    menu = input("Masukkan Nomor Menu Yang Anda Inginkan : ")

    if menu == "1":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargamakan.append(int(12000))
        for x in range (quantity):
            qtymakan.append(1)     
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "2":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargamakan.append(int(8000))
        for x in range (quantity):
            qtymakan.append(1)       
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "3":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargamakan.append(int(15000))
        for x in range (quantity):
            qtymakan.append(1)       
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "4":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):  
            hargamakan.append(int(12000))
        for x in range (quantity):
            qtymakan.append(1)       
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "5":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargamakan.append(int(13000))
        for x in range (quantity):
            qtymakan.append(1)       
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "6":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargaminum.append(int(4000))
        for x in range (quantity):
            qtyminum.append(1)       
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "7":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargaminum.append(int(6000))
        for x in range (quantity):
            qtyminum.append(1)      
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "8":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargaminum.append(int(10000))
        for x in range (quantity):
            qtyminum.append(1)      
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "9":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargaminum.append(int(9000))
        for x in range (quantity):
            qtyminum.append(1)      
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    elif menu == "10":

        quantity = int(input("Masukkan Porsi :"))
        for x in range (quantity):
            hargaminum.append(int(8000))
        for x in range (quantity):
            qtyminum.append(1)      
        pilih = input("Apakah Ingin Order Lagi (y/n) : ")
        pilih = pilih.lower()

    else :
        print("Nomor Menu Yang Anda Pilih Tidak Ada Di Dalam Menu")
        pilih = "y"


totalmakanan = sum(hargamakan)
totalminuman = sum(hargaminum)

if sum(qtymakan) >= 2:
    makankenadiskon = sum(qtymakan) // 2
else:
    makankenadiskon = 0

if sum(qtyminum) >= 3:
    minumkenadiskon = sum(qtyminum) // 3
else:
    minumkenadiskon = 0

#Menghitung Total
if makankenadiskon > 0:
    makanan_diskon_total = 0
    int_makanan_diskon_iterasi = (makankenadiskon * 2)
    for x in hargamakan [ 0 : int_makanan_diskon_iterasi] :
        makanan_diskon_total += (x * 5 / 100)

if minumkenadiskon > 0:
    minuman_diskon_total = 0
    int_minuman_diskon_iterasi = (minumkenadiskon * 3)
    for y in hargaminum [ 0 : int_minuman_diskon_iterasi]:
        minuman_diskon_total += (y * 10 / 100)

print("""
Pembayaran
1. Cash
2. E-Money
3. Debit
""")
pembayaran = input("Pilih Metode Pembayaran : ")

print("\n=================================================================================")
print("|                             S T R U K  B E L I                                |")
print("=================================================================================")
print("\n--------------------------------- M A K A N A N ---------------------------------")
print(" Total Harga Makanan                                       : ","Rp",totalmakanan)
if sum(qtymakan) >= 2:
    print(
    " Anda Mendapatkan Diskon 5% Setiap Pembelian 2 Makanan     : ","Rp",int(makanan_diskon_total) )
else :
    makanan_diskon_total = 0
print("\n--------------------------------- M I N U M A N ---------------------------------")
print(" Total Harga Minuman                                       : ","Rp",totalminuman)
if sum(qtyminum) >= 3:
    print(
" Anda Mendapatkan Diskon 5% Setiap Pembelian 2 Makanan     : ","Rp",int(minuman_diskon_total)  )
else : 
   minuman_diskon_total = 0

int_total_menu = int((totalmakanan - makanan_diskon_total) + (totalminuman - minuman_diskon_total))

print(
"""=================================================================================
 Total Menu                                                : ""","Rp",int_total_menu)
if hari == "1":
    diskonhari = int(int_total_menu * 10 / 100)
    totalmenu = int_total_menu - diskonhari
    print(" Anda Mendapatkan Diskon Weekdays Sebesar 10%              : ","Rp", diskonhari)
    print(" Total Menu                                                : ""","Rp",totalmenu)
    print("=================================================================================")
elif hari == "2":
    diskonhari = int(int_total_menu * 10 / 100)
    totalmenu = int_total_menu - diskonhari
    print(" Anda Mendapatkan Diskon Weekend Sebesar 5%                : ","Rp", diskonhari)
    print(" Total Menu                                                : ""","Rp",totalmenu)
    print("=================================================================================")

if pembayaran == "2":
    diskonpembayaran = int(totalmenu * 5 / 100)
    totalakhir = totalmenu - diskonpembayaran
    print(" Anda Mendapatkan Diskon 5% Karena Menggunakan E-Money      : ","Rp", diskonpembayaran)
    print(" Total Menu                                                 : ","Rp",totalakhir )

print("=================================================================================")
    


