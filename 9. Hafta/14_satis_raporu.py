# Beş günlük satış değerlerini saklamak için boş liste oluşturur.
satislar = []

# Beş gün için kullanıcıdan satış verisi alır.
for gun in range(1, 6):
    # İlgili günün satış değerini kullanıcıdan alır ve float türüne dönüştürür.
    satis = float(input(f"{gun}. gün satışı: "))

    # Alınan satış değerini listeye ekler.
    satislar.append(satis)

# Toplam satış tutarını hesaplar.
toplam = sum(satislar)

# Ortalama satış tutarını hesaplar.
ortalama = toplam / len(satislar)

# En yüksek satış değerini bulur.
en_yuksek = max(satislar)

# En düşük satış değerini bulur.
en_dusuk = min(satislar)

# Toplam satış tutarını ekrana yazdırır.
print(f"Toplam satış: {toplam:.2f}")

# Ortalama satış tutarını ekrana yazdırır.
print(f"Ortalama satış: {ortalama:.2f}")

# En yüksek satış değerini ekrana yazdırır.
print(f"En yüksek satış: {en_yuksek:.2f}")

# En düşük satış değerini ekrana yazdırır.
print(f"En düşük satış: {en_dusuk:.2f}")
