# Üç isimden oluşan başlangıç listesini oluşturur.
isimler = ["Ali", "Cem", "Deniz"]

# Bora adını indeks 1 konumuna ekler ve diğer elemanları sağa kaydırır.
isimler.insert(1, "Bora")

# Birden fazla yeni ismi listenin sonuna ayrı elemanlar olarak ekler.
isimler.extend(["Ece", "Fırat"])

# Güncellenmiş listeyi ekrana yazdırır.
print(isimler)
