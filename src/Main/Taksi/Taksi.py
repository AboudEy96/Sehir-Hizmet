# TAKSI
baslangic = 3.0
gunduz_tarife = 1.5
gece_tarife = 2.0


class Taksi:

    def __init__(self, KM_MESAFE: float = None, GUN_ZAMANI: str = None, HAFTA_SONU: bool = None):
        self.KM_MESAFE = KM_MESAFE
        self.GUN_ZAMANI = GUN_ZAMANI
        self.HAFTA_SONU = HAFTA_SONU

    def setZAMAN(self, gun: str):
        while True:
            try:
                self.GUN_ZAMANI = str(gun)
                if gun in ["day", "night"]:
                    self.GUN_ZAMANI = gun
                break
            except ValueError:
                print("you should use string ( day , night )")

    def setHAFTA(self, hfsonu: bool):
        while True:
            try:
                self.HAFTA_SONU = bool(hfsonu)
                self.HAFTA_SONU = hfsonu
                break
            except ValueError:
                print("Hafta sonu true / false olmasi gerekiyor")

    def setKM(self, kmmesafe: 0.0):
        while True:
            try:
                kmmesafe = float(kmmesafe)
                self.KM_MESAFE = kmmesafe
                break
            except ValueError:
                print("wrong varible please use ( a.b )")

    def printInfo(self):
        print("Kilo Metre Mesafe: \t", self.KM_MESAFE)
        print("Gunun Zamani: \t", self.GUN_ZAMANI)
        print("HAFTA Sonu mu?: \t", self.HAFTA_SONU)

    def TaksiSelected(self):
        km = float(input("Mesafeyi girin (km):"))
        self.setKM(km)
        gun = str(input("Günün zamanını girin (day/night): "))
        self.setZAMAN(gun)
        hf_sonuINPUT = input(" Hafta sonu mu (Yes/No): ").strip().lower()
        hf_sonu = hf_sonuINPUT.strip().lower() in ["yes", "y", "true", "t"]
        self.setHAFTA(hf_sonu)
        self.TaksiHesabla()

    def TaksiHesabla(self):
        global baslangic, gunduz_tarife, gece_tarife

        if self.GUN_ZAMANI == "day":
            tarife = (baslangic + gunduz_tarife * self.KM_MESAFE)
            ucret = tarife * 1.1 if self.HAFTA_SONU else tarife
            print("Toplam ücretiniz: $", ucret)
        elif self.GUN_ZAMANI == "night":
            tarife = (baslangic + gece_tarife * self.KM_MESAFE)
            ucret = tarife * 1.1 if self.HAFTA_SONU else tarife
            print("Toplam ücretiniz: $", ucret)
