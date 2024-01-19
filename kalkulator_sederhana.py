def tambah(x,y):
    return x+y

def kurang(x,y):
    return x-y

def kali(x,y):
    return x*y

def bagi(x,y):
    if y==0:
        return "Tidak bisa dibagi oleh 0"
    return x/y

while True:
    print("pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("masukkan nomor opreasi (1/2/3/4/5): ")

    if pilihan =="5":
        print("keluar dari kalkulator")
        break
    
    angka1=float(input("Masukkan angka pertama: "))
    angka2=float(input("Masukkan angka kedua: "))

    if pilihan=="1":
        print("Hasil:",tambah(angka1,angka2))
    elif pilihan=="2":
        print("Hasil:",kurang(angka1,angka2))
    elif pilihan=="3":
        print("Hasil:",kali(angka1,angka2))
    elif pilihan=="4":
        print("Hasil:",bagi(angka1,angka2))
    else:
        print("Pilihan tidak valid")