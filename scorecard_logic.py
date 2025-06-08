def generate_scorecard(product_name):
    # Basit örnek, ileride yapay zekaya veya veri tabanına bağlanacak
    if "dyson" in product_name.lower():
        return (
            "🌀 Dyson V15 Detect\n\n"
            "✅ Satisfaction: 92/100\n👍 Müşteri yorumları çok olumlu.\n\n"
            "🧯 Risk: 23/100\n⚠️ Fiyat yüksek bulunmuş.\n\n"
            "💠 Hissiyat: 88/100\n✨ Kaliteli tasarım ve sessiz çalışma.\n\n"
            "⚙️ Uzman Skoru: 90/100\n🔬 Bağımsız testlerde yüksek puan aldı."
        )
    else:
        return f"'{product_name}' için veri bulunamadı. Lütfen daha popüler bir ürün deneyin."
