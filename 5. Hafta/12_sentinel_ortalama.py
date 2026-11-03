# Sayıların toplamını tutacak değişkeni sıfırlar.
toplam = 0
# Kaç sayı girildiğini takip edecek sayacı sıfırlar.
adet = 0
# Kullanıcıdan ilk sayı değerini alır.
sayi = int(input("Sayı girin (bitirmek için 0): "))

# Kullanıcı 0 dışında bir sayı girdiği sürece tekrar eder.
while sayi != 0:
    # Girilen sayıyı toplamın üzerine ekler.
    toplam += sayi
    # Geçerli sayı adedini bir artırır.
    adet += 1
    # Bir sonraki tur için yeni sayı alır.
    sayi = int(input("Sayı girin (bitirmek için 0): "))

# En az bir sayı girilip girilmediğini kontrol eder.
if adet > 0:
    # Toplamı sayı adedine bölerek ortalamayı hesaplar.
    ortalama = toplam / adet
    # Hesaplanan ortalamayı ekrana yazdırır.
    print("Ortalama:", ortalama)
else:
    # Hiç sayı girilmediğinde kullanıcıyı bilgilendirir.
    print("Ortalama hesaplamak için sayı girilmedi.")
