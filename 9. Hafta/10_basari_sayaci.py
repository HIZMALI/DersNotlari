# Beş öğrencinin notlarını içeren listeyi oluşturur.
notlar = [70, 45, 82, 39, 90]

# Başarılı öğrenci sayısını tutmak için sayacı sıfırlar.
basarili = 0

# Listedeki her notu sırayla inceler.
for not_degeri in notlar:
    # Not 50 veya üzerindeyse öğrenciyi başarılı kabul eder.
    if not_degeri >= 50:
        # Başarılı öğrenci sayısını bir artırır.
        basarili += 1

# Başarılı öğrenci sayısını ekrana yazdırır.
print("Başarılı öğrenci sayısı:", basarili)

# Toplam öğrenci sayısından başarılı sayısını çıkararak başarısız sayısını hesaplar.
basarisiz = len(notlar) - basarili

# Başarısız öğrenci sayısını ekrana yazdırır.
print("Başarısız öğrenci sayısı:", basarisiz)
