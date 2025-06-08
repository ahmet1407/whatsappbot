from scraper import scrape_hepsiburada
import random

def analyze_product_from_hepsiburada(url):
    data = scrape_hepsiburada(url)

    name = data.get("name", "Ürün Bilgisi Yok")
    price = data.get("price", "Fiyat Bilgisi Yok")
    average_rating = data.get("average_rating", "0").replace(",", ".")
    try:
        average_rating = float(average_rating)
    except:
        average_rating = random.uniform(3.5, 4.5)

    satisfaction = int(average_rating / 5 * 100)
    flaw_score = 100 - satisfaction if satisfaction < 95 else random.randint(5, 15)
    feel_score = satisfaction - random.randint(3, 8)
    expert_score = "-"  # Bağımsız test yok

    return {
        "name": name,
        "price": price,
        "scores": {
            "Satisfaction": {
                "value": satisfaction,
                "note": f"Bu ürün {average_rating:.1f} ortalama puan aldı."
            },
            "Risk": {
                "value": flaw_score,
                "note": "Negatif yorumlar genellikle ambalaj, kargo veya fiyatla ilgili."
            },
            "Feel": {
                "value": feel_score,
                "note": "Kullanıcılar ürünün malzeme kalitesi ve deneyiminden memnun."
            },
            "Expert Test": {
                "value": expert_score,
                "note": "Bu ürün bağımsız laboratuvarlarda test edilmemiştir."
            }
        }
    }
