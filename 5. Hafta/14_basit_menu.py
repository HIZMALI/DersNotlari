# Kullanıcı çıkış seçeneğini seçene kadar sürekli çalışan döngüyü başlatır.
while True:
    # Birinci menü seçeneğini ekrana yazdırır.
    print("1 - Merhaba de")
    # İkinci menü seçeneğini ekrana yazdırır.
    print("2 - Python mesajı göster")
    # Çıkış seçeneğini ekrana yazdırır.
    print("0 - Çıkış")
    # Kullanıcıdan menü seçimini alır.
    secim = input("Seçim: ")
    # Kullanıcının çıkış seçeneğini seçip seçmediğini kontrol eder.
    if secim == "0":
        # Döngüyü hemen sonlandırır.
        break
    # Kullanıcının birinci seçeneği seçip seçmediğini kontrol eder.
    elif secim == "1":
        # Merhaba mesajını ekrana yazdırır.
        print("Merhaba!")
    # Kullanıcının ikinci seçeneği seçip seçmediğini kontrol eder.
    elif secim == "2":
        # Python ile ilgili kısa mesajı ekrana yazdırır.
        print("Python öğrenmeye devam ediyoruz.")
    # Tanımlanan seçeneklerin dışında bir değer girildiğinde çalışır.
    else:
        # Geçersiz seçim mesajını gösterir.
        print("Geçersiz seçim.")

# Menü döngüsü sona erdiğinde kapanış mesajını gösterir.
print("Program kapatıldı.")
