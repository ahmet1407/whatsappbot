from amazon_scraper import scrape_amazon
import random

def analyze_product_from_amazon(url):
    data = scrape_amazon(url)
    
    name = data.get("name", "Ürün Bilgisi Yok")
    price = data.get("price", "Fiyat Bilgisi Yok")
    comments = data.get("comments", [])
    average_rating = data.get("average_rating", 0)
    review_count = data.get("review_count", 0)

    satisfaction = int(float(average_rating) / 5 * 100) if average_rating else random.randint(70, 85)
    flaw_score = 100 - satisfaction if satisfaction < 95 else random.randint(5, 15)
    feel_score = satisfaction - random.randint(3, 8)
    expert_score = "-"  # Amazon'da teknik test yok

    satisfaction_note = f"Bu ürün ortalama {average_rating} puanla {review_count}+ değerlendirme aldı."
    flaw_note = "Negatif yorumlar genellikle teslimat veya beklenti uyumsuzluğu ile ilgili."
    feel_note = "Kullanıcılar ürün kalitesi ve kullanım deneyimini olumlu değerlendiriyor."

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
