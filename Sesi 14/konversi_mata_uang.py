#Konversi mata uang

def konversi_mata_uang(jumlah, nilai_tukar):
    return jumlah*nilai_tukar

usd_ke_idr = 15000

jumlah_usd = float(input("Masukkan jumlah dalam USD: "))
jumlah_idr = konversi_mata_uang(jumlah_usd, usd_ke_idr)

print(f"{jumlah_usd} USD setara dengan {jumlah_idr} IDR.")