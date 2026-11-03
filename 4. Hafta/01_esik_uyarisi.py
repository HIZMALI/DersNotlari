# Kullanıcıdan güncel stok miktarını tam sayı olarak alır.
stok = int(input("Stok miktarı: "))

# Stok miktarı 5'in altındaysa kritik stok uyarısını çalıştırır.
if stok < 5:
    # Koşul doğru olduğunda kullanıcıya uyarı mesajını gösterir.
    print("Stok kritik seviyede.")

# Bu satır if bloğunun dışında olduğu için her durumda çalışır.
print(f"Güncel stok: {stok}")
