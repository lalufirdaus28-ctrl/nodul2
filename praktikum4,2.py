# Membuat class (cetakan) bernama Siswa
class Siswa:
    # Constructor: dijalankan otomatis saat objek Siswa dibuat
    def __init__(self, nama, nilai):
        # Atribut PUBLIC: nama siswa
        self.nama = nama
        # Terlihat seperti mengisi atribut biasa, tapi karena ada @nilai.setter,
        # baris ini OTOMATIS memanggil setter (nilai diperiksa dulu)
        self.nilai = nilai

    # 1. GETTER: @property mengubah method ini agar bisa dipanggil seperti atribut
    @property
    def nilai(self):
        # Menampilkan pesan bahwa getter sedang dipakai
        print("(Memanggil getter @property)")
        # Mengembalikan nilai private yang tersimpan
        return self.__nilai

    # 2. SETTER: dipanggil otomatis setiap kali ada yang menulis "objek.nilai = ..."
    # Namanya harus sama dengan nama getter (nilai)
    @nilai.setter
    def nilai(self, nilai_baru):
        # Menampilkan pesan bahwa setter sedang dipakai
        print(f"(Memanggil setter @nilai.setter dengan nilai {nilai_baru})")

        # Validasi ('satpam'): nilai harus antara 0 sampai 100
        if 0 <= nilai_baru <= 100:
            # Valid -> disimpan ke atribut private __nilai
            self.__nilai = nilai_baru
            print("-> Nilai berhasil diupdate.")
        else:
            # Tidak valid -> ditolak, nilai lama tetap aman
            print(f"-> Gagal! Nilai {nilai_baru} tidak valid.")


# --- Mari kita coba cara baru ---
# Membuat objek susi dengan nilai 80 -> setter dipanggil, nilai valid
susi = Siswa("Susi", 80)

# Garis pemisah supaya output mudah dibaca
print("-" * 20)

# A. Mengubah nilai: ditulis seperti atribut biasa, tapi yang jalan adalah SETTER
# 101 di luar rentang 0-100, jadi ditolak (nilai tetap 80)
susi.nilai = 101

print("-" * 20)

# Mengubah nilai ke 90 -> valid, jadi berhasil disimpan
susi.nilai = 90

print("-" * 20)

# B. Membaca nilai: ditulis seperti atribut biasa, tapi yang jalan adalah GETTER
print(f"Nilai Susi sekarang: {susi.nilai}")