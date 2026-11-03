# Kullanıcıdan ilk yaş değerini alır.
yas = int(input("Yaş: "))

# Yaş 0'dan küçük veya 120'den büyük olduğu sürece tekrar eder.
while yas < 0 or yas > 120:
    # Kullanıcıya geçersiz veri girdiğini bildirir.
    print("Geçersiz yaş. 0-120 arasında bir değer girin.")
    # Kullanıcıdan yeni bir yaş değeri alır.
    yas = int(input("Yaş: "))

# Geçerli yaş değerini ekrana yazdırır.
print("Kabul edilen yaş:", yas)
