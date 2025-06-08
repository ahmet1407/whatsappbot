import requests
from bs4 import BeautifulSoup

def scrape_hepsiburada(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Bağlantı hatası: {e}"}

    soup = BeautifulSoup(response.text, "html.parser")

    # Meta title
    try:
        title = soup.find("meta", {"property": "og:title"})["content"]
    except:
        title = "Ürün başlığı bulunamadı"

    # Meta price
    try:
        price = soup.find("meta", {"property": "product:price:amount"})["content"]
    except:
        price = "Fiyat bulunamadı"

    # Meta rating
    try:
        rating = soup.find("span", {"class": "rating-star"}).get_text(strip=True)
    except:
        rating = "Puan bulunamadı"

    # Dummy comment analysis
    pos_score = 7
    neg_score = 2

    return {
        "name": title,
        "price": f"{price} TL" if price != "Fiyat bulunamadı" else price,
        "average_rating": rating,
        "positive_mentions": pos_score,
        "negative_mentions": neg_score
    }
