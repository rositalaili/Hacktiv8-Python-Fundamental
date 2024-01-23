import sqlite3

def baca_data_sqlite(database_file):
    connection=sqlite3.connect(database_file)
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM produk")
    data = cursor.fetchal1()
    connection.close()
    return data

def tambah_data_sqlite(database_file, nama_produk, harga, stok):
    connection=sqlite3.connect(database_file)
    cursor=connection.cursor()
    cursor.execute("INSERT INTO produk (nama_produk, harga, stok) VALUES (?,?,?)",
                   (nama_produk, harga, stok))
    connection.commit()
    connection.close()

def main():
    database_file='produk.db'
    produk = baca_data_sqlite(database_file)

    print("Data Produk:")
    for item in produk:        
        print(f"{item[1]}: {item[2]} IDR, Stok: {item[3]}")    
    
    tambah_produk = input("Tambah produk baru? (y/n): ")    
    if tambah_produk.lower() == 'y':        
        nama_produk = input("Nama produk: ")        
        harga_produk = input("Harga produk (IDR): ")        
        stok_produk = input("Stok produk: ")        
        
        tambah_data_sqlite(database_file, nama_produk, harga_produk, stok_produk)        
        print("Produk berhasil ditambahkan dan disimpan.")

if __name__ == "__main__":    
    main()
