# Kullanıcıdan analiz edilecek ham metni alır.
ham_metin = input("Analiz edilecek metin: ")

# Karşılaştırmaları kolaylaştırmak için metnin kenar boşluklarını temizler ve küçük harfe dönüştürür.
metin = ham_metin.strip().lower()

# Sesli harf sayısını tutacak sayacı sıfırlar.
sesli = 0

# Rakam karakteri sayısını tutacak sayacı sıfırlar.
rakam = 0

# Boşluk karakteri sayısını tutacak sayacı sıfırlar.
bosluk = 0

# Temizlenmiş metindeki bütün karakterleri tek tek dolaşır.
for karakter in metin:
    # Karakter Türkçe sesli harflerden biriyse bu koşula girer.
    if karakter in "aeıioöuü":
        # Sesli harf sayacını bir artırır.
        sesli += 1

    # Karakterin rakam olup olmadığını ayrı olarak kontrol eder.
    if karakter.isdigit():
        # Rakam sayacını bir artırır.
        rakam += 1

    # Karakterin boşluk olup olmadığını ayrı olarak kontrol eder.
    if karakter == " ":
        # Boşluk sayacını bir artırır.
        bosluk += 1

# Dilimlemede negatif adım kullanarak temizlenmiş metnin tersini oluşturur.
ters = metin[::-1]

# Metnin ters haliyle aynı olup olmadığını karşılaştırarak palindrom sonucunu üretir.
palindrom = metin == ters

# Temizlenmiş metnin toplam karakter sayısını ekrana yazdırır.
print(f"Karakter sayısı: {len(metin)}")

# Toplam sesli harf sayısını ekrana yazdırır.
print(f"Sesli harf: {sesli}")

# Toplam rakam karakteri sayısını ekrana yazdırır.
print(f"Rakam: {rakam}")

# Toplam boşluk sayısını ekrana yazdırır.
print(f"Boşluk: {bosluk}")

# Metnin ters çevrilmiş halini ekrana yazdırır.
print(f"Ters metin: {ters}")

# Palindrom kontrolünün Boolean sonucunu ekrana yazdırır.
print(f"Palindrom mu? {palindrom}")
