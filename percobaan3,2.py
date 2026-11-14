# Membuat class (cetakan) bernama Kalkulator
class Kalkulator:

    # Constructor: dijalankan otomatis saat objek Kalkulator dibuat
    def __init__(self, nilai_awal):
        # ATRIBUT OBJEK: menyimpan nilai yang sedang dipegang kalkulator
        self.nilai = nilai_awal

    # METHOD OBJEK: memakai self, jadi bekerja pada data objek (self.nilai)
    def tambah(self, angka):
        # Menambahkan angka ke nilai milik objek ini (nilai = nilai + angka)
        self.nilai += angka
        # Mengembalikan nilai terbaru setelah ditambah
        return self.nilai

    # Penanda bahwa method di bawahnya adalah STATIC METHOD
    @staticmethod
    # Static method tidak memakai self maupun cls, jadi tidak butuh data objek/class
    def kali(a, b):
        # Mengembalikan hasil perkalian a dan b
        return a * b


# Membuat objek calc dengan nilai awal 10
calc = Kalkulator(10)
# Memanggil method objek: 10 + 5 = 15, lalu hasilnya ditampilkan
print(f"Hasil tambah: {calc.tambah(5)}")

# Memanggil static method langsung lewat nama class (tanpa membuat objek): 5 x 3 = 15
print(f"Hasil kali: {Kalkulator.kali(5, 3)}")