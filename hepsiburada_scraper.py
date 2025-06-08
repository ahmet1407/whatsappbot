import requests
from bs4 import BeautifulSoup

def scrape_hepsiburada(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        name = soup.find("h1", class_="product-name best-price-trick").text.strip()
    except:
        name = "Ürün adı alınamadı"

    try:
        price = soup.find("span", class_="price").text.strip()
    except:
        price = "Fiyat alınamadı"

    try:
        rating_tag = soup.find("span", class_="overall-rating")
        average_rating = float(rating_tag.text.strip().replace(",", "."))
    except:
        average_rating = 0

    try:
        review_count_tag = soup.find("span", class_="total-review-count")
        review_count = int(review_count_tag.text.strip().split()[0])
    except:
        review_count = 0

    comments = []

    return {
        "name": name,
        "price": price,
        "average_rating": average_rating,
        "review_count": review_count,
        "comments": comments
    }
