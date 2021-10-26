nim = []
nama = []
fakultas = []
prodi = []
ipk = []

pilihan = 1
while pilihan != 0 :
    print("""
    
    ===========================
    |     Daftar Mahasiswa    |
    ===========================
    """)
    print ("1. Masukan Data.")
    print ("2. Tampilkan Data.")
    print ("3. Keluar.")

    pilihan = int(input("Masukkan Pilihan Anda : "))
    print("")
   
    if pilihan == 1 :
        inputnim = (int(input("Masukkan NIM : ")))
        nim.append({'NIM' : inputnim})
        inputnama = (str(input("Masukkan Nama : ")))
        nama.append({'Nama' : inputnama})
        inputfakultas = (str(input("Masukkan Fakultas : ")))
        fakultas.append({'Fakultas' : inputfakultas})
        inputprodi = (str(input("Masukkan Prodi : ")))
        prodi.append({'Prodi' : inputprodi})
        inputipk = (float(input("Masukkan IPK Terakhir : ")))
        ipk.append({'IPK' : inputipk})
        
        
    elif pilihan == 2 :
        penentu = True
        for i in range (len(nim)) :
            if penentu :
                print ("NIM\tNama\tFakultas\tProdi\tIPK")
            print (nim[i]['NIM'],'\t',nama[i]['Nama'],'\t',fakultas[i]['Fakultas'],'\t',prodi[i]['Prodi'],'\t',ipk[i]['IPK'])
            penentu = False

    elif pilihan == 3 :
        print("Terima Kasih")
        break       
