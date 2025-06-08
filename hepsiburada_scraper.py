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
        rating = float(rating_tag.get_text(strip=True).replace(",", "."))  # Örn. "4,6" → 4.6
    except:
        rating = 0

    try:
        review_count_tag = soup.find("a", {"href": re.compile("#yorumlar")})
        review_count = int(re.search(r'\d+', review_count_tag.get_text()).group())
    except:
        review_count = 0

    return {
        "name": title,
        "price": f"{price} TL",
        "average_rating": rating,
        "review_count": review_count
    }
