print("+" + 54 * "=" + "+")
print(("|" + " " * 54 + "|\n")*2, end="")
print("|                  SELAMAT DATANG DI                   |")
print("|                     HOTEL PYTHON                     |")
print(("|" + " " * 54 + "|\n")*2, end="")
print("+" + 54 * "=" + "+")
print()
print("                  DESKRIPSI AKOMODASI                   ")
print("Hotel Python adalah hotel bintang-10 dengan kolam renang\noutdoor. Hotel ini menyediakan kamar-kamar modern dengan\nWIFI gratis.Terletak di Jalan Lapangan Udara di Cirebon.")
print()
print("     FASILITAS-FASILITAS YANG ADA DI HOTEL PYTHON :     ")
print()
print(" " * 10 + "Relevan untuk trip Anda: ")
print(" " * 10 + "a. AC")
print(" " * 10 + "b. WIFI Gratis")
print(" " * 10 + "c. Kamar Mandi Pribadi")
print(" " * 10 + "d. Smart TV")
print(" " * 10 + "e. Parkir Gratis")
print()
print(" " * 10 + "Kamar Mandi: ")
print(" " * 10 + "a. Tisu Toilet")
print(" " * 10 + "b. Handuk")
print(" " * 10 + "c. Sandal")
print(" " * 10 + "d. Kamar Mandi Pribadi")
print(" " * 10 + "e. Toilet")
print(" " * 10 + "f. Peralatan Mandi")
print(" " * 10 + "g. Pengering Rambut")
print(" " * 10 + "h. Shower")
print()
print(" " * 10 + "Kamar Tidur: ")
print(" " * 10 + "a. Lemari")
print(" " * 10 + "b. Bed Cover")
print(" " * 10 + "c. Kasur dan Tempat Tidur")
print(" " * 10 + "d. Meja Rias")
print(" " * 10 + "e. Bantal dan Guling")
print(" " * 10 + "f. Lampu Tidur")
print()
print(" " * 10 + "Outdoor: ")
print(" " * 10 + "a. Teras")
print(" " * 10 + "b. Taman")
print()
print(" " * 10 + "Dapur: ")
print(" " * 10 + "a. Ketel Listrik")
print(" " * 10 + "b. Kulkas")
print(" " * 10 + "c. Alat Makan")
print()
print(" " * 10 + "Amenitas Kamar:")
print(" " * 10 + "a. Stop Kontak Dekat Tempat Tidur")
print()
print(" " * 10 + "Kegiatan: ")
print(" " * 10 + "a. Mini Golf")
print(" " * 10 + "b. Taman Bermain Anak")
print(" " * 10 + "c. Pijat")
print(" " * 10 + "d. Spa")
print(" " * 10 + "e. Gym")
print(" " * 10 + "f. Kolam Renang")
print()
print(" " * 10 + "Umum: ")
print(" " * 10 + "a. Layanan Antar Jemput")
print(" " * 10 + "b. AC")
print(" " * 10 + "c. Lift")
print(" " * 10 + "d. Antar Jemput Bandara")
print()



print("           SILAHKAN PILIH MENU DIBAWAH INI :            ")
while True:
    print(" " * 4 +"1. RESERVASI KAMAR")
    print(" " * 4 +"2. EDIT PESANAN")
    print(" " * 4 +"3. DELETE PESANAN")
    print(" " * 4 +"4. CETAK TRANSAKSI")
    print(" " * 4 +"5. CHECK-IN")
    print(" " * 4 +"6. CHECK-OUT")
    print(" " * 4 +"7. LIHAT KAMAR TERSEDIA")
    print(" " * 4 +"8. MENCARI PESANAN DENGAN KODE PEMESANAN")
    print(" " * 4 +"9. RIWAYAT TRANSAKSI" )
    print(" " * 4 +"0. EXIT")
    try:
        menu = int(input("Masukkan nomor menu yang dipilih : "))
        break
    except:
        print("HANYA PILIH ANGKA 0 SAMPAI 9 SAJA!")