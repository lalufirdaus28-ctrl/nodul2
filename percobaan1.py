# Membuat class bernama Hero
class Hero:

    # Variabel class PUBLIC: bisa diakses dari luar lewat Hero.jumlah
    jumlah = 0
    # Variabel class PRIVATE (dua garis bawah): tidak bisa diakses langsung dari luar
    __privateJumlah = 0

    # Constructor: dijalankan otomatis saat objek Hero dibuat
    def __init__(self, name, health):
        # Atribut objek PUBLIC: nama hero
        self.name = name
        # Atribut objek PUBLIC: darah hero
        self.health = health

        # Atribut objek PRIVATE: namanya diubah Python menjadi _Hero__private
        self.__private = 'private'
        # TYPO! Seharusnya "self", bukan "selt" -> inilah penyebab error
        selt.__protected = 'protected'

# Membuat objek hero_1 (error terjadi di baris ini)
hero_1 = Hero('Atsu', 100)

# Menampilkan semua atribut milik objek hero_1
print(hero_1.__dict__)
# Menampilkan semua isi milik class Hero
print(Hero.__dict__)
# Mencoba mengakses variabel private class dari luar
print(Hero.__privateJumlah)