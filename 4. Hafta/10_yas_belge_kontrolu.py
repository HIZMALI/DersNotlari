# Kullanıcıdan yaş bilgisini tam sayı olarak alır.
yas = int(input("Yaş: "))

# Örnekte gerekli belgenin var olduğunu Boolean değer olarak tanımlar.
belge_var = True

# Başvuru için önce yaşın en az 18 olup olmadığını kontrol eder.
if yas >= 18:
    # Yaş koşulu sağlanırsa ikinci aşamada belge durumunu kontrol eder.
    if belge_var:
        # Hem yaş hem belge koşulu sağlanıyorsa başvuruyu kabul eder.
        print("Başvuru alınabilir.")
    else:
        # Yaş uygun fakat belge yoksa eksik belge mesajı verir.
        print("Gerekli belge eksik.")
else:
    # Yaş 18'in altındaysa belge kontrolüne girmeden başvuruyu reddeder.
    print("Yaş koşulu sağlanmıyor.")
