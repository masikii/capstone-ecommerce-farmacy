# =====================================================
# E-COMMERCE FARMASI RUMAH SAKIT
# Capstone Project Module 1
# =====================================================

# ======================
# DATA OBAT
# ======================

obat_list = [
    {"id": "O001", "nama": "Paracetamol", "kategori": "Analgesik", "harga": 5000, "stok": 100, "terjual": 0},
    {"id": "O002", "nama": "Amoxicillin", "kategori": "Antibiotik", "harga": 15000, "stok": 50, "terjual": 0},
    {"id": "O003", "nama": "Ibuprofen", "kategori": "Anti Inflamasi", "harga": 8000, "stok": 80, "terjual": 0},
    {"id": "O004", "nama": "Cetirizine", "kategori": "Antihistamin", "harga": 7000, "stok": 60, "terjual": 0},
    {"id": "O005", "nama": "Vitamin C", "kategori": "Suplemen", "harga": 12000, "stok": 120, "terjual": 0},
    {"id": "O006", "nama": "Antasida", "kategori": "Pencernaan", "harga": 6000, "stok": 70, "terjual": 0},
    {"id": "O007", "nama": "Salbutamol", "kategori": "Asma", "harga": 20000, "stok": 40, "terjual": 0},
    {"id": "O008", "nama": "Metformin", "kategori": "Diabetes", "harga": 18000, "stok": 55, "terjual": 0},
    {"id": "O009", "nama": "Amlodipine", "kategori": "Hipertensi", "harga": 17000, "stok": 65, "terjual": 0},
    {"id": "O010", "nama": "Omeprazole", "kategori": "Asam Lambung", "harga": 14000, "stok": 75, "terjual": 0}
]

customer_list = []
transaksi_list = []

# =====================================================
# UTILITIES
# =====================================================

def generate_id(prefix, data_list):
    if not data_list:
        return f"{prefix}001"
    
    max_number = 0
    
    for data in data_list:
        number = int(data["id"][1:])
        if number > max_number:
            max_number = number
    
    new_number = max_number + 1
    return f"{prefix}{str(new_number).zfill(3)}"

def generate_transaksi_id():
    if not transaksi_list:
        return "T001"
    
    max_number = 0
    
    for data in transaksi_list:
        number = int(data["id_transaksi"][1:])
        if number > max_number:
            max_number = number
    
    new_number = max_number + 1
    return f"T{str(new_number).zfill(3)}"


def input_angka(pesan):
    while True:
        try:
            value = int(input(pesan))
            if value < 0:
                print("Input tidak boleh negatif.")
                continue
            return value
        except ValueError:
            print("Masukkan angka yang valid.")


def cari_data(data_list, key, value):
    for data in data_list:
        if data[key] == value:
            return data
    return None


# =====================================================
# CRUD OBAT
# =====================================================

def tambah_obat():
    while True:
        print("\n=== TAMBAH OBAT ===")

        nama = input("Nama Obat: ").title()
        kategori = input("Kategori: ").title()
        harga = input_angka("Harga: ")
        stok = input_angka("Stok: ")

        new_obat = {
            "id": generate_id("O", obat_list),
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "stok": stok,
            "terjual": 0
        }

        obat_list.append(new_obat)
        print(f"Obat berhasil ditambahkan dengan ID {new_obat['id']}")

        # VALIDASI y/n
        while True:
            lagi = input("Tambah obat lagi? (y/n): ").lower()
            if lagi in ["y", "n"]:
                break
            else:
                print("⚠ Input tidak valid! Hanya boleh y atau n.")

        if lagi == "n":
            print("Kembali ke menu utama.")
            break


def lihat_obat():
    if not obat_list:
        print("Belum ada data obat.")
        return

    # Lebar tiap kolom
    lebar_id = 6
    lebar_nama = 22
    lebar_kategori = 15
    lebar_harga = 10
    lebar_stok = 8
    lebar_terjual = 8

    # Garis horizontal
    garis = "+" + "-"*lebar_id + "+" + "-"*lebar_nama + "+" + "-"*lebar_kategori + "+" + "-"*lebar_harga + "+" + "-"*lebar_stok + "+" + "-"*lebar_terjual + "+"

    print("\n" + "+" + "-"*(len(garis)-2) + "+")
    print("|" + "DATA OBAT".center(len(garis)-2) + "|")
    print(garis)

    # Header
    print(
        "|"
        + "ID".center(lebar_id) + "|"
        + "Nama Obat".center(lebar_nama) + "|"
        + "Kategori".center(lebar_kategori) + "|"
        + "Harga".center(lebar_harga) + "|"
        + "Stok".center(lebar_stok) + "|"
        + "Terjual".center(lebar_terjual) + "|"
    )

    print(garis)

    # Isi Data
    for o in obat_list:
        print(
            "|"
            + o["id"].center(lebar_id) + "|"
            + o["nama"].ljust(lebar_nama) + "|"
            + o["kategori"].ljust(lebar_kategori) + "|"
            + str(o["harga"]).rjust(lebar_harga) + "|"
            + str(o["stok"]).center(lebar_stok) + "|"
            + str(o["terjual"]).center(lebar_terjual) + "|"
        )

    print(garis)


