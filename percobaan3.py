# Membuat class (cetakan) bernama Mobil
class Mobil:

    # ATRIBUT CLASS: dimiliki oleh class, nilainya dipakai bersama oleh semua objek
    # Dipakai untuk menghitung berapa mobil yang sudah dibuat
    total_mobil_dibuat = 0

    # Constructor: dijalankan otomatis setiap kali objek Mobil baru dibuat
    def __init__(self, nama):
        # ATRIBUT OBJEK: setiap mobil punya nama sendiri-sendiri
        self.nama = nama
        # Setiap ada mobil baru dibuat, hitungan total bertambah 1
        Mobil.total_mobil_dibuat += 1

    # METHOD OBJEK: dipanggil lewat objek (contoh: avanza.nyalakan_mesin())
    def nyalakan_mesin(self):
        # Menampilkan pesan bahwa mesin mobil ini menyala
        print(f"Mesin {self.nama} menyala!")

    # Penanda bahwa method di bawahnya adalah CLASS METHOD
    @classmethod
    # cls berarti class itu sendiri (Mobil), bukan objek tertentu
    def get_total_produksi(cls):
        # Menampilkan jumlah total mobil yang sudah dibuat
        print(f"Pabrik telah memproduksi {cls.total_mobil_dibuat} unit mobil.")


# Memanggil class method sebelum ada mobil dibuat -> hasilnya 0
Mobil.get_total_produksi()

# Menampilkan garis pembuka
print("--- Membuat mobil ---")
# Membuat objek pertama, total_mobil_dibuat menjadi 1
avanza = Mobil("Avanza")
# Membuat objek kedua, total_mobil_dibuat menjadi 2
xenia = Mobil("Xenia")
# Menampilkan garis penutup
print("---------------------")

# Memanggil class method lagi -> sekarang hasilnya 2
Mobil.get_total_produksi()