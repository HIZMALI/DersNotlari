# Kullanıcıdan sepet tutarını ondalıklı sayı olarak alır.
tutar = float(input("Sepet tutarı (TL): "))

# Sepet tutarı 500 TL veya üzerindeyse ücretsiz kargo uygular.
if tutar >= 500:
    # Ücretsiz kargo koşulu sağlandığında bu mesajı gösterir.
    print("Kargo ücretsiz.")
else:
    # Sepet tutarı sınırın altındaysa kargo ücreti uygulanacağını bildirir.
    print("Kargo ücreti uygulanacak.")

# Sepet tutarını karar sonucundan bağımsız olarak ekrana yazdırır.
print(f"Sepet tutarı: {tutar:.2f} TL")
