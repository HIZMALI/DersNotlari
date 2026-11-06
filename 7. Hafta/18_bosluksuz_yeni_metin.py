# Kullanıcıdan boşluk içerebilecek bir metin alır.
metin = input("Metin: ")

# Yeni karakterlerin biriktirileceği boş stringi oluşturur.
yeni_metin = ""

# Orijinal metindeki bütün karakterleri dolaşır.
for karakter in metin:
    # O turdaki karakter boşluk değilse yeni metne eklenmesine izin verir.
    if karakter != " ":
        # Boşluk olmayan karakteri yeni metnin sonuna ekler.
        yeni_metin += karakter

# Boşlukları çıkarılmış yeni metni ekrana yazdırır.
print(yeni_metin)
