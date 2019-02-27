import math

class segitiga:
    jumlah_sisi=3

class segiempat:
    jumlah_sisi=4

class samasisi(segitiga):
    def __init__(self,sisi,tinggi):
        self.sisi=sisi
        self.tinggi=tinggi

    def hitung_luas(self):
        print(self.sisi*self.tinggi/2)

    def hitung_keliling(self):
        print(self.sisi*self.jumlah_sisi)

class samakaki(segitiga):
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        print(self.alas*self.tinggi/2)

    def hitung_keliling(self):
        print(self.alas+((math.sqrt(math.exp(self.alas/2)+math.exp(self.tinggi)))*2))
        

class persegi(segiempat):
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        print(self.panjang*self.lebar)

    def hitung_keliling(self):
        print((self.panjang+self.lebar)*2)

class traperium(segiempat):
    def __init__(self,alas,tutup,tinggi):
        self.alas = alas
        self.tutup = tutup
        self.tinggi = tinggi

    def hitung_luas(self):
        print((self.alas+self.tutup)*self.tinggi/2)

    def hitung_keliling(self):
        print(self.alas+self.tutup+self.tinggi+(math.sqrt(math.exp(self.tinggi)+math.exp(self.alas-self.tutup))))
class jajargenjang(segiempat):
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def hitung_luas(self):
        print(self.alas*self.tinggi)

    def hitung_keliling(self):
        print((self.alas+self.tinggi)*2)
