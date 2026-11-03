# Beş öğrencinin not toplamını tutmak için biriktiriciyi sıfırlar.
toplam = 0

# Başarılı öğrenci sayısını tutacak sayacı sıfırlar.
basarili = 0

# Başarısız öğrenci sayısını tutacak sayacı sıfırlar.
basarisiz = 0

# Beş öğrencinin notunu almak için döngüyü beş kez çalıştırır.
for sira in range(1, 6):
    # Kullanıcıdan öğrencinin notunu alır ve tam sayıya dönüştürür.
    notu = int(input(f"{sira}. öğrencinin notu: "))
    # Girilen notu toplam puanın üzerine ekler.
    toplam += notu
    # Notun başarı sınırı olan 50 veya üzerinde olup olmadığını kontrol eder.
    if notu >= 50:
        # Başarılı öğrenci sayısını bir artırır.
        basarili += 1
    else:
        # Başarısız öğrenci sayısını bir artırır.
        basarisiz += 1

# Beş öğrencinin toplam puanını beşe bölerek sınıf ortalamasını hesaplar.
ortalama = toplam / 5

# Hesaplanan sınıf ortalamasını iki ondalık basamakla gösterir.
print(f"Sınıf ortalaması: {ortalama:.2f}")

# Başarılı öğrenci sayısını gösterir.
print(f"Başarılı öğrenci: {basarili}")

# Başarısız öğrenci sayısını gösterir.
print(f"Başarısız öğrenci: {basarisiz}")
