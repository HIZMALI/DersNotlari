# Kullanıcıdan yaş bilgisini tam sayı olarak alır.
yas = int(input("Yaş: "))

# Öğrenci durumunu örnek amacıyla Boolean değer olarak tanımlar.
ogrenci = True

# Kullanıcıdan 1 veya 2 olması beklenen bilet türü seçimini alır.
bilet_turu = int(input("1: Standart, 2: Premium -> "))

# Önce negatif yaş değerini geçersiz kabul eder.
if yas < 0:
    # Geçersiz yaş bilgisini kullanıcıya bildirir.
    print("Geçersiz yaş.")
elif bilet_turu != 1 and bilet_turu != 2:
    # İzin verilen bilet türleri dışındaki seçimleri geçersiz kabul eder.
    print("Geçersiz bilet türü.")
elif yas <= 6:
    # 0-6 yaş aralığında bileti ücretsiz olarak belirler.
    print("Bilet: Ücretsiz")
elif yas <= 17:
    # 7-17 yaş aralığında çocuk bileti uygular.
    print("Bilet: Çocuk bileti")
else:
    # 18 ve üzerindeki kişiler için yetişkin bileti uygular.
    print("Bilet: Yetişkin bileti")

    # Öğrenci indirimi yalnızca yetişkin bileti dalında ayrıca kontrol edilir.
    if ogrenci:
        # Yetişkin kullanıcı öğrenci ise indirim uygulanacağını bildirir.
        print("Öğrenci indirimi uygulanabilir.")
