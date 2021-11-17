menu_makanan = [
  {"no": '1', "nama": "Nasi Goreng", "harga": 10000,},
  {"no": '2', "nama": "Ayam Goreng", "harga": 8000,},
  {"no": '3', "nama": "Nasi Kuning", "harga": 15000,},
  {"no": '4', "nama": "Nasi Pecel  ", "harga": 1200},
  {"no": '5', "nama": "Es Teh     ", "harga": 4000},
  {"no": '6', "nama": "Es Jeruk    ", "harga": 6000},
  {"no": '7', "nama": "Jus Alpukat", "harga": 10000,},
  {"no": '8', "nama": "Jus Mangga  ", "harga": 9000}
]
menu_pesanan = [[],[],[],[]]

def menu():
    print("""
==================================
       WELCOME TO RESTO
==================================
    1. Tambah Pesanan
    2. Hapus Pesanan
    3. Lihat Pesanan
    4. Bayar Pesanan
    5. Keluar
    """)
   
    
def tambah_pesanan():
    while True :
        try:
            print("""
    ==============================    
            DAFTAR MENU
    ==============================
        """)
            for menu in menu_makanan:
                print(f"[{menu['no']}] {menu['nama']}","\t=> Rp ", f"{menu['harga']}")

            pesanan = int(input("\nMasukkan Nomor Pesanan : ")) - 1
            qty = int(input("Masukkan Banyak Pesanan : "))
            menu_dipesan = menu_makanan[pesanan]
            harga_qty = int(menu_dipesan["harga"]) * qty
            
            if menu_dipesan["nama"] not in menu_pesanan[0] :
                menu_pesanan[0].append(menu_dipesan["nama"])
                menu_pesanan[1].append(menu_dipesan["harga"])
                menu_pesanan[2].append(qty)
                menu_pesanan[3].append(harga_qty)
            else:
                harga_qty = int(menu_dipesan["harga"]) * qty
                tambahan_qty = menu_pesanan[2]
                tambahan_harga = menu_pesanan[3]
                index = menu_pesanan[0].index(menu_dipesan["nama"])
                tambahan_qty[index] = tambahan_qty[index] + qty
                tambahan_harga[index] = tambahan_harga[index] + harga_qty

            ulang = input("Apakah Ingin Memesan Lagi ? (y/n) : ")
            if ulang == "n":
                
                break

        except:
            print("Menu Tidak Ada Silahkan Memilih Kembali")

def hapus_pesanan():
    while True:
        try:
            from itertools import count
            print("""
    ===============================    
        DAFTAR MENU PESANAN
    ===============================
""")
            for index,nama, harga,jumlah in zip(count(),menu_pesanan[0],menu_pesanan[1],menu_pesanan[2]):
                print( "|",index +1,".","|","{}".format(nama),"\t\t\t\t -Rp ", "{}".format(harga),"|",jumlah)

            hapus_menu = int(input("Masukan nomor menu yang ingin dihapus : "))
                
            indexmenu = hapus_menu - 1
            nama_menu = menu_pesanan[0]
            harga_menu = menu_pesanan[1]
            qty_menu = menu_pesanan[2]
            total_menu = menu_pesanan[3]
            del nama_menu[indexmenu]
            del harga_menu[indexmenu]
            del qty_menu[indexmenu]
            del total_menu[indexmenu]

            print("Menu Dengan Nomor:", hapus_menu ,"Berhasil Dihapus!")
            ulang = input("Ingin Menghapus Lagi(y/n)? : ")

            if ulang == "n":
                
                break

        except:
            print("Menu Yang Dipesan Belum Ada Silahkan Memesan Terlebih Dahulu")
            break


def lihat_pesanan():
    from itertools import count
    try:
        print("""
    ===============================    
        DAFTAR MENU PESANAN
    ===============================
""")
        for index,nama, harga,jumlah in zip(count(),menu_pesanan[0],menu_pesanan[1],menu_pesanan[2]):
            print( "|",index +1,".","|","{}".format(nama),"\t\t\t\t -Rp ", "{}".format(harga),"|",jumlah)
        input("\nPencet Enter Untuk Kembali")
    except:
        print("Pesanan Anda Belum Ada Silahkan Memesan Pesanan")

def bayar_pesan():
    try:
        harga_total = sum(menu_pesanan[3])
        print("\n=================================================================================")
        print("|                             S T R U K  B E L I                                |")
        print("=================================================================================")
        from itertools import count
        for index,nama, harga,jumlah in zip(count(),menu_pesanan[0],menu_pesanan[1],menu_pesanan[2]):
            print( "|",index +1,".","|","{}".format(nama),"\t\t\t\t\t\t -Rp ", "{}".format(harga),"|",jumlah)
        print("=================================================================================")
        print(" Total Menu                                                     :","Rp", harga_total)
        print("=================================================================================")
        menu_pesanan[0].clear()
        menu_pesanan[1].clear()
        menu_pesanan[2].clear()
        menu_pesanan[3].clear()
        input("\nTekan Enter Untuk Membuat Pesanan Baru")
    except:
        print("Pesanan Belum Ada Silahkan Pesan Terlebih Dahulu")

def exit_count():
    import time
    waktu = int(5)
            
    waktu = int(5)
    for i in range(waktu) :
        print("program akan keluar dalam",(int(waktu) - i ), "detik")
        time.sleep(1)

def exit():
    import sys
    sys.exit()

def end():
    exit_count()
    exit()
    
def pilihan():
    while True:
        
        tes = input("masukan pilihan : ")
        if tes == "1":
            tambah_pesanan()
            main()
        elif tes == "2":
            hapus_pesanan()
            main()
        elif tes == "3":
            lihat_pesanan()
            main()
        elif tes =="4":
            bayar_pesan()
            main()
        elif tes == "5":
            end()
        


# MAIN

def main():
    menu()
    pilihan()
    
main()