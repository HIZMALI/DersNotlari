# Salonun üç sırasını sırayla dolaşır.
for sira in range(1, 4):
    # Her sıradaki dört koltuğu sırayla dolaşır.
    for koltuk in range(1, 5):
        # O anda işlenen sıra ve koltuk numarasını gösterir.
        print(f"Sıra {sira} - Koltuk {koltuk}")
