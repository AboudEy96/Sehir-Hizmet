
tookDiscount = False
class Elektrik:
    def __init__(self, TUKETIM_KWH: float = None):
        self.TUKETIM_KWH = TUKETIM_KWH

    def setTUKETIM(self, kwh: float):
        while True:
            try:
                kwh = float(kwh)
                self.TUKETIM_KWH = kwh
                break
            except ValueError:
                print("wrong number try: (xyz,b)")

    def ElektrikSelect(self):
            kwh = float(input("Elektrik birimlerini girin: "))
            self.setTUKETIM(kwh)
            self.ElektrikHesabla()

    def ElektrikHesabla(self):
            global tookDiscount

            if not tookDiscount:

                if self.TUKETIM_KWH <= 100.0:
                    ucret = self.TUKETIM_KWH * 0.50
                else:
                    ucret = (100.0 * 0.50) + ((self.TUKETIM_KWH - 100.0) * 0.75)
                tookDiscount = True
                print("Toplam fatura after discount:", ucret)
            else:
               ucret = (self.TUKETIM_KWH * 0.75)
               tookDiscount = True
               if (self.TUKETIM_KWH > 200.0):
                 ucret = (self.TUKETIM_KWH * 1.20)

            if ucret > 100:
                ucret = ucret * 1.05
            print("Toplam fatura: ", ucret)
    def printInfo(self):
        print(" Tüketilen birim \t", self.TUKETIM_KWH)
