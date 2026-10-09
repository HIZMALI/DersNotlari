sayi = int(input("Bir tam sayı girin: "))  # Kullanıcıdan karşılaştırmalarda kullanılacak tam sayıyı alır.
elliye_esit_mi = sayi == 50  # Sayının 50'ye eşit olup olmadığını kontrol eder.
elliye_esit_degil_mi = sayi != 50  # Sayının 50'ye eşit olmadığını kontrol eder.
elliden_buyuk_mu = sayi > 50  # Sayının 50'den büyük olup olmadığını kontrol eder.
elliden_kucuk_mu = sayi < 50  # Sayının 50'den küçük olup olmadığını kontrol eder.
elli_ve_uzeri_mi = sayi >= 50  # Sayının 50 veya daha büyük olup olmadığını kontrol eder.
elli_ve_alti_mi = sayi <= 50  # Sayının 50 veya daha küçük olup olmadığını kontrol eder.
print(f"50'ye eşit mi? {elliye_esit_mi}")  # Eşitlik karşılaştırmasının sonucunu gösterir.
print(f"50'ye eşit değil mi? {elliye_esit_degil_mi}")  # Eşit değil karşılaştırmasının sonucunu gösterir.
print(f"50'den büyük mü? {elliden_buyuk_mu}")  # Büyük karşılaştırmasının sonucunu gösterir.
print(f"50'den küçük mü? {elliden_kucuk_mu}")  # Küçük karşılaştırmasının sonucunu gösterir.
print(f"50 ve üzeri mi? {elli_ve_uzeri_mi}")  # Büyük veya eşit karşılaştırmasının sonucunu gösterir.
print(f"50 ve altı mı? {elli_ve_alti_mi}")  # Küçük veya eşit karşılaştırmasının sonucunu gösterir.
