# Girilen notların toplamını tutmak için biriktiriciyi sıfırlar.
toplam = 0

# Beş öğrencinin notunu almak için döngüyü beş kez çalıştırır.
for sira in range(1, 6):
    # Kullanıcıdan ilgili öğrencinin notunu alır.
    notu = int(input(f"{sira}. öğrencinin notu: "))
    # Girilen notu toplam puanın üzerine ekler.
    toplam += notu

# Beş notun toplamını beşe bölerek ortalamayı hesaplar.
ortalama = toplam / 5

# Ortalamayı iki ondalık basamakla gösterir.
print(f"Sınıf ortalaması: {ortalama:.2f}")
