# Tahmin edilmesi gereken gizli sayıyı belirler.
gizli_sayi = 7
# Deneme sayacını sıfırdan başlatır.
deneme = 0
# Kullanıcının ilk tahminini alır.
tahmin = int(input("1-10 arasında tahmin: "))
# İlk tahmini deneme sayısına dahil eder.
deneme += 1

# Tahmin gizli sayıdan farklı olduğu sürece tekrar eder.
while tahmin != gizli_sayi:
    # Tahmin gizli sayıdan küçükse çalışır.
    if tahmin < gizli_sayi:
        # Kullanıcıya daha büyük sayı denemesini söyler.
        print("Daha büyük bir sayı dene.")
    # Tahmin gizli sayıdan büyükse çalışır.
    else:
        # Kullanıcıya daha küçük sayı denemesini söyler.
        print("Daha küçük bir sayı dene.")
    # Kullanıcıdan yeni bir tahmin alır.
    tahmin = int(input("Yeni tahmin: "))
    # Her yeni tahminde deneme sayısını bir artırır.
    deneme += 1

# Doğru tahmin yapıldığında başarı mesajını gösterir.
print("Doğru tahmin!")
# Toplam deneme sayısını ekrana yazdırır.
print("Deneme sayısı:", deneme)
