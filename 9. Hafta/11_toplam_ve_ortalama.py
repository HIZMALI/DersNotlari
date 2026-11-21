# Dört ürün fiyatını içeren listeyi oluşturur.
fiyatlar = [25, 40, 15, 20]

# Listedeki bütün fiyatların toplamını hesaplar.
toplam = sum(fiyatlar)

# Toplamı eleman sayısına bölerek ortalamayı hesaplar.
ortalama = toplam / len(fiyatlar)

# Toplam fiyatı ekrana yazdırır.
print("Toplam:", toplam)

# Ortalama fiyatı iki ondalık basamakla ekrana yazdırır.
print(f"Ortalama: {ortalama:.2f}")
