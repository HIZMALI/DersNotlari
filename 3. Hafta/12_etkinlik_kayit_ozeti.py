ad_soyad = input("Ad soyad: ")  # Kullanıcıdan katılımcının ad ve soyad bilgisini alır.
yas = int(input("Yaş: "))  # Kullanıcıdan yaşı alır ve tam sayıya dönüştürür.
ogrenci_cevabi = input("Öğrenci misiniz? (evet/hayir): ")  # Kullanıcıdan öğrenci durumunu metin olarak alır.
bilet_fiyati = float(input("Bilet fiyatı: "))  # Kullanıcıdan bir biletin fiyatını alır ve float türüne dönüştürür.
bilet_sayisi = int(input("Bilet sayısı: "))  # Kullanıcıdan alınacak bilet sayısını alır ve int türüne dönüştürür.
toplam_ucret = bilet_fiyati * bilet_sayisi  # Bilet fiyatı ile bilet sayısını çarparak toplam ücreti hesaplar.
yas_uygun = yas >= 18  # Katılımcının 18 yaş veya üzerinde olup olmadığını kontrol eder.
ogrenci_mi = ogrenci_cevabi == "evet"  # Öğrenci cevabını True veya False değerine dönüştürür.
ogrenci_indirimi_kosulu = yas_uygun and ogrenci_mi  # Yaş ve öğrenci koşullarının aynı anda sağlanıp sağlanmadığını kontrol eder.
bes_yuz_esigi = toplam_ucret >= 500  # Toplam ücretin 500 TL veya üzerinde olup olmadığını kontrol eder.
print(f"Katılımcı: {ad_soyad}")  # Katılımcının ad ve soyadını gösterir.
print(f"Toplam ücret: {toplam_ucret:.2f} TL")  # Toplam bilet ücretini iki ondalık basamakla gösterir.
print(f"18 yaş veya üzeri mi? {yas_uygun}")  # Yaş koşulunun Boolean sonucunu gösterir.
print(f"Öğrenci mi? {ogrenci_mi}")  # Öğrenci durumunun Boolean sonucunu gösterir.
print(f"Öğrenci indirimi koşulu: {ogrenci_indirimi_kosulu}")  # Birleşik öğrenci indirimi koşulunu gösterir.
print(f"500 TL eşiği: {bes_yuz_esigi}")  # Toplam ücret eşik koşulunun Boolean sonucunu gösterir.
