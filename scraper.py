import requests
from bs4 import BeautifulSoup
import re

def scrape_hepsiburada(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Bağlantı sağlanamadı: {e}"}

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        title = soup.find("h1", {"class": re.compile(".*product-name.*")}).get_text(strip=True)
    except:
        title = "Ürün başlığı alınamadı"

    try:
        price_tag = soup.find("span", {"class": re.compile(".*price.*")})
        price = price_tag.get_text(strip=True).replace("\xa0TL", "").replace("TL", "")
    except:
        price = "Fiyat alınamadı"

    try:
        rating_tag = soup.find("span", {"class": re.compile(".*rating-star.*")})
        rating = rating_tag.get_text(strip=True)
    except:
        rating = "Puan alınamadı"

    try:
        comment_section = soup.find("div", {"id": "comments-section"})
        comments = comment_section.get_text(" ", strip=True) if comment_section else ""
        pos_score = comments.lower().count("harika") + comments.lower().count("mükemmel")
        neg_score = comments.lower().count("berbat") + comments.lower().count("kötü")
    except:
        pos_score, neg_score = 0, 0

    summary = {
        "title": title,
        "price": f"{price} TL",
        "rating": rating,
        "positive_mentions": pos_score,
        "negative_mentions": neg_score
    }

    return summary
