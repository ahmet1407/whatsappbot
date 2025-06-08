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
        rating = "0"

    return {
        "title": title,
        "price": f"{price} TL",
        "rating": rating
    }
