# Örnekte hesabın aktif olduğunu Boolean değer olarak tanımlar.
hesap_aktif = True

# Örnekte parolanın doğru olmadığını Boolean değer olarak tanımlar.
parola_dogru = False

# Önce hesabın aktif olup olmadığını kontrol eder.
if hesap_aktif:
    # Dış koşul doğruysa hesabın aktif olduğunu bildirir.
    print("Hesap aktif.")

    # Parola kontrolü yalnızca hesap aktif olduğunda yapılır.
    if parola_dogru:
        # Parola da doğruysa girişin başarılı olduğunu bildirir.
        print("Giriş başarılı.")
    else:
        # Hesap aktif fakat parola yanlışsa bu mesajı gösterir.
        print("Parola hatalı.")
else:
    # Hesap aktif değilse parola kontrolüne girmeden bu mesajı gösterir.
    print("Hesap pasif.")