def update_obat():
    id_obat = input("Masukkan ID Obat: ").upper()
    obat = cari_data(obat_list, "id", id_obat)

    if not obat:
        print("Obat tidak ditemukan.")
        return

    while True:
        print("\n=== UPDATE DATA OBAT ===")
        print(f"Nama     : {obat['nama']}")
        print(f"Kategori : {obat['kategori']}")
        print(f"Harga    : {obat['harga']}")
        print(f"Stok     : {obat['stok']}")

        print("\n1. Update Nama")
        print("2. Update Kategori")
        print("3. Update Harga")
        print("4. Update Stok")
        print("5. Selesai")

        # VALIDASI PILIHAN 1-5
        while True:
            pilihan = input("Pilih menu update (1-5): ")
            if pilihan in ["1", "2", "3", "4", "5"]:
                break
            print("Pilihan tidak valid! Harus pilih angka 1-5.")

        if pilihan == "1":
            nama_baru = input("Nama baru (Enter untuk skip): ").title()
            if nama_baru != "":
                obat["nama"] = nama_baru
                print("Nama berhasil diperbarui.")
            else:
                print("Nama tidak diubah.")

        elif pilihan == "2":
            kategori_baru = input("Kategori baru (Enter untuk skip): ").title()
            if kategori_baru != "":
                obat["kategori"] = kategori_baru
                print("Kategori berhasil diperbarui.")
            else:
                print("Kategori tidak diubah.")

        elif pilihan == "3":
            while True:
                harga_input = input("Harga baru (Enter untuk skip): ")
                if harga_input == "":
                    print("Harga tidak diubah.")
                    break
                try:
                    harga_baru = int(harga_input)
                    if harga_baru >= 0:
                        obat["harga"] = harga_baru
                        print("Harga berhasil diperbarui.")
                        break
                    else:
                        print("Harga tidak boleh negatif.")
                except ValueError:
                    print("Input harus angka.")

        elif pilihan == "4":
            while True:
                stok_input = input("Stok baru (Enter untuk skip): ")
                if stok_input == "":
                    print("Stok tidak diubah.")
                    break
                try:
                    stok_baru = int(stok_input)
                    if stok_baru >= 0:
                        obat["stok"] = stok_baru
                        print("Stok berhasil diperbarui.")
                        break
                    else:
                        print("Stok tidak boleh negatif.")
                except ValueError:
                    print("Input harus angka.")

        elif pilihan == "5":
            print("Selesai update.")
            break

        # VALIDASI y/n
        while True:
            lagi = input("\nIngin update field lain? (y/n): ").lower()
            if lagi in ["y", "n"]:
                break
            print("Input tidak valid! Hanya boleh y atau n.")

        if lagi == "n":
            print("Selesai update.")
            break


