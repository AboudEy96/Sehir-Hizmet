from src.Main.Elektrik.Elektrik import Elektrik
from src.Main.Taksi.Taksi import Taksi

# TAKSI
baslangic = 3.0
gunduz_tarife = 1.5
gece_tarife = 2.0

print(" Akıllı Şehir Hizmet Asistanına Hoş Geldiniz")
print("Bir hizmet seçin:")
print(" 1. Taksi Ücreti Hesaplayıcısı "
      ",\n 2. Elektrik Faturası Hesaplayıcısı\n ,"
      "3. Sağlık Kontrolü (BMI ve İdeal Kilo)")
selector = int(input())

if selector == 1:
    txi = Taksi()
    txi.TaksiSelected()

if (selector == 2):
    elk = Elektrik()
    elk.ElektrikSelect()
##txi.printInfo()1