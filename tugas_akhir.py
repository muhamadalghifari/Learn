menu = [
    print("=" * 80),
    print("|" + " " * 28 + "D A F T A R   M E N U" + " " * 29 + "|"),
    print("=" * 80),
    print("|         Makanan        |", "        Minuman        |","          Camilan          |"),
    print("-" * 80),
    print("|  Ayam Goreng  :", 30000, " |  Jus Jeruk    :", 10000, " |  Pisang Coklat    :", 15000, " |"),
    print("|  Nasi Goreng  :", 20000, " |  Jus Alpukat  :", 10000, " |  Udang Keju       :", 15000, " |"),
    print("|  Sate Ayam    :", 20000, " |  Es Kelapa    :", 10000, " |  Udang Rambutan   :", 15000, " |"),
    print("|  Bakso        :", 20000, " |  Kopi Hitam   :", 8000, "  |  Kentang Goreng   :", 15000, " |"),
    print("|  Soto Ayam    :", 20000, " |  Es Teh       :", 8000, "  |  Roti Bakar       :", 10000, " |"),
    print("|  Mie Goreng   :", 15000, " |  Air Mineral  :", 5000, "  |  Siomay           :", 10000, " |"),
    print("=" * 80),
    print("=" * 80),
    print("|       Untuk pembelian diatas Rp50.000 mendapatkan diskon sebesar 10%         |"),
    print("|           Silakan untuk memilih opsi yang tersedia di bawah ini              |"),
    print("=" * 80),
]

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def view_order(self):
        if not self.items:
            print("Keranjang Anda kosong.")
        else:
            print("Keranjang Anda:")
            for item in self.items:
                print(f"{item.name}: Rp{item.price}") 
            total = sum(item.price for item in self.items)
            print(f"Total: Rp{total}")

    def checkout(self):
        total = sum(item.price for item in self.items)
        if total > 50000:
            discount = total * 0.1
            total -= discount
            print(f"Anda mendapat diskon 10%! Total setelah diskon: Rp{total:.2f}")
        else:
            print(f"Total yang harus dibayar: Rp{total:.2f}")
        self.items = []  # Kosongkan keranjang setelah checkout
        print("Terima kasih telah memesan!")

    def cancel_order(self):
        self.items = []
        print("Pesanan Anda telah dibatalkan.")

class Menu:
    def __init__(self):
        self.items = [
            MenuItem("Ayam Goreng", 30000),
            MenuItem("Nasi Goreng", 20000),
            MenuItem("Sate Ayam", 20000),
            MenuItem("Bakso", 20000),
            MenuItem("Soto Ayam", 20000),
            MenuItem("Mie Goreng", 15000),
            MenuItem("Jus Jeruk", 10000),
            MenuItem("Jus Alpukat", 10000),
            MenuItem("Es Kelapa", 10000),
            MenuItem("Kopi Hitam", 8000),
            MenuItem("Es Teh", 8000),
            MenuItem("Air Mineral", 5000),
            MenuItem("Pisang Coklat", 15000),
            MenuItem("Udang Keju", 15000),
            MenuItem("Udang Rambutan", 15000),
            MenuItem("Kentang Goreng", 15000),
            MenuItem("Roti Bakar", 10000),
            MenuItem("Siomay", 10000)
        ]

    def view_menu(self):
        print("Menu:")
        for item in self.items:
            print(f"{item.name}: Rp{item.price}")

menu = Menu()
order = Order()

while True:
    print("\nPilih opsi:")
    print("1. Tambah item ke keranjang")
    print("2. Hapus item dari keranjang")
    print("3. Lihat keranjang")
    print("4. Checkout")
    print("5. Batalkan pesanan")
    print("0. Keluar")
        
    choice = input("Masukkan pilihan Anda: ")
        
    try:
        if choice == '1':
            item_name = input("Masukkan nama item yang ingin dipesan: ")
            found_items = [item for item in menu.items if item.name.lower() == item_name.lower()]
            if found_items:
                order.add_item(found_items[0])
                print(f"{item_name} telah ditambahkan ke keranjang Anda.")
            else:
                print(f"{item_name} tidak ditemukan di menu.")
            
        elif choice == '2':
            item_name = str(input("Masukkan nama item yang ingin dihapus dari keranjang: "))
            order.remove_item(item_name)

        elif choice == '3':
            order.view_order()
            
        elif choice == '4':
            order.view_order()
            confirm = input("Apakah Anda yakin ingin checkout? (y/n): ")
            if confirm.lower() == 'y':
                order.checkout()
            
        elif choice == '5':
            confirm = input("Apakah Anda yakin ingin membatalkan pesanan? (y/n): ")
            if confirm.lower() == 'y':
                order.cancel_order()
            
        elif choice == '0':
            print("Terima kasih, sampai jumpa!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    except ValueError:
        print("Input tidak valid. Silakan masukkan pilihan yang benar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
