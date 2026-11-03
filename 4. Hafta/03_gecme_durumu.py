# Kullanıcıdan sınav puanını tam sayı olarak alır.
puan = int(input("Sınav puanı: "))

# Puan 50 veya üzerindeyse öğrenciyi başarılı kabul eder.
if puan >= 50:
    # Başarı koşulu sağlandığında bu mesajı gösterir.
    print("Başarılı")
else:
    # Başarı koşulu sağlanmadığında bu mesajı gösterir.
    print("Başarısız")

# Bu satır iki karar bloğunun dışında olduğu için her durumda çalışır.
print("Değerlendirme tamamlandı.")
