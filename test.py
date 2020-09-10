# 1. telebe qeydiyyat et
lst = []


class telebe:

    def __init__(self, id, ad, soyad, yas, sinif, mekteb):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.mekteb = mekteb

    def goster(self):
        print("Qeydiyyat nomresi:", self.id, "|", "Adi:", self.ad, "|", "Soyadi:", self.soyad, "|", "Yasi:", self.yas,
              "|", "Sinifi:", self.sinif, "|", "Mektebi", self.mekteb)


def icra():
    print("Yeni Tələbə")
    telebe.id = int(input("Telebe ID: "))
    telebe.ad = input("Telebenin adi: ")
    telebe.soyad = input("Telebenin soyadi: ")
    telebe.yas = input("Telebenin yasi: ")
    telebe.sinif = input("Telebenin sinifi: ")
    telebe.mekteb = input("Telebenin mekteb: ")
    telebe1 = telebe(telebe.id, telebe.ad, telebe.soyad, telebe.yas, telebe.sinif, telebe.mekteb)
    telebe1.goster()
    lst.append(telebe1)

def mekteb():# mektebe gore telebeleri cixart
    print("--Bir mektebde oxuyan teleblerin adi soyadi siyahisi---")
    b = input("mektebini yaz:")
    for i in lst:
        if i.mekteb == b:
            print("Adi:", i.ad, "Soyadi:", i.soyad)

def id():
    liste = []
    a = int(input("id-ni yaz:"))
    for i in lst:
        if i.id == a:
            liste.append(i)
    return liste

def telebeSil():
    silTelebe = int(input("silinecek id-ni yaz:"))
    silinecekObyekt = 0
    for i in lst:
        if i.id == silTelebe:
            silinecekObyekt = i
    lst.remove(silinecekObyekt)
    print("qalan telebeler:")
    for i in lst:
        print(i.ad, i.soyad)

def sinif():
    c = input("sinifini yaz:")
    for i in lst:
        if i.sinif == c:
            print(i.ad, i.soyad)

def yas():
    d = input("yasini yaz:")
    for i in lst:
        if i.yas == d:
            print(i.ad, i.soyad)

def idGore():
    e = int(input("id-ni yaz:"))
    for i in lst:
        if i.id == e:
            print("Ad:", i.ad, "Soyad:", i.soyad, "Yas:", i.yas, "Sinif:", i.sinif, "Mekteb:", i.mekteb)




# Komanda nomrelerine gore input gir
icraEt = int(input("Komand nomresini gir :"))
while icraEt == 1 or icraEt == 2 or icraEt == 3 or icraEt == 4 or icraEt == 5 or icraEt == 6 or icraEt == 7:

    if icraEt == 1:
        icra()
    elif icraEt == 2:#mektebe gore sirala
        mekteb()
    elif icraEt == 3:  # id-e gore datalari cixar
        yenilist = id()
        for i in yenilist:
            print(i.ad, i.soyad)
    elif icraEt == 4:  # telebe sil
        telebeSil()
    elif icraEt == 5: #sinife gore ad soyad yaz
        sinif()
    elif icraEt == 6:#yasa gore
        yas()
    elif icraEt == 7:  #adi soyadi yasi sinif ve mektebini yazdir
        idGore()

    icraEt = int(input("Komand nomresini gir :"))
print("Proqram bitdi")