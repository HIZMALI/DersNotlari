yas = int(input("Yaş: "))  # Kullanıcıdan yaşı alır ve tam sayıya dönüştürür.
cevap = input("Öğrenci misiniz? (evet/hayir): ")  # Kullanıcıdan öğrenci durumunu metin olarak alır.
ogrenci_mi = cevap == "evet"  # Kullanıcının cevabını Boolean öğrenci bilgisine dönüştürür.
yas_uygun = yas >= 18  # Yaşın 18 veya üzerinde olup olmadığını kontrol eder.
etkinlige_uygun = yas_uygun and ogrenci_mi  # Yaş ve öğrenci koşullarının birlikte sağlanıp sağlanmadığını kontrol eder.
print(f"Yaş koşulu: {yas_uygun}")  # Yaş koşulunun sonucunu gösterir.
print(f"Öğrenci koşulu: {ogrenci_mi}")  # Öğrenci koşulunun sonucunu gösterir.
print(f"Etkinliğe uygunluk: {etkinlige_uygun}")  # İki koşulun birleşik sonucunu gösterir.
