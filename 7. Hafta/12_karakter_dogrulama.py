# Kullanıcıdan öğrenci numarası benzeri bir değer alır.
numara = input("Öğrenci numarası: ").strip()

# Girilen değerin yalnızca rakam karakterlerinden oluşup oluşmadığını kontrol eder.
yalnizca_rakam = numara.isdigit()

# Girilen değerin tam olarak sekiz karakter olup olmadığını kontrol eder.
sekiz_hane = len(numara) == 8

# İki koşulu birlikte değerlendirerek genel geçerlilik sonucunu üretir.
gecerli = yalnizca_rakam and sekiz_hane

# Son doğrulama sonucunu ekrana yazdırır.
print(f"Geçerli öğrenci numarası mı? {gecerli}")
