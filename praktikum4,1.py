# Membuat class (cetakan) bernama Siswa
class Siswa:
    # Constructor: dijalankan otomatis saat objek Siswa dibuat
    def __init__(self, nama, nilai):
        # Atribut PUBLIC: nama siswa, bisa diakses dari luar
        self.nama = nama
        # Atribut PRIVATE (dua garis bawah): diberi nilai awal 0 dulu
        self.__nilai = 0
        # Nilai asli dari parameter dikirim lewat setter supaya diperiksa dulu
        self.set_nilai(nilai)

    # GETTER: Hanya untuk 'membaca'
    def get_nilai(self):
        # Menampilkan pesan bahwa getter sedang dipakai
        print(f"(Akses getter untuk {self.nama})")
        # Mengembalikan nilai private ke pemanggil
        return self.__nilai

    # SETTER: 'Satpam' untuk 'menulis'
    def set_nilai(self, nilai_baru):
        # Menampilkan pesan bahwa setter sedang dipakai
        print(f"(Akses setter untuk {self.nama} dengan nilai {nilai_baru})")
        # Memeriksa apakah nilai ada di antara 0 sampai 100
        if 0 <= nilai_baru <= 100:
            # Valid -> nilai disimpan
            self.__nilai = nilai_baru
            print("-> Nilai berhasil diupdate.")
        else:
            # Tidak valid -> nilai ditolak, nilai lama tetap aman
            print(f"-> Gagal! Nilai {nilai_baru} tidak valid. Harus antara 0-100.")


# Membuat objek budi dengan nilai 70 (langsung diperiksa oleh setter)
budi = Siswa("Budi", 70)

# Mengubah nilai menjadi 95 -> valid, jadi berhasil
budi.set_nilai(95)

# Mencoba mengubah nilai menjadi 105 -> tidak valid, jadi ditolak
budi.set_nilai(105)

# Membaca nilai lewat getter, lalu menampilkannya
print(f"Nilai Budi sekarang: {budi.get_nilai()}")