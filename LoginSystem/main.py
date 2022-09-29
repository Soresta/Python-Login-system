# ------------------------------------------------------------
import random

kullanicilar = ["akif", "kaan", "Musfettin"]
ogrenciNoListesi = []
ogrenciBilgileri = {}
tcList = []

tcVeAdListesi= {}
# ogrencii numarası verilcek kısım:
def kullaniciBilgi():
    for isim in kullanicilar:

        tc = random.randint(11111111111,99999999999)
        tcList.append(tc)

        ogrenciNo = random.randint(220000000, 229999999)
        while ogrenciNo in ogrenciNoListesi:
            ogrenciNo = random.randint(220000000, 229999999)
        ogrenciNoListesi.append(ogrenciNo)

        ogrenciBilgileri.update({tc: [isim, ogrenciNo]})
    print(ogrenciBilgileri)


kullaniciBilgi()




#----------------------------------------------------------------------
"""Oğrenci numarasını uutma kısmı"""
def sifreBul():
    while True:
        tcQ = int(input("Tc numaranızı giriniz :"))
        if tcQ in ogrenciBilgileri.keys():
            nameQ = input("Adınızı giriniz :")
            adi = ogrenciBilgileri.get(tcQ)

            if nameQ == adi[0]:
                sNumber = adi[1]
                print(f"Oğrenci numaranız {sNumber}")
                break

            else:
                print(f"Adınız girdiğiniz TC numarası ile uyuşmuyor, Lütfen tekrar deneyiniz! ")
        else:
            print("Bu TC numarasına bağlı bir öğrenci numarası bulunmamaktadır!")






# ----------------------------------------------------
# şifre oluşturma kısmı:
sifrelerListesi = []

# çalışıyor!
def sifreOlusturma():
    while True:
        sPasswordA = input("eğer öğrenci numarasını unuttuysanız 'E' tıklayın, Devam etmek için 'H' tuşuna basınız: ")
        if sPasswordA == "E":
            sifreBul()
        else:
            try:
                ogrenciNoSorgulama = int(input("Öğrenci numaranızı giriniz :"))
                if ogrenciNoSorgulama in ogrenciNoListesi:
                    sifren = input("Şifre oluştur: ")
                    sifrelerListesi.append(sifren)
                    print("Şifreniz :", sifren)
                    break
                else:
                    print("Ogrenci numaranızı yanlış girdiniz.")
            except(ValueError):
                print("Lütfen Rakamlardan oluşan öğrenci Numaranızı giriniz!")


sifreOlusturma()


print(tcList)

# --------------------------------------------------------------------------------
print("""#-------------------------Giriş Sistemi-------------------------#""")


# giriş ekranı
# giris sistemi:
def girisSistemi():
    while True:
        try:
            ogrenciNosorgulama = int(input("Öğrenci numaranızı giriniz :"))
            if ogrenciNosorgulama in ogrenciNoListesi:
                while True:
                    sifreniz = input("Şifrenizi giriniz :")
                    if sifreniz in sifrelerListesi:
                        print("Hoşgeldin", ogrenciBilgileri.get(ogrenciNosorgulama))
                        break
                    else:
                        print("Şifreniz hatalıdır tekrar deneyiniz!")
                break
            else:
                print("Ogrenci numaranız yanlıştır!, Tekrar giriniz")
        except(ValueError):
            print("Lütfen Rakamlardan oluşan öğrenci Numaranızı giriniz!")

girisSistemi()





