class RekeningBank:
    def __init__(self, nama, saldo):
        # nama dibuat PUBLIC (tanpa garis bawah), jadi bisa diakses dari luar
        self.nama = nama
        # saldo dibuat PRIVATE (diawali dua garis bawah), jadi tidak bisa diakses dari luar
        self.__saldo = saldo


# Membuat objek rekening Budi
akun_budi = RekeningBank("Budi", 1000000)

# Mengakses nama dari luar class -> BERHASIL karena public
print(f"Nama pemilik: {akun_budi.nama}")

# Mengakses saldo dari luar class -> ERROR karena private
try:
    print(f"Saldo Budi: {akun_budi.__saldo}")
except AttributeError as e:
    print(f"ERROR: {e}")