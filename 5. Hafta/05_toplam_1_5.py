# Sayacı 1 değerinden başlatır.
sayac = 1
# Toplam değerini sıfırdan başlatır.
toplam = 0

# Sayaç 5 veya daha küçük olduğu sürece döngüyü sürdürür.
while sayac <= 5:
    # O anki sayaç değerini mevcut toplamın üzerine ekler.
    toplam += sayac
    # Sayaç değerini bir artırır.
    sayac += 1

# Hesaplanan toplamı ekrana yazdırır.
print("1 ile 5 arasındaki sayıların toplamı:", toplam)
