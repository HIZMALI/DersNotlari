# Kaç sayı alındığını takip edecek sayacı sıfırlar.
sayac = 0
# Negatif olmayan sayıların toplamını sıfırlar.
toplam = 0

# Beş sayı alınana kadar döngüyü sürdürür.
while sayac < 5:
    # Kullanıcıdan bir tam sayı alır.
    sayi = int(input("Sayı: "))
    # Girilen sayı adedini bir artırır.
    sayac += 1
    # Sayının negatif olup olmadığını kontrol eder.
    if sayi < 0:
        # Negatif sayı geldiğinde o turun kalanını atlar.
        continue
    # Negatif olmayan sayıyı toplamın üzerine ekler.
    toplam += sayi

# Negatif olmayan sayıların toplamını gösterir.
print("Negatif olmayan sayıların toplamı:", toplam)
