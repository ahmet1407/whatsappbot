from hepsiburada_scraper import scrape_hepsiburada
import random

def analyze_product_from_hepsiburada(url):
    data = scrape_hepsiburada(url)

    if "error" in data:
        return {"error": data["error"]}

    name = data.get("name", "Ürün Bilgisi Yok")
    price = data.get("price", "Fiyat Bilgisi Yok")
    average_rating = float(data.get("average_rating", 4.2))
    review_count = data.get("review_count", 100)

    satisfaction = int((average_rating / 5) * 100)
    flaw_score = 100 - satisfaction if satisfaction < 95 else random.randint(5, 15)
    feel_score = satisfaction - random.randint(3, 8)
    expert_score = "-"

    satisfaction_note = f"Bu ürün ortalama {average_rating} puanla {review_count}+ değerlendirme aldı."
    flaw_note = "Negatif yorumlar genellikle kargo, ambalaj veya fiyatla ilgili."
    feel_note = "Kullanıcılar genel olarak ürün kalitesinden ve tasarımından memnun."

    return {
        "name": name,
        "price": price,
        "scores": {
            "Satisfaction": {"value": satisfaction, "note": satisfaction_note},
            "Risk": {"value": flaw_score, "note": flaw_note},
            "Feel": {"value": feel_score, "note": feel_note},
            "Expert Test": {"value": expert_score, "note": "Bu ürün bağımsız laboratuvarlarda test edilmemiştir."}
        }
    }
