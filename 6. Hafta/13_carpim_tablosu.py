# Birinci çarpanı 1'den 10'a kadar ilerleten dış döngüyü başlatır.
for birinci in range(1, 11):
    # Her birinci çarpan için ikinci çarpanı 1'den 10'a kadar ilerletir.
    for ikinci in range(1, 11):
        # İki sayıyı çarpar ve işlemi sonuçla birlikte ekrana yazar.
        print(f"{birinci} x {ikinci} = {birinci * ikinci}")
    # Her çarpım grubu bittikten sonra ekranda boş bir satır bırakır.
    print()
