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
        title = soup.find("span", attrs={"id": "product-name"}).get_text(strip=True)
    except:
        title = "Ürün Bilgisi Yok"

    try:
        price_tag = soup.find("div", class_="product-price-container")
        price = price_tag.get_text(strip=True).split("TL")[0].strip() + " TL"
    except:
        price = "Fiyat Bilgisi Yok"

    try:
        rating_tag = soup.find("span", class_="rating-star")
        rating = float(rating_tag.get_text(strip=True).replace(",", "."))
    except:
        rating = 0

    return {
        "name": title,
        "price": price,
        "average_rating": rating,
        "review_count": 0,
        "comments": []
    }
