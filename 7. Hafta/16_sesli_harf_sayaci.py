# Kullanıcıdan metin alır ve büyük-küçük harf farkını kaldırmak için küçük harfe dönüştürür.
metin = input("Metin: ").lower()

# Bulunan sesli harf sayısını tutacak sayacı sıfırlar.
sesli_sayisi = 0

# Metindeki bütün karakterleri tek tek dolaşır.
for karakter in metin:
    # O turdaki karakterin Türkçe sesli harflerden biri olup olmadığını kontrol eder.
    if karakter in "aeıioöuü":
        # Karakter sesliyse sayacı bir artırır.
        sesli_sayisi += 1

# Toplam sesli harf sayısını ekrana yazdırır.
print(f"Sesli harf sayısı: {sesli_sayisi}")
