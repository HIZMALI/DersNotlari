# Kullanıcıdan alınacak öğrenci notlarını saklamak için boş liste oluşturur.
notlar = []

# Beş öğrencinin notunu almak için döngüyü başlatır.
for sira in range(1, 6):
    # Kullanıcıdan ilgili öğrencinin notunu alır ve tam sayıya dönüştürür.
    puan = int(input(f"{sira}. öğrenci notu: "))

    # Girilen notu listenin sonuna ekler.
    notlar.append(puan)

# Notların toplamını hesaplar.
toplam = sum(notlar)

# Notların ortalamasını hesaplar.
ortalama = toplam / len(notlar)

# En yüksek notu bulur.
en_yuksek = max(notlar)

# En düşük notu bulur.
en_dusuk = min(notlar)

# Başarılı öğrenci sayısını tutacak sayacı sıfırlar.
basarili = 0

# Listedeki bütün notları sırayla dolaşır.
for not_degeri in notlar:
    # Not 50 veya üzerindeyse başarı koşulu sağlanır.
    if not_degeri >= 50:
        # Başarılı öğrenci sayısını bir artırır.
        basarili += 1

# Toplam öğrenci sayısından başarılı sayısını çıkararak başarısız sayısını bulur.
basarisiz = len(notlar) - basarili

# Rapor başlığını ekrana yazdırır.
print("--- SINIF RAPORU ---")

# Girilen not listesini ekrana yazdırır.
print("Notlar:", notlar)

# Öğrenci sayısını ekrana yazdırır.
print("Öğrenci sayısı:", len(notlar))

# Sınıf ortalamasını iki ondalık basamakla ekrana yazdırır.
print(f"Ortalama: {ortalama:.2f}")

# En yüksek notu ekrana yazdırır.
print("En yüksek:", en_yuksek)

# En düşük notu ekrana yazdırır.
print("En düşük:", en_dusuk)

# Başarılı öğrenci sayısını ekrana yazdırır.
print("Başarılı:", basarili)

# Başarısız öğrenci sayısını ekrana yazdırır.
print("Başarısız:", basarisiz)
