import requests
from bs4 import BeautifulSoup
import re

def scrape_amazon_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Ürün ismi
        title = soup.find(id='productTitle')
        name = title.get_text(strip=True) if title else "Ürün adı bulunamadı"

        # Fiyat
        price_tag = soup.select_one('#priceblock_ourprice, #priceblock_dealprice')
        price = price_tag.get_text(strip=True) if price_tag else "Fiyat bilgisi yok"

        # Ortalama puan
        rating_tag = soup.select_one('span.a-icon-alt')
        rating_text = rating_tag.get_text(strip=True) if rating_tag else "0"
        match = re.search(r"(\d+[.,]?\d*)", rating_text)
        rating = float(match.group(1).replace(',', '.')) if match else 0

        # Yorum sayısı
        review_count_tag = soup.select_one('#acrCustomerReviewText')
        review_text = review_count_tag.get_text(strip=True) if review_count_tag else "0"
        review_match = re.search(r"(\d+[.,]?\d*)", review_text.replace('.', ''))
        review_count = int(review_match.group(1)) if review_match else 0

        return {
            "name": name,
            "price": price,
            "average_rating": rating,
            "review_count": review_count,
            "comments": []  # Geliştirme yapılabilir
        }

    except Exception as e:
        return {"error": str(e)}
