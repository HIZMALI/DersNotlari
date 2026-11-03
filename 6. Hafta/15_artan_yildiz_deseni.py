# Satır numarasını 1'den 5'e kadar ilerletir.
for satir in range(1, 6):
    # İç döngüyü o anki satır numarası kadar çalıştırır.
    for _ in range(satir):
        # Yıldızı aynı satıra ekler.
        print("*", end="")
    # O satırın yıldızları tamamlanınca alt satıra geçer.
    print()
