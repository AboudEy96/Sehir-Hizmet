from logging import NullHandler
from src.Taksi.Taksi import Taksi

baslangic = 3.0
gunduz_tarife = 1.5
gece_tarife = 2.0

km = float(input("Mesafeyi girin (km):"))

gun = str(input("Günün zamanını girin (day/night): "))

hf_sonuINPUT = input(" Hafta sonu mu (Yes/No): ").strip().lower()
hf_sonu = hf_sonuINPUT.strip().lower() in ["yes", "y", "true", "t"]
txi = Taksi(km,gun,hf_sonu)


def Hesabla():
    if txi.GUN_ZAMANI == "day":
        tarife = (baslangic + gunduz_tarife * txi.KM_MESAFE)
        ucret = tarife * 1.1 if txi.HAFTA_SONU else tarife
        print("Toplam ücretiniz: $", ucret)

    else:
        if txi.GUN_ZAMANI == "night":
         tarife = (baslangic + gece_tarife * txi.KM_MESAFE)
         ucret = tarife * 1.1 if txi.HAFTA_SONU else tarife
         print("Toplam ücretiniz: $", ucret)


Hesabla()
##txi.printInfo()