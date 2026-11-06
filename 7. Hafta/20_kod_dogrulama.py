# Kullanıcıdan kontrol edilecek kodu alır ve kenar boşluklarını temizler.
kod = input("Kod: ").strip()

# Kodun toplam uzunluğunun altı karakter olup olmadığını kontrol eder.
uzunluk_dogru = len(kod) == 6

# Kod boş değilse ve ilk karakter A ise başlangıç koşulunu True yapar.
baslangic_dogru = len(kod) > 0 and kod[0].upper() == "A"

# İlk karakterden sonraki bölümün yalnızca rakamlardan oluşup oluşmadığını kontrol eder.
rakamlar_dogru = kod[1:].isdigit()

# Üç ayrı doğrulama sonucunun tamamının doğru olup olmadığını kontrol eder.
gecerli = uzunluk_dogru and baslangic_dogru and rakamlar_dogru

# Genel geçerlilik sonucunu ekrana yazdırır.
print(f"Kod geçerli mi? {gecerli}")
