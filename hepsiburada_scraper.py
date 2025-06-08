import requests
from bs4 import BeautifulSoup

def scrape_hepsiburada(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("h1").text.strip() if soup.find("h1") else "Ürün adı bulunamadı"
    
    try:
        price = soup.find("span", {"data-bind": "markupText:'currentPriceBeforePoint'"}).text
        price += "," + soup.find("span", {"data-bind": "markupText:'currentPriceAfterPoint'"}).text + " TL"
    except:
        price = "Fiyat bulunamadı"

    try:
        rating_text = soup.find("span", {"class": "rating-star"}).text.strip()
        average_rating = float(rating_text.replace(",", "."))
    except:
        average_rating = None

    try:
        review_count = soup.find("a", {"class": "product-review-count"}).text.strip().split()[0]
        review_count = int(review_count.replace(".", ""))
    except:
        review_count = 0

    return {
        "name": title,
        "price": price,
        "average_rating": average_rating,
        "review_count": review_count,
        "comments": []
    }
