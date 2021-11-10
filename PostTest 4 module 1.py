
food_menu = [[],[]]
drink_menu = [[],[]]
main = False

while main != True:
    print("""
    ==================================
        MENU MAKANAN DAN MINUMAN
    ==================================
        1. TAMBAH MENU
        2. LIAT MENU
        3. UPDATE MENU
        4. HAPUS MENU
        5. KELUAR
        """)
    choice = input("Masukkan pilihan : ")

    #Menu Create
    if choice == "1" :
        repeat = "y"
        while repeat != "n":
            print("""Menu Apa Yang Ingin Ditambah
        1. Makanan 
        2. Minuman""")
            add_menu = input("Pilih Jenis Menu Yang Ingin Ditambah : ")
            if add_menu == "1":
                food_new_menu = input("Masukkan Nama Menu Makanan : ")
                food_menu[0].append(food_new_menu)
                food_price = input("Masukkan Harga Menu Makanan : Rp ")
                food_menu[1].append(food_price)
                repeat = input("Apakah Ingin Menambah Menu Lain? (y,n) : ")
                main = False

            if add_menu == "2":
                drink_new_menu = input("Masukkan Nama Menu Minuman : ")
                drink_menu[0].append(drink_new_menu)
                drink_price = input("Masukkan Harga Menu Minuman: Rp ")
                drink_menu[1].append(drink_price)
                repeat = input("Apakah Ingin Menambah Menu Lain? (y,n) : ")
                main = False

    #Menu Read
    elif choice == "2":
        print("""==================================
    MENU MAKANAN
==================================""")
        for food, foodprice in zip(food_menu[0],food_menu[1]):
                print( "{}".format(food), "\t\t\t\t -Rp ", "{}".format(foodprice))

        print("""\n==================================
    MENU MINUMAN
==================================""")
        for drink, drinkprice in zip(drink_menu[0],drink_menu[1]):
                print( "{}".format(drink), "\t\t\t\t -Rp ", "{}".format(drinkprice))
        input("Kembali Ke Menu Awal Pencet Enter")
        
        main = False


    #Menu Update
    elif choice == "3":
        print("""Menu Apa Yang Ingin Anda Update
1. Makanan 
2. Minuman""")
        update_menu_choice = input("Pilih Jenis Menu Yang Ingin Diupdate: ")
        #Update Makanan
        if update_menu_choice == "1":
            print("""==================================
           MENU MAKANAN
==================================""")
            for food, foodprice in zip(food_menu[0],food_menu[1]):
                print( "{}".format(food), "\t\t\t\t -Rp ", "{}".format(foodprice))

            update_food_menu = int(input("Masukkan Nomor Menu Yang Ingin Diupdate : "))
            update_food_name = input("Masukkan Nama Menu Baru : ")
            update_food_price = input("Masukkan Harga Menu Baru : ")
            
            indexmenu = update_food_menu - 1
            foodmenu = food_menu[0]
            foodprice = food_menu[1]

            foodmenu[indexmenu] = update_food_name
            foodprice[indexmenu] = update_food_price
            main = False

        #Update Minuman
        elif update_menu_choice == "2":
            print("""\n==================================
           MENU MINUMAN
==================================""")
            for drink, drinkprice in zip(drink_menu[0],drink_menu[1]):
                print( "{}".format(drink), "\t\t\t\t -Rp ", "{}".format(drinkprice))

            update_drink_menu = int(input("Masukkan Nomor Menu Yang Ingin Dihapus : "))
            update_drink_name = input("Masukkan Nama Menu Baru : ")
            update_drink_price = input("Masukkan Harga Menu Baru : ")
            
            indexmenu = update_drink_menu - 1
            drinkmenu = drink_menu[0]
            drinkprice = drink_menu[1]

            drinkmenu[indexmenu] = update_drink_name
            drinkprice[indexmenu] = update_drink_price
            main = False

    #Menu Delete           
    elif choice == "4" :
        print("""Menu Apa Yang Ingin Anda Hapus
1. Makanan 
2. Minuman""")
        delete_menu_choice = input("Pilih Jenis Menu Yang Ingin Diupdate: ")

        #Menghapus Makanan
        if delete_menu_choice == "1":
            delete_choice = input("""Pilih Metode Hapus Menu 
1. Hapus Semua Menu Makanan
2. Hapus 1 Menu Makanan
Masukkan Pilihan Anda : """)
            #Menghapus Seluruh Menu Makanan
            if delete_choice == "1":
                confirm = input("Apakah Anda Yakin Ingin Mengosongkan Menu Makanan? (y,n) : ")
                if confirm == "y":
                    food_menu.clear()
                elif confirm == "n":
                    main = False
            
            #Menghapus 1 Menu Makanan
            elif delete_choice == "2":
                print("""==================================
           MENU MAKANAN
==================================""")
                for food, foodprice in zip(food_menu[0],food_menu[1]):
                    print( "{}".format(food), "\t\t\t\t -Rp ", "{}".format(foodprice))

                delete_food_menu = int(input("Masukkan Nomor Menu Yang Ingin Dihapus : "))
                indexmenu = delete_food_menu - 1
                foodmenu = food_menu[0]
                foodprice = food_menu[1]
                del foodmenu[indexmenu]
                del foodprice[indexmenu]
                main = False

        #Menghapus Minuman
        elif delete_menu_choice == "2":
            delete_choice = input("""Pilih Metode Hapus Menu 
1. Hapus Semua Menu Minuman
2. Hapus 1 Menu Minuman
Masukkan Pilihan Anda : """)
            #Menghapus Seluruh Menu Minum
            if delete_choice == "1":
                confirm = input("Apakah Anda Yakin Ingin Mengosongkan Menu Makanan? (y,n) : ")
                if confirm == "y":
                    drink_menu.clear()
                elif confirm == "n":
                    main = False
            
            #Menghapus 1 Menu Minuman
            elif delete_choice == "2":
                print("""\n==================================
           MENU MINUMAN
==================================""")
                for drink, drinkprice in zip(drink_menu[0],drink_menu[1]):
                    print( "{}".format(drink), "\t\t\t\t -Rp ", "{}".format(drinkprice))

                delete_drink_menu = int(input("Masukkan Nomor Menu Yang Ingin Dihapus : "))
                indexmenu = delete_drink_menu - 1
                drinkmenu = drink_menu[0]
                drinkprice = drink_menu[1]
                del drinkmenu[indexmenu]
                del drinkprice[indexmenu]
                main = False

    elif choice == "5":
        print("Terima Kasih")
        main = True