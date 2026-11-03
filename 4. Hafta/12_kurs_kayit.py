# Kullanıcıdan yaş bilgisini tam sayı olarak alır.
yas = int(input("Yaş: "))

# Kullanıcıdan ön test puanını tam sayı olarak alır.
puan = int(input("Ön test puanı (0-100): "))

# Örnekte kontenjanın mevcut olduğunu Boolean değer olarak tanımlar.
kontenjan_var = True

# Yaş veya puan mantıksal sınırların dışındaysa veriyi geçersiz kabul eder.
if yas < 0 or puan < 0 or puan > 100:
    # Geçersiz veri olduğunda diğer kayıt kararlarına geçmez.
    print("Geçersiz veri.")
elif yas < 16:
    # Geçerli veri olsa da yaş 16'nın altındaysa yaş koşulunu reddeder.
    print("Yaş koşulu sağlanmıyor.")
else:
    # Yaş koşulu sağlandığı için puana göre grup belirlemeye başlar.
    if puan >= 80:
        # 80 ve üzerindeki puanları ileri gruba atar.
        grup = "İleri"
    elif puan >= 60:
        # 60-79 arasındaki puanları temel gruba atar.
        grup = "Temel"
    else:
        # 60'ın altındaki puanlarda uygun grup olmadığını None ile belirtir.
        grup = None

    # Bir grup belirlenmişse kayıt için kontenjanı kontrol eder.
    if grup is not None:
        # Kontenjan mevcutsa kayıt uygunluğunu onaylar.
        if kontenjan_var:
            # Belirlenen grup adını sonuç mesajında gösterir.
            print(f"{grup} gruba kayıt uygun.")
        else:
            # Grup uygun olsa da kontenjan yoksa kaydı reddeder.
            print("Kontenjan dolu.")
    else:
        # Hiçbir grup seçilmediyse ön test puanının yetersiz olduğunu bildirir.
        print("Ön test puanı yetersiz.")
