class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar


#Fungsi Menghitung Keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)
    
#Fungsi Menghitung Luas
    def hitung_luas(self):
        return self.panjang * self.lebar

#Fungsi Metode  str untuk menampilkan string object
    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


# Contoh penggunaan
persegi_panjang = PersegiPanjang(30, 45)
print(persegi_panjang)               # Persegi panjang, panjang 3 cm, dan lebar 2 cm
print("Keliling:", persegi_panjang.hitung_keliling(), "cm")   # Keliling: 10 cm
print("Luas:", persegi_panjang.hitung_luas(), "cm²")         # Luas: 6 cm²
