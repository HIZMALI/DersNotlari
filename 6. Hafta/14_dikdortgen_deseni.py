# Üç satırlık bir desen oluşturmak için dış döngüyü üç kez çalıştırır.
for _ in range(3):
    # Her satırda beş yıldız yazdırmak için iç döngüyü beş kez çalıştırır.
    for _ in range(5):
        # Yıldızı aynı satırda tutmak için satır sonu yerine boşluk kullanır.
        print("*", end=" ")
    # Beş yıldız tamamlandığında bir alt satıra geçer.
    print()
