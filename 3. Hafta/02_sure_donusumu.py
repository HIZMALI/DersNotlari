toplam_saniye = int(input("Toplam saniye: "))  # Kullanıcıdan toplam saniyeyi alır ve tam sayıya dönüştürür.
dakika = toplam_saniye // 60  # Toplam saniyenin içinde kaç tam dakika olduğunu hesaplar.
kalan_saniye = toplam_saniye % 60  # Tam dakikalar ayrıldıktan sonra kalan saniyeyi hesaplar.
print(f"{toplam_saniye} saniye = {dakika} dakika {kalan_saniye} saniye")  # Dönüştürülen süreyi okunur biçimde gösterir.
