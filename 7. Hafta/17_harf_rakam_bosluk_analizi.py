# Kullanıcıdan analiz edilecek metni alır.
metin = input("Metin: ")

# Harf sayısını tutacak sayacı sıfırlar.
harf_sayisi = 0

# Rakam sayısını tutacak sayacı sıfırlar.
rakam_sayisi = 0

# Boşluk sayısını tutacak sayacı sıfırlar.
bosluk_sayisi = 0

# Metindeki bütün karakterleri sırayla dolaşır.
for karakter in metin:
    # O turdaki karakter yalnızca bir harfse bu koşula girer.
    if karakter.isalpha():
        # Harf sayacını bir artırır.
        harf_sayisi += 1
    # Karakter bir rakam karakteriyse bu koşula girer.
    elif karakter.isdigit():
        # Rakam sayacını bir artırır.
        rakam_sayisi += 1
    # Karakter normal bir boşluksa bu koşula girer.
    elif karakter == " ":
        # Boşluk sayacını bir artırır.
        bosluk_sayisi += 1

# Metnin toplam karakter sayısını ekrana yazdırır.
print(f"Toplam karakter: {len(metin)}")

# Bulunan harf sayısını ekrana yazdırır.
print(f"Harf: {harf_sayisi}")

# Bulunan rakam sayısını ekrana yazdırır.
print(f"Rakam: {rakam_sayisi}")

# Bulunan boşluk sayısını ekrana yazdırır.
print(f"Boşluk: {bosluk_sayisi}")
