import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_hepsiburada_v2(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Bağlantı sağlanamadı: {e}"}

    soup = BeautifulSoup(response.text, "html.parser")

    # Ürün başlığını çekmeye çalış
    try:
        title = soup.find("h1").get_text(strip=True)
    except:
        try:
            title = soup.find("span", {"id": "product-name"}).get_text(strip=True)
        except:
            try:
                title = soup.title.get_text(strip=True)
            except:
                title = "Ürün başlığı alınamadı"

    # Fiyat
    try:
        price_span = soup.find("span", string=re.compile(r"TL|\u20ba"))
        price = price_span.get_text(strip=True)
    except:
        price = "Fiyat alınamadı"

    # Ortalama puan
    try:
        rating_tag = soup.find("span", class_=re.compile("rating|star"))
        rating = rating_tag.get_text(strip=True)
    except:
        rating = "0.0"

    # Gömülü JSON varsa onu da dene
    try:
        script_tags = soup.find_all("script")
        for script in script_tags:
            if "window.__INITIAL_STATE__" in script.text:
                json_text = script.text.split('window.__INITIAL_STATE__ = ')[1].split(';')[0].strip()
                parsed_json = json.loads(json_text)
                product = parsed_json.get("product", {}).get("product", {})
                title = product.get("name", title)
                price = str(product.get("price", {}).get("value", price)) + " TL"
                rating = str(product.get("rating", {}).get("average", rating))
                break
    except:
        pass

    return {
        "title": title,
        "price": price,
        "rating": rating
    }
