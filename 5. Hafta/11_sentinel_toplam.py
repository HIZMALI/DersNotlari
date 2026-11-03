# Toplam değerini sıfırdan başlatır.
toplam = 0
# Kullanıcıdan ilk sayı değerini alır.
sayi = int(input("Sayı girin (bitirmek için 0): "))

# Kullanıcı 0 dışında bir sayı girdiği sürece tekrar eder.
while sayi != 0:
    # Girilen sayıyı mevcut toplamın üzerine ekler.
    toplam += sayi
    # Bir sonraki tur için kullanıcıdan yeni sayı alır.
    sayi = int(input("Sayı girin (bitirmek için 0): "))

# Kullanıcı 0 girdiğinde hesaplanan toplamı gösterir.
print("Toplam:", toplam)
