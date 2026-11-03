# Kullanıcının bakiyesini sıfırdan başlatır.
bakiye = 0.0

# Kullanıcı çıkış seçeneğini seçene kadar menüyü tekrar eder.
while True:
    # Para ekleme seçeneğini ekrana yazdırır.
    print("\n1 - Para ekle")
    # Harcama yapma seçeneğini ekrana yazdırır.
    print("2 - Harcama yap")
    # Bakiye gösterme seçeneğini ekrana yazdırır.
    print("3 - Bakiye göster")
    # Çıkış seçeneğini ekrana yazdırır.
    print("0 - Çıkış")
    # Kullanıcıdan bir menü seçimi alır.
    secim = input("Seçim: ")
    # Kullanıcı çıkışı seçtiğinde çalışır.
    if secim == "0":
        # Programın kapanacağını bildirir.
        print("Program kapatılıyor.")
        # Menü döngüsünü sonlandırır.
        break
    # Kullanıcı para ekleme seçeneğini seçtiğinde çalışır.
    elif secim == "1":
        # Kullanıcıdan eklenecek para tutarını alır.
        tutar = float(input("Eklenecek tutar: "))
        # Tutarın pozitif olup olmadığını kontrol eder.
        if tutar > 0:
            # Tutarı mevcut bakiyenin üzerine ekler.
            bakiye += tutar
            # Güncel bakiyeyi ekrana yazdırır.
            print("Yeni bakiye:", bakiye)
        # Pozitif olmayan tutarlarda çalışır.
        else:
            # Kullanıcıya geçersiz tutar mesajı verir.
            print("Tutar pozitif olmalıdır.")
    # Kullanıcı harcama seçeneğini seçtiğinde çalışır.
    elif secim == "2":
        # Kullanıcıdan harcama tutarını alır.
        tutar = float(input("Harcama tutarı: "))
        # Harcama tutarının pozitif olup olmadığını kontrol eder.
        if tutar <= 0:
            # Pozitif olmayan tutarı reddeder.
            print("Tutar pozitif olmalıdır.")
        # Harcama tutarının mevcut bakiyeyi aşıp aşmadığını kontrol eder.
        elif tutar > bakiye:
            # Yetersiz bakiye mesajını gösterir.
            print("Yetersiz bakiye.")
        # Tutar geçerli ve bakiye yeterli olduğunda çalışır.
        else:
            # Harcama tutarını mevcut bakiyeden düşer.
            bakiye -= tutar
            # Güncel bakiyeyi ekrana yazdırır.
            print("Yeni bakiye:", bakiye)
    # Kullanıcı bakiye gösterme seçeneğini seçtiğinde çalışır.
    elif secim == "3":
        # Mevcut bakiyeyi ekrana yazdırır.
        print("Mevcut bakiye:", bakiye)
    # Geçerli seçeneklerin dışında bir değer girildiğinde çalışır.
    else:
        # Kullanıcıya geçersiz seçim mesajı verir.
        print("Geçersiz seçim.")
