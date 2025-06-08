from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scorecard_logic import analyze_product_from_hepsiburada
import requests
import re

app = Flask(__name__)

def resolve_redirect_if_needed(url):
    if "app.hb.biz" in url or "t.co/" in url:
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            return response.url
        except:
            return url
    return url

def extract_urls(text):
    url_pattern = r'https?://\S+'
    return re.findall(url_pattern, text)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').strip()
    urls = extract_urls(incoming_msg)
    resp = MessagingResponse()

    if not urls:
        resp.message("🔗 Lütfen geçerli bir Hepsiburada ürün linki gönderin.")
        return str(resp)

    valid_url = None
    for url in urls:
        real_url = resolve_redirect_if_needed(url)
        if "hepsiburada.com" in real_url:
            valid_url = real_url
            break

    if not valid_url:
        resp.message("🔗 Lütfen geçerli bir Hepsiburada ürün linki gönderin.")
        return str(resp)

    try:
        result = analyze_product_from_hepsiburada(valid_url)

        name = result['name']
        price = result['price']
        scores = result['scores']

        reply = f"📌 {name}\n💸 Fiyat: {price}\n\n"
        for key, val in scores.items():
            reply += f"✅ {key}: {val['value']}\n{val['note']}\n\n"

    except Exception as e:
        reply = f"❌ Ürün analiz edilirken bir hata oluştu: {str(e)}"

    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
