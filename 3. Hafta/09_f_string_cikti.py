ad = input("Adınız: ")  # Kullanıcıdan ad bilgisini alır.
puan = float(input("Puanınız: "))  # Kullanıcıdan puanı alır ve ondalıklı sayıya dönüştürür.
gecme_kosulu = puan >= 50  # Puanın 50 veya üzerinde olup olmadığını kontrol eder.
print(f"Öğrenci: {ad}")  # Kullanıcının adını etiketli biçimde gösterir.
print(f"Puan: {puan:.2f}")  # Puanı iki ondalık basamakla biçimlendirerek gösterir.
print(f"50 ve üzeri mi? {gecme_kosulu}")  # Boolean koşul sonucunu f-string içinde gösterir.
