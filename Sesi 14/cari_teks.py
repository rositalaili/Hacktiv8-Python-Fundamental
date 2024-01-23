#Pencarian kata dalam Teks
teks = """Ini adalah contoh teks.
Teks ini digunakan untuk latihan pencarian kata."""

kata_cari = input("Masukkan kata yang ingin Anda cari: ")

if kata_cari in teks:
    print(f"'{kata_cari}' ditemukan dalam teks.")
else:
    print(f"'{kata_cari}' tidak ditemukan dalam teks.")
