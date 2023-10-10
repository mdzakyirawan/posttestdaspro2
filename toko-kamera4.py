#Muhammad Dzaky Irawan
#2309116031


import os
os.system('cls')

from prettytable import PrettyTable

# Data produk kamera
produk_kamera = [
    {"id": 1, "nama": "Kamera Canon", "harga": 1000, "stok": 10},
    {"id": 2, "nama": "Kamera Nikon", "harga": 8000, "stok": 5},
    {"id": 3, "nama": "Kamera Fuji", "harga": 1200, "stok": 8},
    {"id": 4, "nama": "Kamera Sony", "harga": 1500, "stok": 12},
    {"id": 5, "nama": "Kamera Lumix", "harga": 9000, "stok": 6},
]

# Data admin (username dan password)
admin_credentials = {"username": "admin", "password": "admin123"}

# Fungsi untuk menampilkan daftar produk dalam bentuk tabel
def tampilkan_daftar_produk():
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Harga", "Stok"]
    for produk in produk_kamera:
        table.add_row([produk["id"], produk["nama"], produk["harga"], produk["stok"]])
    print(table)

# Fungsi login admin
def login_admin():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    if username == admin_credentials["username"] and password == admin_credentials["password"]:
        return True
    else:
        print("Login gagal. Username atau password salah.")
        return False

# Fungsi tambah produk (CRUD)
def tambah_produk():
    nama_produk = input("Masukkan nama produk baru: ")
    harga_produk = float(input("Masukkan harga produk: "))
    stok_produk = int(input("Masukkan stok produk: "))
    new_id = len(produk_kamera) + 1
    produk_kamera.append({"id": new_id, "nama": nama_produk, "harga": harga_produk, "stok": stok_produk})
    print("Produk berhasil ditambahkan!")

# Fungsi ubah stok produk (CRUD)
def ubah_stok_produk():
    tampilkan_daftar_produk()
    id_produk = int(input("Masukkan ID produk yang akan diubah stoknya: "))
    stok_baru = int(input("Masukkan stok baru: "))
    for produk in produk_kamera:
        if produk["id"] == id_produk:
            produk["stok"] = stok_baru
            print("Stok produk berhasil diubah!")
            return
    print("Produk dengan ID tersebut tidak ditemukan.")

# Fungsi hapus produk (CRUD)
def hapus_produk():
    tampilkan_daftar_produk()
    id_produk = int(input("Masukkan ID produk yang akan dihapus: "))
    for produk in produk_kamera:
        if produk["id"] == id_produk:
            produk_kamera.remove(produk)
            print("Produk berhasil dihapus!")
            return
    print("Produk dengan ID tersebut tidak ditemukan.")

# Fungsi transaksi (untuk user)
def transaksi():
    tampilkan_daftar_produk()
    total_harga = 0
    while True:
        id_produk = int(input("Masukkan ID produk yang akan dibeli (0 untuk selesai): "))
        if id_produk == 0:
            break
        for produk in produk_kamera:
            if produk["id"] == id_produk:
                if produk["stok"] > 0:
                    total_harga += produk["harga"]
                    produk["stok"] -= 1
                else:
                    print("Stok produk habis. Silakan pilih produk lain.")
                break
        else:
            print("Produk dengan ID tersebut tidak ditemukan.")
    print(f"Total harga pembelian: Rp{total_harga:.2f}")

# Program utama
while True:
    print("\nSelamat datang di Toko Kamera")
    print("1. Login Admin")
    print("2. Login User")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if login_admin():
            while True:
                print("\nMenu Admin:")
                print("1. Tampilkan Daftar Produk")
                print("2. Tambah Produk")
                print("3. Ubah Stok Produk")
                print("4. Hapus Produk")
                print("5. Keluar")
                admin_menu = input("Pilih menu: ")

                if admin_menu == "1":
                    tampilkan_daftar_produk()
                elif admin_menu == "2":
                    tambah_produk()
                elif admin_menu == "3":
                    ubah_stok_produk()
                elif admin_menu == "4":
                    hapus_produk()
                elif admin_menu == "5":
                    break
                else:
                    print("Pilihan tidak valid.")

    elif pilihan == "2":
        transaksi()

    elif pilihan == "3":
        print("Terima kasih! Sampai jumpa lagi.")
        break

    else:
        print("Pilihan tidak valid.")
