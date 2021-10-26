pilihan ="0"
def menu(): 
    print("""
    ===========================
    |      Konversi Suhu      |
    ===========================
Pilih Proses
Ketik 1 untuk ubah Fahrenheit ke Celsius
Ketik 2 untuk ubah Kelvin ke Celsius
Ketik 3 untuk ubah Reamur ke Celsius
Ketik 4 untuk keluar
    """)
    pilihan = input()
    return pilihan

while pilihan != "4":
    pilihan = menu()
    if pilihan == "1":
        fahrenheit = float(input("Masukkan nilai Fahrenheit :  "))
                    
        celcius = (fahrenheit - 32) * 5 / 9
                    
        print(round(celcius,2), "C") 
                        
    elif pilihan == "2":
        kelvin = float(input("Masukkan nilai Kelvin :  "))
                    
        celcius = kelvin - 273
                    
        print(round(celcius, 2), "C")

    elif pilihan == "3":
        reamur = float(input("Masukkan nilai Reamur :  "))
                    
        celcius = reamur * 5 / 4
                    
        print(round(celcius, 2), "C") 

print("Terima Kasih")