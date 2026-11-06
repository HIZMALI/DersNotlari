# Kullanıcıdan bir ad alır ve string olarak saklar.
ad = input("Adınız: ")

# Girilen adın toplam karakter sayısını hesaplar.
uzunluk = len(ad)

# Girilen adın ilk karakterini alır.
ilk_karakter = ad[0]

# Girilen adın son karakterini alır.
son_karakter = ad[-1]

# Metin uzunluğunu ekrana yazdırır.
print(f"Uzunluk: {uzunluk}")

# İlk karakteri ekrana yazdırır.
print(f"İlk karakter: {ilk_karakter}")

# Son karakteri ekrana yazdırır.
print(f"Son karakter: {son_karakter}")
