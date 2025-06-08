import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_hepsiburada_product(url):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    try:
        title = soup.find("h1", {"id": "product-name"}).text.strip()
    except:
        title = "Ürün adı bulunamadı"

    try:
        price = soup.find("span", {"data-bind": "markupText:'currentPriceBeforePoint'"}).text.strip()
        price_fraction = soup.find("span", {"data-bind": "markupText:'currentPriceAfterPoint'"}).text.strip()
        price = f"{price},{price_fraction} TL"
    except:
        price = "Fiyat bulunamadı"

    try:
        rating = soup.find("span", {"class": "rating-star"}).text.strip()
    except:
        rating = "Puan yok"

    try:
        total_reviews = soup.find("a", {"href": "#productReviews"}).text.strip()
    except:
        total_reviews = "Yorum yok"

    reviews = []
    review_tags = soup.find_all("div", class_="review-text")
    for tag in review_tags[:5]:
        reviews.append(tag.text.strip())

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "total_reviews": total_reviews,
        "reviews": reviews
    }
