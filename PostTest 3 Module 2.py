list_user = ["admin"]
list_password = ["admin"]

main = False

while main != True :
    print("""
==================================
       WELCOME TO LOGIN APP
==================================
    1. Login
    2. Register
    3. Keluar
    """)
    pilihan = input("Masukkan pilihan : ")

    int_attempt_counter = 0

    if pilihan == "1":
        print(
"""
==================================
            LOGIN MENU
==================================
""")
        #Login User
        loginuser = "1"
        while loginuser != "0":
            login_user = input("Username : ")
            login_user = login_user.lower()
            if login_user in list_user:
                index_username = list_user.index(login_user)
                loginuser = "0"
                int_attempt_counter = 0
            else:
                print("Username Tidak Terdaftar\n")
                loginuser = "1"
                int_attempt_counter += 1
                print("Anda Telah Salah Memasukkan Username : ",int_attempt_counter, "Kali")
                if int_attempt_counter > 2:
                    print("\nAnda Salah Username 3 Kali Aplikasi Akan Keluar")
                    exit()
                    

        #Login Password
        loginpass = "1"
        while loginpass != "0":
            login_password = input("Password : ")
            if login_password == list_password[index_username]:
                loginpass = "0"
                print(
"""
==================================
Selamat Datang Anda Berhasil Login
==================================
""")
                logout = input("Apakah Anda Ingin Logout (y) : ")
                logout = logout.lower
                if logout == "y":
                    main = False
            else : 
                print("Password Yang Anda Masukkan Salah\n")
                print("Username :",login_user)
                loginpass = "1"
                int_attempt_counter += 1
                print("Anda Telah Salah Memasukkan Password : ",int_attempt_counter, "Kali")
                if int_attempt_counter > 2:
                    print("\nAnda Salah Memasukkan Password 3 Kali Aplikasi Akan Keluar")
                    exit()

    elif pilihan == "2":
        loopuser = True
        print(
"""
==================================
          REGISTER MENU
==================================
""")
        while loopuser != False:
            register_username = input("Masukkan Username : ")
            register_username = register_username.lower()
            if register_username not in list_user:
                list_user.append(register_username)
                loopuser = False
            else :
                print("Username",register_username, "Sudah Ada, Gunakan Username Lain\n")
                loopuser = True

        register_password = input("Masukkan Password : ")

        konfirmasi = False
        while konfirmasi != True:
            konfirmasi_password = input("Konfirmasi Password : ")
            if register_password == konfirmasi_password:
                list_password.append(register_password)
                konfirmasi = True
            else :
                print("\nKonfirmasi Password Tidak Sesuai\n")
                konfirmasi = False

        print("Akun Anda Berhasil Didaftar Silahkan Login")
        main = False

    elif pilihan == "3":
        print("\nSelamat Tinggal")
        main = True