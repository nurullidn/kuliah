class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def belajar(self):
        print(self.nama, "sedang belajar ASD")

manusia1 = Manusia("Bubu", 2)

print(manusia1.umur)

manusia1.belajar()