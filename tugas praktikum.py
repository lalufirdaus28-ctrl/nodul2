# Membuat class (cetakan) bernama Hero untuk game
class Hero:
    # VARIABEL CLASS PRIVATE: dipakai bersama semua Hero, untuk menghitung total Hero yang dibuat
    __jumlah = 0

    # Constructor: dijalankan otomatis saat Hero baru dibuat
    def __init__(self, nama, health, attPower, armor):
        # Nama hero, dibuat PRIVATE (dua garis bawah) supaya tidak bisa diubah dari luar
        self.__name = nama

        # BASE STATS: nilai dasar hero, tidak pernah berubah walaupun level naik
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor

        # Hero baru selalu mulai dari level 1
        self.__level = 1
        # Hero baru mulai dengan EXP 0
        self.__exp = 0

        # ATRIBUT DINAMIS: dihitung dari base stats x level, jadi ikut naik saat level naik
        # Darah maksimal
        self.__healthMax = self.__healthStandar * self.__level
        # Kekuatan serangan
        self.__attPower = self.__attPowerStandar * self.__level
        # Pertahanan (armor)
        self.__armor = self.__armorStandar * self.__level

        # Darah saat ini, awalnya penuh (sama dengan darah maksimal)
        self.__health = self.__healthMax

        # Setiap ada Hero baru, jumlah total Hero bertambah 1
        Hero.__jumlah += 1

    # GETTER gainEXP: sengaja dikosongkan (pass), hanya syarat agar setter bisa dibuat
    @property
    def gainEXP(self):
        pass

    # SETTER gainEXP: dipanggil otomatis saat menulis "hero.gainEXP = angka"
    @gainEXP.setter
    def gainEXP(self, addEXP):
        # Menambahkan EXP baru ke EXP yang sudah dimiliki
        self.__exp += addEXP

        # Selama EXP sudah 100 atau lebih, hero naik level
        # (pakai while supaya bisa naik lebih dari 1 level sekaligus)
        while self.__exp >= 100:
            # Menampilkan pesan level up
            print(f"{self.__name} level up")
            # Level naik 1
            self.__level += 1
            # EXP dikurangi 100 (sisa EXP tetap disimpan)
            self.__exp -= 100

            # Hitung ulang semua atribut dinamis berdasarkan level yang baru
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

            # Darah saat ini diisi penuh sesuai darah maksimal yang baru
            self.__health = self.__healthMax

    # Method attack: hero menyerang musuh
    def attack(self, musuh):
        # Setiap menyerang, hero mendapat 50 EXP lewat setter gainEXP
        self.gainEXP = 50

    # GETTER info (read-only): hanya bisa dibaca, tidak bisa diubah dari luar
    @property
    def info(self):
        # Mengembalikan teks status hero (\n = baris baru, \t = tab)
        return (f"{self.__name} level {self.__level}: \n"
                f"\thealth = {self.__health}/{self.__healthMax} \n"
                f"\tattack = {self.__attPower} \n"
                f"\tarmor = {self.__armor}")


# ===== Test case =====
# Membuat dua hero: slardar dan axe
slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
# Menampilkan status awal slardar (level 1)
print(slardar.info)

# Slardar menyerang 3 kali, tiap serangan dapat 50 EXP
slardar.attack(axe)   # EXP 50, belum level up
slardar.attack(axe)   # EXP 100, level up ke 2, EXP kembali 0
slardar.attack(axe)   # EXP 50, belum level up lagi

# Menampilkan status slardar setelah level 2
print(slardar.info)