# Yedi günlük sıcaklık değerlerini liste olarak tanımlar.
sicakliklar = [18, 21, 24, 19, 27, 23, 20]

# Listenin en düşük sıcaklığını bulur.
en_dusuk = min(sicakliklar)

# Listenin en yüksek sıcaklığını bulur.
en_yuksek = max(sicakliklar)

# Sıcaklıkların toplamını gün sayısına bölerek ortalamayı hesaplar.
ortalama = sum(sicakliklar) / len(sicakliklar)

# En düşük sıcaklığı ekrana yazdırır.
print("En düşük:", en_dusuk)

# En yüksek sıcaklığı ekrana yazdırır.
print("En yüksek:", en_yuksek)

# Ortalama sıcaklığı iki ondalık basamakla ekrana yazdırır.
print(f"Ortalama: {ortalama:.2f}")