def hapus_obat():
    if not obat_list:
        print("Tidak ada data obat untuk dihapus.")
        return

    # Tampilkan daftar obat dulu
    print("\n=== DAFTAR OBAT ===")

    lebar_id = 6
    lebar_nama = 22
    lebar_kategori = 15
    lebar_harga = 10
    lebar_stok = 8
    lebar_terjual = 8

    garis = "+" + "-"*lebar_id + "+" + "-"*lebar_nama + "+" + "-"*lebar_kategori + "+" + "-"*lebar_harga + "+" + "-"*lebar_stok + "+" + "-"*lebar_terjual + "+"

    print(garis)
    print(
        "|"
        + "ID".center(lebar_id) + "|"
        + "Nama Obat".center(lebar_nama) + "|"
        + "Kategori".center(lebar_kategori) + "|"
        + "Harga".center(lebar_harga) + "|"
        + "Stok".center(lebar_stok) + "|"
        + "Terjual".center(lebar_terjual) + "|"
    )
    print(garis)

    for o in obat_list:
        print(
            "|"
            + o["id"].center(lebar_id) + "|"
            + o["nama"].center(lebar_nama) + "|"
            + o["kategori"].center(lebar_kategori) + "|"
            + str(o["harga"]).center(lebar_harga) + "|"
            + str(o["stok"]).center(lebar_stok) + "|"
            + str(o["terjual"]).center(lebar_terjual) + "|"
        )

    print(garis)

    # Validasi ID
    while True:
        id_obat = input("Masukkan ID Obat yang ingin dihapus: ").upper()
        obat = cari_data(obat_list, "id", id_obat)

        if obat:
            break
        else:
            print("ID tidak ditemukan! Silakan masukkan ID yang benar.")

    # Validasi konfirmasi
    while True:
        konfirmasi = input("Yakin hapus? (y/n): ").lower()
        if konfirmasi in ["y", "n"]:
            break
        else:
            print("Input tidak valid! Hanya boleh y atau n.")

    if konfirmasi == "y":
        obat_list.remove(obat)
        print("Obat berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


# =====================================================
# CRUD CUSTOMER
# =====================================================

def tambah_customer():
    while True:
        print("\n=== TAMBAH CUSTOMER ===")

        # VALIDASI NAMA (HANYA HURUF & SPASI)
        while True:
            nama = input("Nama Customer: ").strip()
            
            if nama.replace(" ", "").isalpha():
                nama = nama.title()
                break
            else:
                print("Nama hanya boleh huruf dan spasi! Tidak boleh angka atau simbol.")

        # VALIDASI NO HP (HANYA ANGKA)
        while True:
            no_hp = input("No HP: ").strip()
            
            if no_hp.isdigit():
                break
            else:
                print("No HP hanya boleh angka!")

        new_customer = {
            "id": generate_id("C", customer_list),
            "nama": nama,
            "no_hp": no_hp,
            "total_belanja": 0
        }

        customer_list.append(new_customer)
        print(f"Customer berhasil ditambahkan dengan ID {new_customer['id']}")

        # VALIDASI y/n
        while True:
            lagi = input("Tambah customer lagi? (y/n): ").lower()
            if lagi in ["y", "n"]:
                break
            else:
                print("⚠ Input tidak valid! Hanya boleh y atau n.")

        if lagi == "n":
            print("Kembali ke menu utama.")
            break


def lihat_customer():
    print("\n" + "="*70)
    print(f"{'ID':<6}{'Nama':<20}{'No HP':<15}{'Total Belanja':<15}")
    print("="*70)

    for c in customer_list:
        print(f"{c['id']:<6}{c['nama']:<20}{c['no_hp']:<15}{c['total_belanja']:<15}")

    print("="*70)


# =====================================================
# TRANSAKSI
# =====================================================

def transaksi():
    print("\n=== TRANSAKSI PENJUALAN ===")

    # =========================
    # TAMPILKAN DATA CUSTOMER
    # =========================
    if not customer_list:
        print("Belum ada customer.")
        return

    print("\n--- DAFTAR CUSTOMER ---")
    lebar_id = 6
    lebar_nama = 20
    lebar_hp = 15
    lebar_total = 15

    garis_c = "+" + "-"*lebar_id + "+" + "-"*lebar_nama + "+" + "-"*lebar_hp + "+" + "-"*lebar_total + "+"

    print(garis_c)
    print(
        "|"
        + "ID".center(lebar_id) + "|"
        + "Nama".center(lebar_nama) + "|"
        + "No HP".center(lebar_hp) + "|"
        + "Total Belanja".center(lebar_total) + "|"
    )
    print(garis_c)

    for c in customer_list:
        print(
            "|"
            + c["id"].center(lebar_id) + "|"
            + c["nama"].center(lebar_nama) + "|"
            + c["no_hp"].center(lebar_hp) + "|"
            + str(int(c["total_belanja"])).center(lebar_total) + "|"
        )

    print(garis_c)

    # =========================
    # VALIDASI ID CUSTOMER
    # =========================
    while True:
        id_customer = input("Masukkan ID Customer: ").upper()
        customer = cari_data(customer_list, "id", id_customer)
        if customer:
            break
        else:
            print("Customer tidak ditemukan! Masukkan ID yang benar.")

    # =========================
    # TAMPILKAN DATA OBAT
    # =========================
    if not obat_list:
        print("Belum ada data obat.")
        return

    print("\n--- DAFTAR OBAT ---")

    lebar_id = 6
    lebar_nama = 22
    lebar_kategori = 15
    lebar_harga = 10
    lebar_stok = 8

    garis_o = "+" + "-"*lebar_id + "+" + "-"*lebar_nama + "+" + "-"*lebar_kategori + "+" + "-"*lebar_harga + "+" + "-"*lebar_stok + "+"

    print(garis_o)
    print(
        "|"
        + "ID".center(lebar_id) + "|"
        + "Nama Obat".center(lebar_nama) + "|"
        + "Kategori".center(lebar_kategori) + "|"
        + "Harga".center(lebar_harga) + "|"
        + "Stok".center(lebar_stok) + "|"
    )
    print(garis_o)

    for o in obat_list:
        print(
            "|"
            + o["id"].center(lebar_id) + "|"
            + o["nama"].center(lebar_nama) + "|"
            + o["kategori"].center(lebar_kategori) + "|"
            + str(o["harga"]).center(lebar_harga) + "|"
            + str(o["stok"]).center(lebar_stok) + "|"
        )

    print(garis_o)

    # =========================
    # VALIDASI ID OBAT
    # =========================
    while True:
        id_obat = input("Masukkan ID Obat: ").upper()
        obat = cari_data(obat_list, "id", id_obat)
        if obat:
            break
        else:
            print("Obat tidak ditemukan! Masukkan ID yang benar.")

    # =========================
    # INPUT QTY
    # =========================
    qty = input_angka("Jumlah beli: ")

    if qty > obat["stok"]:
        print("Stok tidak mencukupi.")
        return

    total = qty * obat["harga"]

    # Diskon otomatis
    if total > 100000:
        total *= 0.10
        print("Diskon 10% diterapkan!")
    elif qty >= 10:
        total *= 0.5
        print("Diskon 5% diterapkan!")

    # Update data
    obat["stok"] -= qty
    obat["terjual"] += qty
    customer["total_belanja"] += total

    new_transaksi = {
        "id_transaksi": generate_transaksi_id(),
        "id_customer": id_customer,
        "id_obat": id_obat,
        "qty": qty,
        "total": total
    }

    transaksi_list.append(new_transaksi)

    print(f"Transaksi berhasil. Total bayar: {int(total)}")


# =====================================================
# LAPORAN
# =====================================================

def laporan():
    print("\n")

    # ======================
    # HITUNG TOTAL PENDAPATAN
    # ======================
    total_pendapatan = 0
    for t in transaksi_list:
        total_pendapatan += t["total"]

    # ======================
    # CARI OBAT TERLARIS 
    # ======================
    obat_text = "Belum ada data"
    if len(obat_list) > 0:
        obat_laris = obat_list[0]
        for o in obat_list:
            if o["terjual"] > obat_laris["terjual"]:
                obat_laris = o
        obat_text = obat_laris["nama"] + " (" + str(obat_laris["terjual"]) + " terjual)"

    # ======================
    # CARI CUSTOMER TERAKTIF 
    # ======================
    customer_text = "Belum ada data"
    if len(customer_list) > 0:
        customer_top = customer_list[0]
        for c in customer_list:
            if c["total_belanja"] > customer_top["total_belanja"]:
                customer_top = c
        customer_text = customer_top["nama"] + " (Total: " + str(int(customer_top["total_belanja"])) + ")"

    # ======================
    # CETAK TABEL
    # ======================
    lebar = 59

    print("+" + "-" * lebar + "+")
    print("|" + "LAPORAN PENJUALAN".center(lebar) + "|")
    print("+" + "-" * lebar + "+")

    print("|" + " Total Pendapatan ".ljust(22) + "|" + str(int(total_pendapatan)).center(lebar - 23) + "|")
    print("+" + "-" * lebar + "+")

    print("|" + " Obat Terlaris ".ljust(22) + "|" + obat_text.center(lebar - 23) + "|")
    print("+" + "-" * lebar + "+")

    print("|" + " Customer Teraktif ".ljust(22) + "|" + customer_text.center(lebar - 23) + "|")
    print("+" + "-" * lebar + "+")


# =====================================================
# MENU
# =====================================================

def menu():
    print("\n===== E-COMMERCE FARMASI RUMAH SAKIT =====")
    print("1. Tambah Obat")
    print("2. Lihat Obat")
    print("3. Update Obat")
    print("4. Hapus Obat")
    print("5. Tambah Customer")
    print("6. Lihat Customer")
    print("7. Transaksi")
    print("8. Laporan")
    print("9. Keluar")


# =====================================================
# MAIN PROGRAM LOOP
# =====================================================

while True:
    menu()

    # VALIDASI PILIHAN 1-9
    while True:
        pilihan = input("Pilih menu (1-9): ")
        if pilihan in ["1","2","3","4","5","6","7","8","9"]:
            break
        else:
            print("⚠ Menu tidak valid! Harus pilih angka 1 sampai 9.")

    if pilihan == "1":
        tambah_obat()
    elif pilihan == "2":
        lihat_obat()
    elif pilihan == "3":
        update_obat()
    elif pilihan == "4":
        hapus_obat()
    elif pilihan == "5":
        tambah_customer()
    elif pilihan == "6":
        lihat_customer()
    elif pilihan == "7":
        transaksi()
    elif pilihan == "8":
        laporan()
    elif pilihan == "9":
        print("Terima kasih telah menggunakan sistem.")
        break