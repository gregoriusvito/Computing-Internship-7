import math

global jumlah_sisi
class Kubus:
    jumlah_sisi = 6
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        luas = 6*self.sisi**2
        print(luas)

    def hitung_volume(self):
        volume = self.sisi**3
        print(volume)

class Balok:
    jumlah_sisi = 6
    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_luas(self):
        luas = 2 * (self.panjang*self.lebar + self.panjang*self.tinggi + self.lebar*self.tinggi)
        print(luas)

    def hitung_volume(self):
        volume = self.panjang*self.lebar*self.tinggi
        print(volume)

class Tabung:
    jumlah_sisi = 3
    def __init__(self,jari,tinggi):
        self.jari = jari
        self.tinggi = tinggi

    def hitung_luas(self):
        luas = (2 * math.pi * self.jari**2) + (math.pi * 2 * self.jari * self.tinggi)
        print("%.3f" % luas)

    def hitung_volume(self):
        volume = math.pi * self.jari**2 * self.tinggi
        print("%.3f" % volume)

class Kerucut:
    jumlah_sisi = 2
    def __init__(self,jari,tinggi):
        self.jari = jari
        self.tinggi = tinggi

    def hitung_luas(self):
        s = math.sqrt(self.tinggi**2 + self.jari**2)
        luas = math.pi * self.jari * (self.jari + s)
        print("%.3f" % luas)

    def hitung_volume(self):
        volume = (math.pi * self.jari**2 * self.tinggi)/3
        print("%.3f" % volume)

cube = Tabung(2,4)
print(cube.jumlah_sisi)