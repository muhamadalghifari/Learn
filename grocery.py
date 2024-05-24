class TokoKelontong:
    def __init__(self):
        self.inventaris = {}
        self.total_penjualan = 0.0
        self.riwayat_penjualan = []

    def tambah_item(self, nama, harga, stok):
        self.inventaris[nama] = {'harga': harga, 'stok': stok}
        print(f"Item {nama} ditambahkan ke inventaris.")

    def hapus_item(self, nama):
        if nama in self.inventaris:
            del self.inventaris[nama]
            print(f"Item {nama} dihapus dari inventaris.")
        else:
            print(f"Item {nama} tidak ditemukan dalam inventaris.")

    def perbarui_harga(self, nama, harga_baru):
        if nama in self.inventaris:
            self.inventaris[nama]['harga'] = harga_baru
            print(f"Harga untuk {nama} diperbarui menjadi Rp{harga_baru}.")
        else:
            print(f"Item {nama} tidak ditemukan dalam inventaris.")

    def tampilkan_inventaris(self):
        for item, info in self.inventaris.items():
            print(f"{item}: Rp{info['harga']} (Stok: {info['stok']})")

    def proses_penjualan(self, nama, jumlah):
        if nama in self.inventaris and self.inventaris[nama]['stok'] >= jumlah:
            total_biaya = self.inventaris[nama]['harga'] * jumlah
            self.inventaris[nama]['stok'] -= jumlah
            self.total_penjualan += total_biaya
            self.riwayat_penjualan.append((nama, jumlah, total_biaya))
            print(f"Terjual {jumlah} {nama}. Total biaya: Rp{total_biaya}")
        else:
            print(f"Stok tidak mencukupi untuk {nama} atau item tidak ditemukan.")

    def tampilkan_total_penjualan(self):
        print(f"Total penjualan: Rp{self.total_penjualan}")

    def cari_item(self, nama):
        if nama in self.inventaris:
            item = self.inventaris[nama]
            print(f"{nama}: Rp{item['harga']} (Stok: {item['stok']})")
        else:
            print(f"Item {nama} tidak ditemukan dalam inventaris.")

    def restok_item(self, nama, jumlah):
        if nama in self.inventaris:
            self.inventaris[nama]['stok'] += jumlah
            print(f"Restok {nama} dengan {jumlah} unit. Stok baru: {self.inventaris[nama]['stok']}")
        else:
            print(f"Item {nama} tidak ditemukan dalam inventaris.")

    def buat_laporan_penjualan(self):
        print("Laporan Penjualan:")
        for penjualan in self.riwayat_penjualan:
            print(f"Item: {penjualan[0]}, Jumlah: {penjualan[1]}, Total Biaya: Rp{penjualan[2]}")
        print(f"Total penjualan: Rp{self.total_penjualan}")

def main():
    toko = TokoKelontong()

    while True:
        print("\nManajemen Toko Kelontong")
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Perbarui Harga")
        print("4. Tampilkan Inventaris")
        print("5. Proses Penjualan")
        print("6. Tampilkan Total Penjualan")
        print("7. Cari Item")
        print("8. Restok Item")
        print("9. Buat Laporan Penjualan")
        print("10. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            nama = input("Masukkan nama item: ")
            harga = float(input("Masukkan harga item: "))
            stok = int(input("Masukkan stok item: "))
            toko.tambah_item(nama, harga, stok)
        elif pilihan == '2':
            nama = input("Masukkan nama item: ")
            toko.hapus_item(nama)
        elif pilihan == '3':
            nama = input("Masukkan nama item: ")
            harga_baru = float(input("Masukkan harga baru: "))
            toko.perbarui_harga(nama, harga_baru)
        elif pilihan == '4':
            toko.tampilkan_inventaris()
        elif pilihan == '5':
            nama = input("Masukkan nama item: ")
            jumlah = int(input("Masukkan jumlah: "))
            toko.proses_penjualan(nama, jumlah)
        elif pilihan == '6':
            toko.tampilkan_total_penjualan()
        elif pilihan == '7':
            nama = input("Masukkan nama item: ")
            toko.cari_item(nama)
        elif pilihan == '8':
            nama = input("Masukkan nama item: ")
            jumlah = int(input("Masukkan jumlah untuk restok: "))
            toko.restok_item(nama, jumlah)
        elif pilihan == '9':
            toko.buat_laporan_penjualan()
        elif pilihan == '10':
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
