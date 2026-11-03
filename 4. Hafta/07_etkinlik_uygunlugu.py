# Kullanıcıdan yaş bilgisini alır.
yas = int(input("Yaş: "))

# Örnekte üyeliğin aktif olup olmadığını Boolean değer olarak tanımlar.
uyelik_aktif = True

# Yaş 18-30 aralığındaysa ve üyelik aktifse kayıt koşullarını sağlanmış kabul eder.
if 18 <= yas <= 30 and uyelik_aktif:
    # İki koşul da doğru olduğunda uygunluk mesajını gösterir.
    print("Gençlik etkinliğine kayıt uygun.")
else:
    # Koşullardan en az biri sağlanmıyorsa uygun olmadığını bildirir.
    print("Kayıt koşulları sağlanmıyor.")
