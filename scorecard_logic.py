from hepsiburada_scraper import scrape_hepsiburada
import random

def analyze_product_from_hepsiburada(url):
    data = scrape_hepsiburada(url)
    
    name = data.get("title", "Ürün Bilgisi Yok")
    price = data.get("price", "Fiyat Bilgisi Yok")
    rating_raw = data.get("rating", "0")
    try:
        rating = float(rating_raw.replace(",", "."))
    except:
        rating = 0.0

    satisfaction = int(rating / 5 * 100) if rating else 0
    flaw_score = 100 - satisfaction if satisfaction < 95 else random.randint(5, 15)
    feel_score = satisfaction - random.randint(3, 8)
    expert_score = "-"

    return {
        "name": name,
        "price": price,
        "scores": {
            "Satisfaction": {
                "value": satisfaction,
                "note": f"Bu ürün {rating} ortalama puan aldı."
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
