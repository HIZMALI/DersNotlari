# Kullanıcıdan menüdeki işlem numarasını alır.
secim = int(input("1: Ekle, 2: Sil, 3: Listele -> "))

# Kullanıcı 1'i seçtiyse ekleme işlemini belirler.
if secim == 1:
    # Ekleme seçimini kullanıcıya bildirir.
    print("Ekleme işlemi seçildi.")
elif secim == 2:
    # Kullanıcı 2'yi seçtiyse silme işlemini bildirir.
    print("Silme işlemi seçildi.")
elif secim == 3:
    # Kullanıcı 3'ü seçtiyse listeleme işlemini bildirir.
    print("Listeleme işlemi seçildi.")
else:
    # 1, 2 ve 3 dışındaki seçimleri geçersiz kabul eder.
    print("Geçersiz seçim.")
