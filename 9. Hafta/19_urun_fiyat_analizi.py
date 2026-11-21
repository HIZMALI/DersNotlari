# Kullanıcıdan alınacak altı ürün fiyatını saklamak için boş liste oluşturur.
fiyatlar = []

# Altı kez fiyat girişi alınmasını sağlar.
for sira in range(1, 7):
    # Kullanıcıdan ilgili ürünün fiyatını alır ve float türüne dönüştürür.
    fiyat = float(input(f"{sira}. ürün fiyatı: "))

    # Girilen fiyatı listeye ekler.
    fiyatlar.append(fiyat)

# Bütün ürün fiyatlarının toplamını hesaplar.
toplam = sum(fiyatlar)

# Ortalama ürün fiyatını hesaplar.
ortalama = toplam / len(fiyatlar)

# En pahalı ürün fiyatını bulur.
en_pahali = max(fiyatlar)

# En ucuz ürün fiyatını bulur.
en_ucuz = min(fiyatlar)

# 100 TL üzerindeki ürün sayısını tutmak için sayacı sıfırlar.
yuz_ustu = 0

# Listedeki bütün fiyatları tek tek dolaşır.
for fiyat in fiyatlar:
    # Fiyat 100 TL'den büyükse koşulu sağlar.
    if fiyat > 100:
        # 100 TL üzerindeki ürün sayısını bir artırır.
        yuz_ustu += 1

# Rapor başlığını ekrana yazdırır.
print("--- FİYAT RAPORU ---")

# Toplam fiyatı iki ondalık basamakla ekrana yazdırır.
print(f"Toplam: {toplam:.2f} TL")

# Ortalama fiyatı iki ondalık basamakla ekrana yazdırır.
print(f"Ortalama: {ortalama:.2f} TL")

# En pahalı ürün fiyatını ekrana yazdırır.
print(f"En pahalı: {en_pahali:.2f} TL")

# En ucuz ürün fiyatını ekrana yazdırır.
print(f"En ucuz: {en_ucuz:.2f} TL")

# 100 TL üzerindeki ürün sayısını ekrana yazdırır.
print("100 TL üzeri ürün sayısı:", yuz_ustu)
