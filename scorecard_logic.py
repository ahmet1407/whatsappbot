import random

def analyze_by_product_name(name):
    # Şimdilik sabit değerler (ileride scraper ve API ile güncellenebilir)
    price = "429 USD" if "dyson" in name else "Belirlenemedi"
    
    satisfaction = random.randint(85, 95)
    flaw_score = 100 - satisfaction
    feel_score = satisfaction - random.randint(2, 6)
    expert_score = 90 if "dyson" in name else "-"

    return {
        "name": name.title(),
        "price": price,
        "scores": {
            "Satisfaction": {
                "value": satisfaction,
                "note": "Kullanıcıların çoğu ürün performansından memnun."
            },
            "Risk": {
                "value": flaw_score,
                "note": "Olumsuz yorumlar genelde aksesuar veya kargo konularında."
            },
            "Feel": {
                "value": feel_score,
                "note": "Tasarım ve kullanım hissi olumlu yönde."
            },
            "Expert Test": {
                "value": expert_score,
                "note": "Bu ürün bağımsız test sonuçlarına dayalı olarak değerlendirilmiştir." if expert_score != "-" else "Bu ürün bağımsız laboratuvarlarda test edilmemiştir."
            }
        }
    }
