# Kullanıcıdan toplamanın biteceği üst sınırı alır ve tam sayıya dönüştürür.
n = int(input("Üst sınır: "))

# Sayıları biriktirmek için toplam değişkenini sıfırdan başlatır.
toplam = 0

# 1'den n değerine kadar olan bütün sayıları sırayla dolaşır.
for sayi in range(1, n + 1):
    # O turdaki sayıyı mevcut toplamın üzerine ekler.
    toplam += sayi

# Döngü tamamlandıktan sonra nihai toplamı gösterir.
print(f"1 ile {n} arasındaki sayıların toplamı: {toplam}")
