import requests
from bs4 import BeautifulSoup

def scrape_amazon(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find(id='productTitle')
    price = soup.find('span', {'class': 'a-price-whole'})
    rating = soup.find('span', {'class': 'a-icon-alt'})
    review_count = soup.find(id='acrCustomerReviewText')

    # Yorumlar için dummy değer, gerçek yorumlar scraping gerektiriyor
    comments = []

    return {
        "name": name.get_text(strip=True) if name else "Bilinmiyor",
        "price": price.get_text(strip=True) + " TL" if price else "Fiyat Yok",
        "average_rating": float(rating.get_text().split()[0].replace(',', '.')) if rating else 0,
        "review_count": int(review_count.get_text().split()[0].replace('.', '')) if review_count else 0,
        "comments": comments
    }
