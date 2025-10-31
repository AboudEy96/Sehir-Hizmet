class Taksi:

    def __init__(self, KM_MESAFE: 0.0, GUN_ZAMANI: str, HAFTA_SONU: bool):
        self.KM_MESAFE = KM_MESAFE
        self.GUN_ZAMANI = GUN_ZAMANI
        self.HAFTA_SONU = HAFTA_SONU



    def setZAMAN(self, gun: str):
        while True:
            try:
                self.GUN_ZAMANI = str(gun)
                if (gun == "day" or gun == "night"):
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


tak = Taksi(2.7, "day", False)
