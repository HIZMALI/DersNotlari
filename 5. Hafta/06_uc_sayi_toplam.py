# Kaç sayı alındığını takip edecek sayacı sıfırlar.
adet = 0
# Girilen sayıların toplamını tutacak değişkeni sıfırlar.
toplam = 0

# Üç sayı alınana kadar döngüyü sürdürür.
while adet < 3:
    # Kullanıcıdan tam sayı alır.
    sayi = int(input("Sayı: "))
    # Girilen sayıyı mevcut toplamın üzerine ekler.
    toplam += sayi
    # Alınan sayı adedini bir artırır.
    adet += 1

# Üç sayının toplamını ekrana yazdırır.
print("Toplam:", toplam)
