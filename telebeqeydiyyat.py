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


# Komanda nomrelerine gore input gir
icraEt = int(input("Komand nomresini gir :"))
while icraEt == 1 or icraEt == 2 or icraEt == 3 or icraEt == 4 or icraEt == 5 or icraEt == 6 or icraEt == 7:

    if icraEt == 1:
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

    elif icraEt == 2:  # mektebe gore telebeleri cixart
        print("--Bir mektebde oxuyan teleblerin adi soyadi siyahisi---")
        b = input("mektebini yaz:")
        for i in lst:
            if i.mekteb == b:

                print("Adi:",i.ad, "Soyadi:", i.soyad)

    elif icraEt == 3:  # id-e gore datalari cixar
        a = int(input("id-ni yaz:"))
        for i in lst:
            if i.id == a:
                i.mebleg = 100
                print(i.ad, i.soyad, i.yas, i.sinif, i.mekteb)
    elif icraEt == 4:  # telebe sil
        silTelebe = int(input("silinecek id-ni yaz:"))
        silinecekObyekt = 0
        for i in lst:
            if i.id == silTelebe:
                silinecekObyekt = i
        lst.remove(silinecekObyekt)
        print("qalan telebeler:")
        for i in lst:
            print(i.ad, i.soyad)
    elif icraEt == 5:
        c = input("sinifini yaz:")
        for i in lst:
            if i.sinif == c:
                print(i.ad, i.soyad)
    elif icraEt == 6:
        d = input("yasini yaz:")
        for i in lst:
            if i.yas == d:
                print(i.ad, i.soyad)
    elif icraEt == 7:  # adi soyadi yasi sinif ve mektebini yazdir
        e = int(input("id-ni yaz:"))
        for i in lst:
            if i.id == e:
                print("Ad:",i.ad, "Soyad:",i.soyad, "Yas:",i.yas, "Sinif:", i.sinif, "Mekteb:", i.mekteb)

    icraEt = int(input("Komand nomresini gir :"))

print("Proqram bitdi")