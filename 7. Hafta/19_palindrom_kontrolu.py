# Kullanıcıdan kontrol edilecek metni alır, kenar boşluklarını temizler ve küçük harfe dönüştürür.
metin = input("Kelime: ").strip().lower()

# Dilimlemede negatif adım kullanarak metnin ters halini oluşturur.
ters_metin = metin[::-1]

# Orijinal temizlenmiş metin ile ters metni karşılaştırır.
if metin == ters_metin:
    # İki değer eşitse palindrom sonucunu bildirir.
    print("Palindrom")
else:
    # İki değer eşit değilse palindrom olmadığını bildirir.
    print("Palindrom değil")
